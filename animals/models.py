from django.db import models
# Create your models here.



class AnimalClassification(models.Model):
    animal_classification_id = models.AutoField(primary_key=True)
    kingdom_name = models.CharField(max_length=250)
    species = models.CharField(max_length=250)
    number_of_species = models.IntegerField(default=1, null=True)
    animal_class = models.CharField(max_length=250)
    order = models.CharField(max_length=250)
    domestic = models.BooleanField(default=False)
    wild_animal = models.BooleanField(default=False)

    def __str__(self):
        return self.animal_class


class Animal(models.Model):
    animal_id = models.AutoField(primary_key=True)
    english_name = models.CharField(max_length=250)
    scientific_name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    areas_in_Uganda = models.CharField(max_length=250)

    animal_classifications = models.ForeignKey(
        AnimalClassification, on_delete=models.SET_NULL, null=True
    )
    known_values = models.TextField()
    value_details = models.TextField()
    unique_habitat = models.CharField(max_length=250)
    toxicity_to_humans = models.CharField(max_length=250)
    diet = models.CharField(max_length=250)
    behavior = models.CharField(max_length=250)
    habitat_impact = models.CharField(max_length=250)
    conservation_status = models.CharField(max_length=250)
    conservation_measures = models.CharField(max_length=250)
    reproduction = models.CharField(max_length=250)
    gestation_period = models.CharField(max_length=250)
    life_span = models.CharField(max_length=250)
    predators = models.TextField()
    prey = models.TextField()
    ethical_medicinal_uses = models.TextField()
    threats = models.TextField()
    notes = models.TextField()
    image = models.ImageField(upload_to="animal_images", null=True, blank=True)
    video = models.FileField(upload_to="animal_videos", null=True, blank=True)
    audio = models.FileField(upload_to="animal_audios", null=True, blank=True)
    citation = models.TextField()
    date_entered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.english_name} ({self.scientific_name})"


class AnimalLocalName(models.Model):
    animal_local_name_id = models.AutoField(primary_key=True)
    local_name = models.CharField(max_length=250)
    language = models.CharField(max_length=250)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.local_name} ({self.language}) for {self.animal.english_name} ({self.animal.scientific_name})"
