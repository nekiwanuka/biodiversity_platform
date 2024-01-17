# serializers.py
from rest_framework import serializers
from .models import Plant, Language, PlantName, MedicinalPlant, MedicinalPlantName, ScientificClarification, PlantImageGallery, MedicinalPlantImageGallery

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class PlantNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantName
        fields = '__all__'

class MedicinalPlantNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicinalPlantName
        fields = '__all__'

class ScientificClarificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScientificClarification
        fields = '__all__'

class PlantImageGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantImageGallery
        fields = '__all__'

class MedicinalPlantImageGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicinalPlantImageGallery
        fields = '__all__'

class PlantSerializer(serializers.ModelSerializer):
    total_entries = serializers.SerializerMethodField()
    language_set = LanguageSerializer(many=True, read_only=True)
    plantname_set = PlantNameSerializer(many=True, read_only=True)
    medicinalplant = serializers.PrimaryKeyRelatedField(read_only=True)
    scientificclarification = ScientificClarificationSerializer(read_only=True)
    plantimagegallery_set = PlantImageGallerySerializer(many=True, read_only=True)

    class Meta:
        model = Plant
        fields = '__all__'

    def get_total_entries(self, obj):
        return Plant.objects.count()

class MedicinalPlantSerializer(serializers.ModelSerializer):
    total_entries = serializers.SerializerMethodField()
    medicinalplantname_set = MedicinalPlantNameSerializer(many=True, read_only=True)
    medicinalplantimagegallery_set = MedicinalPlantImageGallerySerializer(many=True, read_only=True)

    class Meta:
        model = MedicinalPlant
        fields = '__all__'

    def get_total_entries(self, obj):
        return MedicinalPlant.objects.count()
