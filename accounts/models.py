# accounts/models.py
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.db import models
from django.utils.translation import gettext_lazy as _
from .manager import UserManager
AUTH_PROVIDERS = {"email": "email", "google": "google", "facebook": "facebook"}


# class UserManager(BaseUserManager):
#     def create_user(self, email, first_name, last_name, password=None, **extra_fields):
#         if not email:
#             raise ValueError(_("The Email field must be set"))
#         email = self.normalize_email(email)
#         user = self.model(
#             email=email, first_name=first_name, last_name=last_name, **extra_fields
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_contributor(
#         self, email, first_name, last_name, password=None, **extra_fields
#     ):
#         extra_fields.setdefault("is_contributor", True)
#         return self.create_user(email, first_name, last_name, password, **extra_fields)

#     def create_admin(self, email, first_name, last_name, password=None, **extra_fields):
#         return self._create_user(email, first_name, last_name, password, is_staff=True, **extra_fields)

#     # def create_superuser(self, email, password=None, **extra_fields):
#     #     extra_fields.setdefault("is_staff", True)
#     #     extra_fields.setdefault("is_superuser", True)
#     #     return self._create_user(email, "Admin", "User", password, **extra_fields)

#     def _create_user(self, email, first_name, last_name, password=None, **extra_fields):
#         email = self.normalize_email(email)
#         user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, verbose_name=_("Email Address"))
    first_name = models.CharField(max_length=100, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=100, verbose_name=_("Last Name"))   
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_contributor = models.BooleanField(default=False)  # Add this field
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]


    objects = UserManager()
    def __str__(self):
        return self.email
    # Add your custom fields and methods here
    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def token(self):
      pass

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Contributor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def get_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"
    def tokens(self):
        pass

class OneTimePassword(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} passcode"