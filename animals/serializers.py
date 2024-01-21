# serializers.py

from rest_framework import serializers
from .models import AnimalClassification, Animal, AnimalLocalName

class AnimalClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalClassification
        fields = '__all__'

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'

class AnimalLocalNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalLocalName
        fields = '__all__'
