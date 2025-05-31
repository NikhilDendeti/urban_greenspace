from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .models import Spot
from .permissions import IsContributorOrReadOnly, IsModerator
from django.shortcuts import get_object_or_404
from rest_framework import status

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_my_spots(request):
    spots = Spot.objects.filter(contributor=request.user).values()
    return JsonResponse(list(spots), safe=False)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_spot(request):
    data = request.data
    user = request.user

    required_fields = ['name', 'latitude', 'longitude', 'spot_type']
    for field in required_fields:
        if field not in data:
            return Response({"error": f"Missing required field: {field}"}, status=400)

    spot = Spot.objects.create(
        name=data['name'],
        latitude=data['latitude'],
        longitude=data['longitude'],
        spot_type=data['spot_type'],
        description=data.get('description', ''),
        plant_species=data.get('plant_species', ''),
        seasonality_notes=data.get('seasonality_notes', ''),
        access_notes=data.get('access_notes', 'Publicly Accessible'),
        safety_notes=data.get('safety_notes', ''),
        image_url=data.get('image_url', ''),
        contributor=user
    )
    return Response({"message": "Spot submitted successfully", "spot_id": spot.id}, status=201)

@api_view(['GET'])
def list_approved_spots(request):
    spots = Spot.objects.filter(status='APPROVED').values()
    return Response(spots)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsModerator])
def list_pending_spots(request):
    spots = Spot.objects.filter(status='PENDING_REVIEW').values()
    return Response(spots)

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsModerator])
def approve_spot(request, id):
    spot = get_object_or_404(Spot, id=id)
    spot.status = 'APPROVED'
    spot.save()
    return Response({"status": "approved"})

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsModerator])
def reject_spot(request, id):
    spot = get_object_or_404(Spot, id=id)
    spot.status = 'REJECTED'
    spot.save()
    return Response({"status": "rejected"})