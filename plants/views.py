# views.py
# views.py
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from .models import Plant, Language, PlantName, MedicinalPlant, MedicinalPlantName, ScientificClarification, PlantImageGallery, MedicinalPlantImageGallery
from .serializers import PlantSerializer, LanguageSerializer, PlantNameSerializer, MedicinalPlantSerializer, MedicinalPlantNameSerializer, ScientificClarificationSerializer, PlantImageGallerySerializer, MedicinalPlantImageGallerySerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10  # Adjust the page size as needed
    page_size_query_param = 'page_size'
    max_page_size = 100

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    pagination_class = StandardResultsSetPagination

class PlantNameViewSet(viewsets.ModelViewSet):
    queryset = PlantName.objects.all()
    serializer_class = PlantNameSerializer
    pagination_class = StandardResultsSetPagination

class MedicinalPlantNameViewSet(viewsets.ModelViewSet):
    queryset = MedicinalPlantName.objects.all()
    serializer_class = MedicinalPlantNameSerializer
    pagination_class = StandardResultsSetPagination

class ScientificClarificationViewSet(viewsets.ModelViewSet):
    queryset = ScientificClarification.objects.all()
    serializer_class = ScientificClarificationSerializer
    pagination_class = StandardResultsSetPagination

class PlantImageGalleryViewSet(viewsets.ModelViewSet):
    queryset = PlantImageGallery.objects.all()
    serializer_class = PlantImageGallerySerializer
    pagination_class = StandardResultsSetPagination

class MedicinalPlantImageGalleryViewSet(viewsets.ModelViewSet):
    queryset = MedicinalPlantImageGallery.objects.all()
    serializer_class = MedicinalPlantImageGallerySerializer
    pagination_class = StandardResultsSetPagination

class MedicinalPlantViewSet(viewsets.ModelViewSet):
    queryset = MedicinalPlant.objects.all()
    serializer_class = MedicinalPlantSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['health_issues', 'part_used', 'preparation_steps', 'dosage', 'contraindications', 'shelf_life', 'notes', 'cultural_value']
    ordering_fields = '__all__'

from rest_framework import viewsets
from .models import Plant, Language, PlantName, MedicinalPlant, MedicinalPlantName, ScientificClarification, PlantImageGallery, MedicinalPlantImageGallery
from .serializers import PlantSerializer, LanguageSerializer, PlantNameSerializer, MedicinalPlantSerializer, MedicinalPlantNameSerializer, ScientificClarificationSerializer, PlantImageGallerySerializer, MedicinalPlantImageGallerySerializer

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class PlantNameViewSet(viewsets.ModelViewSet):
    queryset = PlantName.objects.all()
    serializer_class = PlantNameSerializer

class MedicinalPlantNameViewSet(viewsets.ModelViewSet):
    queryset = MedicinalPlantName.objects.all()
    serializer_class = MedicinalPlantNameSerializer

class ScientificClarificationViewSet(viewsets.ModelViewSet):
    queryset = ScientificClarification.objects.all()
    serializer_class = ScientificClarificationSerializer

class PlantImageGalleryViewSet(viewsets.ModelViewSet):
    queryset = PlantImageGallery.objects.all()
    serializer_class = PlantImageGallerySerializer

class MedicinalPlantImageGalleryViewSet(viewsets.ModelViewSet):
    queryset = MedicinalPlantImageGallery.objects.all()
    serializer_class = MedicinalPlantImageGallerySerializer

class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

class MedicinalPlantViewSet(viewsets.ModelViewSet):
    queryset = MedicinalPlant.objects.all()
    serializer_class = MedicinalPlantSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['health_issues', 'part_used', 'preparation_steps', 'dosage', 'contraindications', 'shelf_life', 'notes', 'cultural_value']
    ordering_fields = '__all__'