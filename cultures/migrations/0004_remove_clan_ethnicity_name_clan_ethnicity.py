# Generated by Django 5.0.1 on 2024-01-17 12:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cultures", "0003_alter_clan_unique_together_alter_clan_ethnicity_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="clan",
            name="ethnicity_name",
        ),
        migrations.AddField(
            model_name="clan",
            name="ethnicity",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="cultures.ethnicity",
            ),
        ),
    ]
