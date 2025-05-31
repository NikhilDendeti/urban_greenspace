from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsContributorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.contributor == request.user or request.user.is_staff

class IsModerator(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff