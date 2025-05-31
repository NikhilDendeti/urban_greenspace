from django.urls import path
from .views import (
    list_my_spots,
    create_spot,
    list_approved_spots,
    list_pending_spots,
    approve_spot,
    reject_spot
)

urlpatterns = [
    path('', list_approved_spots),
    path('create/', create_spot),
    path('mysubmissions/', list_my_spots),
    path('moderation/pending/', list_pending_spots),
    path('<int:id>/approve/', approve_spot),
    path('<int:id>/reject/', reject_spot),
]