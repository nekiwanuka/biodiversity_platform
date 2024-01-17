# myapp/serializers.py
from rest_framework import serializers
from .models import Ethnicity, EthnicGroup, Clan, CulturalKingdom

class EthnicitySerializer(serializers.ModelSerializer):
    total_entries = serializers.SerializerMethodField()

    class Meta:
        model = Ethnicity
        fields = '__all__'

    def get_total_entries(self, obj):
        return Clan.objects.filter(ethnicity=obj).count()

class EthnicGroupSerializer(serializers.ModelSerializer):
    total_entries = serializers.SerializerMethodField()

    class Meta:
        model = EthnicGroup
        fields = '__all__'

    def get_total_entries(self, obj):
        return Clan.objects.filter(ethnic_group=obj).count()

class ClanSerializer(serializers.ModelSerializer):
    total_entries = serializers.SerializerMethodField()

    class Meta:
        model = Clan
        fields = '__all__'

    def get_total_entries(self, obj):
        return Clan.objects.filter(clan_name=obj.clan_name).count()

class CulturalKingdomSerializer(serializers.ModelSerializer):
    total_entries = serializers.SerializerMethodField()

    class Meta:
        model = CulturalKingdom
        fields = '__all__'

    def get_total_entries(self, obj):
        return Clan.objects.filter(cultural_kingdom=obj).count()
