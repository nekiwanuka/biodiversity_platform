from django.db import models
from django.utils.translation import gettext_lazy as _

class Clan(models.Model):
    clan_id = models.BigAutoField(primary_key=True)
    ethnicity = models.ForeignKey('Ethnicity', on_delete=models.CASCADE, blank=True, null=True)
    clan_name = models.CharField(max_length=250, blank=True)
    clan_seat = models.CharField(max_length=250, blank=True)
    clan_anthem = models.TextField(blank=True, null=True)
    clan_roles = models.TextField(blank=True, null=True)

    # Image fields for relevant attributes
    totem_image = models.ImageField(upload_to="clan_images", null=True, blank=True)

    totem = models.CharField(max_length=250, blank=True)
    secondary_totem = models.CharField(max_length=250, blank=True)
    clan_history = models.TextField(blank=True)
    clan_leader_title = models.CharField(max_length=250, blank=True)
    clan_leader_name = models.CharField(max_length=250, blank=True)
    cultural_sites = models.TextField(blank=True)
    male_names = models.TextField(blank=True)
    female_names = models.TextField(blank=True)
    reserved_male_names = models.TextField(blank=True)
    reserved_female_names = models.TextField(blank=True)
    taboos = models.TextField(blank=True)
    lead_god = models.CharField(max_length=250, blank=True)
    other_gods = models.CharField(max_length=250, blank=True)

    # FileField for audio
    audio = models.FileField(upload_to="ethnic_group_audio", blank=True, null=True)

    notes = models.TextField(blank=True, null=True)
    contributor_name = models.CharField(max_length=250, blank=True, null=True)
    citation = models.TextField(blank=True, null=True)
    date_entered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.clan_name

    @property
    def total_entries(self):
        return Clan.objects.filter(clan_name=self.clan_name).count()


class CulturalKingdom(models.Model):
    LEADER_CHOICES = [
        ('king', _('King')),
        ('chief', _('Chief')),
        # Add other choices as needed
    ]

    cultural_kingdom_id = models.BigAutoField(primary_key=True)
    kingdom_name = models.CharField(max_length=250)
    title_of_leader = models.CharField(max_length=250, blank=True, null=True, choices=LEADER_CHOICES)
    number_of_clans = models.IntegerField(default=1, null=True)
    leader_name = models.CharField(max_length=250, blank=True, null=True)
    contributor_name = models.CharField(max_length=250, blank=True, null=True)
    citation = models.TextField(blank=True, null=True)
    date_entered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.kingdom_name

    @property
    def total_entries(self):
        return Clan.objects.filter(cultural_kingdom=self).count()


class Ethnicity(models.Model):
    ethnicity_id = models.BigAutoField(primary_key=True)
    ethnicity_name = models.CharField(max_length=250, unique=True)
    region_in_Uganda = models.CharField(max_length=250, blank=True, null=True)
    language = models.CharField(max_length=250, blank=True, null=True)

    # Image fields for relevant attributes
    common_food_types = models.TextField(blank=True, null=True)
    staple_food = models.CharField(max_length=250, blank=True, null=True)
    staple_food_image = models.ImageField(upload_to='ethnicity_images/', blank=True, null=True)
    cuisines = models.TextField(blank=True, null=True)
    main_cash_crop = models.CharField(max_length=250, blank=True, null=True)
    main_cash_crop_image = models.ImageField(upload_to='ethnicity_images/', blank=True, null=True)
    leisure_activities = models.TextField(blank=True, null=True)
    entertainment_activities = models.TextField(blank=True, null=True)
    denominations = models.TextField(blank=True, null=True)
    universal_rituals = models.TextField(blank=True, null=True)
    ceremonies = models.TextField(blank=True, null=True)
    contributor_name = models.CharField(max_length=250, blank=True, null=True)
    citation = models.TextField(blank=True, null=True)
    date_entered = models.DateTimeField(auto_now_add=True)

    @property
    def total_entries(self):
        return Clan.objects.filter(ethnicity=self).count()

    def __str__(self):
        return self.ethnicity_name


class EthnicGroup(models.Model):
    ethnic_group_id = models.BigAutoField(primary_key=True)
    ethnic_group_name = models.CharField(max_length=250, blank=True, null=True)
    region_in_Uganda = models.CharField(max_length=250, blank=True, null=True)
    number_of_ethnicity = models.IntegerField(default=1, blank=True, null=True)
    number_of_languages = models.IntegerField(default=1, null=True)
    number_of_kingdoms_or_chiefdoms = models.IntegerField(default=1, null=True)

    # FileField for audio
    audio = models.FileField(upload_to="ethnic_group_audio", blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    contributor_name = models.CharField(max_length=250, blank=True, null=True)
    citation = models.TextField(blank=True, null=True)
    date_entered = models.DateTimeField(auto_now_add=True)

    @property
    def total_entries(self):
        return Clan.objects.filter(ethnic_group=self).count()

    def __str__(self):
        return self.ethnic_group_name
