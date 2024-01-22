from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class FgfUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class FgfUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=True, null=True)
    profession = models.CharField(max_length=255, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_contributor = models.BooleanField(default=False)
    is_masteruser = models.BooleanField(default=False)

    # New role field
    ROLE_CHOICES = [
        ('contributor', 'Contributor'),
        ('masteruser', 'Masteruser'),
        ('superuser', 'Superuser'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, blank=True, null=True)

    # Use UserManager to manage user creation
    objects = FgfUserManager()

    def save(self, *args, **kwargs):
        # Set boolean flags based on the role
        if self.role == 'contributor':
            self.is_contributor = True
        elif self.role == 'masteruser':
            self.is_masteruser = True
        elif self.role == 'superuser':
            self.is_superuser = True

        super().save(*args, **kwargs)
