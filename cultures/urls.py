
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import EthnicityViewSet, EthnicGroupViewSet, ClanViewSet, CulturalKingdomViewSet



router = DefaultRouter()
router.register(r'ethnicities', EthnicityViewSet, basename='ethnicity')
router.register(r'ethnicgroups', EthnicGroupViewSet, basename='ethnicgroup')
router.register(r'clans', ClanViewSet, basename='clan')
router.register(r'culturalkingdoms', CulturalKingdomViewSet, basename='culturalkingdom')



urlpatterns = [
    path('api/v1/', include(router.urls)),
]


