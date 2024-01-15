from django.contrib.auth.models import User
from django.db import models
from uuid import uuid4

class FgfUser(User):
    username = None
    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = []

class Contributor(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_valid(self):
        # TODO: check expiry time to invalidate the token
        return True
