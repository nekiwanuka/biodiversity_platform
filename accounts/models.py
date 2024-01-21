from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=True, null=True)
    profession = models.CharField(max_length=255, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_contributor = models.BooleanField(default=False)
    is_masteruser = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

class Superuser(models.Model):
    superuser = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        existing_user = CustomUser.objects.filter(email=self.superuser.email).first()
        if existing_user:
            existing_user.is_superuser = True
            existing_user.save()
        else:
            self.superuser.is_superuser = True
            self.superuser.save()
        super().save(*args, **kwargs)

class Masteruser(models.Model):
    masteruser = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        existing_user = CustomUser.objects.filter(email=self.masteruser.email).first()
        if existing_user:
            existing_user.is_masteruser = True
            existing_user.save()
        else:
            self.masteruser.is_masteruser = True
            self.masteruser.save()
        super().save(*args, **kwargs)

class Contributor(models.Model):
    contributor = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        existing_user = CustomUser.objects.filter(email=self.contributor.email).first()
        if existing_user:
            existing_user.is_contributor = True
            existing_user.save()
        else:
            self.contributor.is_contributor = True
            self.contributor.save()
        super().save(*args, **kwargs)
