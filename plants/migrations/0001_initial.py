# Generated by Django 5.0.1 on 2024-01-20 22:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Language",
            fields=[
                ("langauge_id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=100, null=True, unique=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MedicinalPlant",
            fields=[
                (
                    "medicinal_plant_id",
                    models.BigAutoField(primary_key=True, serialize=False),
                ),
                ("health_issues", models.TextField()),
                ("part_used", models.CharField(blank=True, max_length=100, null=True)),
                ("preparation_steps", models.TextField()),
                ("dosage", models.CharField(blank=True, max_length=100, null=True)),
                ("contraindications", models.TextField()),
                ("shelf_life", models.CharField(blank=True, max_length=100, null=True)),
                ("notes", models.TextField()),
                ("cultural_value", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Plant",
            fields=[
                ("plant_id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "scientific_name",
                    models.CharField(
                        blank=True, max_length=100, null=True, unique=True
                    ),
                ),
                ("synonyms", models.TextField(blank=True, max_length=255, null=True)),
                (
                    "english_name",
                    models.CharField(
                        blank=True, max_length=100, null=True, unique=True
                    ),
                ),
                (
                    "distribution_in_Uganda",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "unique_habitat",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "life_form",
                    models.CharField(
                        choices=[
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
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                ("life_span", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "climate_Impact",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("threats", models.CharField(blank=True, max_length=100, null=True)),
                ("toxicity", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "conservation_status",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("known_values", models.TextField()),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="plant_images/"),
                ),
                (
                    "video",
                    models.FileField(blank=True, null=True, upload_to="plant_videos/"),
                ),
                (
                    "audio",
                    models.FileField(blank=True, null=True, upload_to="plant_audio/"),
                ),
                ("notes", models.TextField()),
                ("citation", models.CharField(max_length=255)),
                ("contributor", models.CharField(max_length=100)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("date_modified", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="MedicinalPlantImageGallery",
            fields=[
                (
                    "medicinal_plant_image_gallery_id",
                    models.BigAutoField(primary_key=True, serialize=False),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="medicinal_plant_gallery/"
                    ),
                ),
                ("caption", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "medicinal_plant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="plants.medicinalplant",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MedicinalPlantName",
            fields=[
                (
                    "medicinal_plant_name_id",
                    models.BigAutoField(primary_key=True, serialize=False),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=255, null=True, unique=True
                    ),
                ),
                (
                    "language",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="plants.language",
                    ),
                ),
                (
                    "medicinal_plant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="plants.medicinalplant",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="medicinalplant",
            name="plant",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="plants.plant"
            ),
        ),
        migrations.CreateModel(
            name="PlantImageGallery",
            fields=[
                (
                    "plant_image_gallery_id",
                    models.BigAutoField(primary_key=True, serialize=False),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="plant_gallery/"
                    ),
                ),
                ("caption", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "plant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="plants.plant"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PlantName",
            fields=[
                (
                    "plant_name_id",
                    models.BigAutoField(primary_key=True, serialize=False),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=255, null=True, unique=True
                    ),
                ),
                (
                    "language",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="plants.language",
                    ),
                ),
                (
                    "plant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="plants.plant"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ScientificClarification",
            fields=[
                (
                    "scientific_clarification_id",
                    models.BigAutoField(primary_key=True, serialize=False),
                ),
                ("kingdom", models.CharField(blank=True, max_length=100, null=True)),
                ("order", models.CharField(blank=True, max_length=100, null=True)),
                ("family", models.CharField(blank=True, max_length=100, null=True)),
                ("genus", models.CharField(blank=True, max_length=100, null=True)),
                ("species", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "plant",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="plants.plant"
                    ),
                ),
            ],
        ),
    ]