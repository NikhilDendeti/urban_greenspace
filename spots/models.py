from django.db import models
from django.conf import settings

# Create your models here.
class Spot(models.Model):
    SPOT_TYPES=[
        ('FRUIT_TREE','Fruit Tree'),
        ('HERB_GARDEN','Herb Garden'),
        ('COMMUNITY_PLOT','Community Plot'),
        ('WILD_EDIBLE','Wild Edible'),
    ]
    STATUS=[
        ('PENDING_REVIEW', 'Pending Review'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('NEEDS_INFO', 'Needs Info')
    ]
    name=models.CharField(max_length=25)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    spot_type=models.CharField(max_length=20,choices=SPOT_TYPES)
    description=models.TextField()
    plant_species = models.CharField(max_length=100)
    seasonality_notes=models.TextField()
    access_notes=models.TextField(default="Publicly Accessible", blank=True, null=True)
    safety_notes=models.TextField(blank=True, null=True)
    image_url=models.URLField(max_length=2048, blank=True, null=True)
    contributor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status=models.CharField(max_length=20, choices=STATUS, default='PENDING_REVIEW')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    last_verified_at=models.DateTimeField(blank=True, null=True)
    