from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import AnimalClassification, Animal, AnimalLocalName
from .serializers import AnimalClassificationSerializer, AnimalSerializer, AnimalLocalNameSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10  # Adjust the page size as needed
    page_size_query_param = 'page_size'
    max_page_size = 100


class AnimalClassificationViewSet(viewsets.ModelViewSet):
    queryset = AnimalClassification.objects.all()
    serializer_class = AnimalClassificationSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['kingdom_name', 'species', 'animal_class']
    ordering_fields = ['kingdom_name', 'species', 'animal_class']
    pagination_class = PageNumberPagination

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['english_name', 'scientific_name', 'areas_in_Uganda']
    ordering_fields = ['english_name', 'scientific_name', 'areas_in_Uganda']
    pagination_class = PageNumberPagination

class AnimalLocalNameViewSet(viewsets.ModelViewSet):
    queryset = AnimalLocalName.objects.all()
    serializer_class = AnimalLocalNameSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['local_name', 'language']
    ordering_fields = ['local_name', 'language']
    pagination_class = PageNumberPagination