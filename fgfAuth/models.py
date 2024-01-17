# models.py

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from uuid import uuid4

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

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password=password, **extra_fields)

class FgfUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = FgfUserManager()

    def __str__(self):
        return self.email

class Contributor(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]
    user = models.OneToOneField(FgfUser, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    
    def __str__(self):
        return f"{self.id}: {self.user.first_name} {self.user.last_name}"

    def is_email_verified(self):
        return bool(
            EmailVerificationToken.objects.filter(user=self.user, verified=True)
        )

class Master(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]
    user = models.OneToOneField(FgfUser, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    profession = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return f"{self.id}: {self.user.first_name} {self.user.last_name}"

    def is_email_verified(self):
        return bool(
            EmailVerificationToken.objects.filter(user=self.user, verified=True)
        )

class EmailVerificationToken(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    user = models.ForeignKey(FgfUser, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_valid(self):
        # TODO: check expiry time to invalidate the token
        return True
