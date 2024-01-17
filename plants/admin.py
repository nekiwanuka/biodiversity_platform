# admin.py
from django.contrib import admin
from .models import Language, PlantName, MedicinalPlantName, ScientificClarification, PlantImageGallery, MedicinalPlantImageGallery, Plant, MedicinalPlant

@admin.register(Language, PlantName, MedicinalPlantName, ScientificClarification, PlantImageGallery, MedicinalPlantImageGallery)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('__str__',)  # Add other fields you want to display in the admin list

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('english_name', 'scientific_name', 'contributor', 'date_added', 'date_modified')
    search_fields = ('english_name', 'scientific_name', 'contributor')
    ordering = ('-date_added',)

@admin.register(MedicinalPlant)
class MedicinalPlantAdmin(admin.ModelAdmin):
    list_display = ('plant', 'health_issues', 'part_used', 'cultural_value')
    search_fields = ('plant__english_name', 'health_issues', 'part_used', 'cultural_value')
