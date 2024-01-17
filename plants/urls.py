# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LanguageViewSet, PlantNameViewSet, MedicinalPlantNameViewSet, ScientificClarificationViewSet, PlantImageGalleryViewSet, MedicinalPlantImageGalleryViewSet, PlantViewSet, MedicinalPlantViewSet

router = DefaultRouter()
router.register(r'languages', LanguageViewSet)
router.register(r'plantnames', PlantNameViewSet)
router.register(r'medicinalplantnames', MedicinalPlantNameViewSet)
router.register(r'scientificclarifications', ScientificClarificationViewSet)
router.register(r'plantimagegalleries', PlantImageGalleryViewSet)
router.register(r'medicinalplantimagegalleries', MedicinalPlantImageGalleryViewSet)
router.register(r'plants', PlantViewSet)
router.register(r'medicinalplants', MedicinalPlantViewSet)  # Add this line

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
