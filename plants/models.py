from django.db import models

LIFE_FORM_CHOICES = [
    ("forest", "Forest"),
    ("meadow", "Meadow"),
    ("climber", "Climber"),
    ("grassland", "Grassland"),
    ("herb", "Herb"),
    ("shrub", "Shrub"),
    ("tree", "Tree"),
    ("perennial", "Perennial"),
    ("vine", "Vine"),
    ("water", "Water"),
    ("tender", "Tender"),
    ("other", "Other"),
]

class Plant(models.Model):
    plant_id = models.BigAutoField(primary_key=True)
    scientific_name = models.CharField(max_length=100, unique=True, blank=True, null=True)
    synonyms = models.TextField(max_length=255, blank=True, null=True)
    english_name = models.CharField(max_length=100, unique=True, blank=True, null=True)
    distribution_in_Uganda = models.CharField(max_length=100, blank=True, null=True)
    unique_habitat = models.CharField(max_length=100, blank=True, null=True)
    life_form = models.CharField(max_length=100, choices=LIFE_FORM_CHOICES, null=True)
    life_span = models.CharField(max_length=100, blank=True, null=True)
    climate_Impact = models.CharField(max_length=100, blank=True, null=True)
    threats = models.CharField(max_length=100, blank=True, null=True)
    toxicity = models.CharField(max_length=100, blank=True, null=True)
    conservation_status = models.CharField(max_length=100, blank=True, null=True)
    known_values = models.TextField()
    image = models.ImageField(upload_to="plant_images/", blank=True, null=True)
    video = models.FileField(upload_to="plant_videos/", blank=True, null=True)
    audio = models.FileField(upload_to="plant_audio/", blank=True, null=True)
    notes = models.TextField()
    citation = models.CharField(max_length=255)
    contributor = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Plant: {self.english_name}"

class Language(models.Model):
    langauge_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

class PlantName(models.Model):
    plant_name_id = models.BigAutoField(primary_key=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return f"Plant Name: {self.name} - Language: {self.language}"

class MedicinalPlant(models.Model):
    medicinal_plant_id = models.BigAutoField(primary_key=True)
    plant = models.OneToOneField(Plant, on_delete=models.CASCADE)
    health_issues = models.TextField()
    part_used = models.CharField(max_length=100, blank=True, null=True)
    preparation_steps = models.TextField()
    dosage = models.CharField(max_length=100, blank=True, null=True)
    contraindications = models.TextField()
    shelf_life = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField()
    cultural_value = models.TextField()

    def __str__(self):
        return f"Medicinal Info for Plant: {self.plant.english_name}"

class MedicinalPlantName(models.Model):
    medicinal_plant_name_id = models.BigAutoField(primary_key=True)
    medicinal_plant = models.ForeignKey(MedicinalPlant, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return f"Medicinal Plant Name: {self.name} - Language: {self.language}"

class ScientificClarification(models.Model):
    scientific_clarification_id = models.BigAutoField(primary_key=True)
    plant = models.OneToOneField('Plant', on_delete=models.CASCADE)
    kingdom = models.CharField(max_length=100, blank=True, null=True)
    order = models.CharField(max_length=100, blank=True, null=True)
    family = models.CharField(max_length=100, blank=True, null=True)
    genus = models.CharField(max_length=100, blank=True, null=True)
    species = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Scientific Clarification for: {self.plant.english_name}"

class PlantImageGallery(models.Model):
    plant_image_gallery_id = models.BigAutoField(primary_key=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="plant_gallery/", blank=True, null=True)
    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.plant.english_name} - {self.caption}"

class MedicinalPlantImageGallery(models.Model):
    medicinal_plant_image_gallery_id = models.BigAutoField(primary_key=True)
    medicinal_plant = models.ForeignKey(MedicinalPlant, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="medicinal_plant_gallery/", blank=True, null=True)
    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.medicinal_plant.plant.english_name} - {self.caption}"
