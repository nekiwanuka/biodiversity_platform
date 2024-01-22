# from rest_framework import viewsets
# from django_filters import rest_framework as filters

# from django_filters.rest_framework import SearchFilter
# from .models import Ethnicity, EthnicGroup, Clan, CulturalKingdom
# from .serializers import (
#     EthnicitySerializer,
#     EthnicGroupSerializer,
#     ClanSerializer,
#     CulturalKingdomSerializer,
# )

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters
from .models import Ethnicity, EthnicGroup, Clan, CulturalKingdom
from .serializers import EthnicitySerializer, EthnicGroupSerializer, ClanSerializer, CulturalKingdomSerializer



class EthnicityFilter(filters.FilterSet):
    class Meta:
        model = Ethnicity
        fields = {
            'ethnicity_name': ['exact', 'icontains'],
            # Add other fields as needed
        }

class EthnicityViewSet(viewsets.ModelViewSet):
    queryset = Ethnicity.objects.all()
    serializer_class = EthnicitySerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = EthnicityFilter
    search_fields = ['ethnicity_name', 'region_in_Uganda', 'language', 'denominations']
    pagination_class = PageNumberPagination


class EthnicGroupFilter(filters.FilterSet):
    class Meta:
        model = EthnicGroup
        fields = {
            'ethnic_group_name': ['exact', 'icontains'],
            # Add other fields as needed
        }

class EthnicGroupViewSet(viewsets.ModelViewSet):
    queryset = EthnicGroup.objects.all()
    serializer_class = EthnicGroupSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = EthnicGroupFilter
    search_fields = ['ethnic_group_name', 'region_in_Uganda', 'number_of_ethnicity']
    pagination_class = PageNumberPagination

# Add similar modifications for Clan and CulturalKingdom views

class ClanFilter(filters.FilterSet):
    class Meta:
        model = Clan
        fields = {
            'clan_name': ['exact', 'icontains'],
            # Add other fields as needed
        }

class ClanViewSet(viewsets.ModelViewSet):
    queryset = Clan.objects.all()
    serializer_class = ClanSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ClanFilter
    search_fields = ['clan_name', 'clan_seat', 'totem']
    pagination_class = PageNumberPagination

class CulturalKingdomFilter(filters.FilterSet):
    class Meta:
        model = CulturalKingdom
        fields = {
            'kingdom_name': ['exact', 'icontains'],
            # Add other fields as needed
        }

class CulturalKingdomViewSet(viewsets.ModelViewSet):
    queryset = CulturalKingdom.objects.all()
    serializer_class = CulturalKingdomSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = CulturalKingdomFilter
    search_fields = ['kingdom_name', 'title_of_leader']
    pagination_class = PageNumberPagination
