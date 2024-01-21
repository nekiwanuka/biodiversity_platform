# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnimalClassificationViewSet, AnimalViewSet, AnimalLocalNameViewSet

router = DefaultRouter()
router.register(r'animal-classifications', AnimalClassificationViewSet, basename='animalclassification')
router.register(r'animals', AnimalViewSet, basename='animal')
router.register(r'animal-local-names', AnimalLocalNameViewSet, basename='animallocalname')

urlpatterns = [
    path('api/', include(router.urls)),
    # Add more URLs as needed
]
