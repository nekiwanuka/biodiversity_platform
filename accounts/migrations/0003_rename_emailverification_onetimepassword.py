# Generated by Django 5.0.1 on 2024-01-18 21:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_remove_user_date_of_birth_remove_user_profession"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="EmailVerification",
            new_name="OneTimePassword",
        ),
    ]
