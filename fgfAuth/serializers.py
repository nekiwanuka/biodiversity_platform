# serializers.py

import logging
from rest_framework import serializers
from django.contrib.auth.models import User
from djoser.serializers import UserCreateSerializer
from drf_writable_nested import WritableNestedModelSerializer
from drf_extra_fields.fields import Base64FileField, Base64ImageField
from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist
from .models import FgfUser, Contributor, Master, EmailVerificationToken

logger = logging.getLogger(__name__)

class UserSerializer(UserCreateSerializer):
    first_name = serializers.CharField(required=True, allow_blank=True)
    last_name = serializers.CharField(allow_blank=True, required=True)
    email = serializers.EmailField(allow_blank=True, required=True)
    password = serializers.CharField(
        style={"input_type": "password"}, min_length=6, max_length=68, write_only=True
    )


    def validate_email(self, email):
        if FgfUser.objects.filter(email=email).exists():
            raise serializers.ValidationError(f"The email '{email}' is already taken")
        return email

    class Meta(UserCreateSerializer.Meta):
        model = FgfUser
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "password",
        )
        

class ContributorSerializer(WritableNestedModelSerializer):
    is_email_verified = serializers.ReadOnlyField(source="user.is_email_verified")
    user = UserSerializer()

    class Meta:
        model = Contributor
        fields = (
            "id",
            "user",
            "date_of_birth",
            "gender",
            "phone_number",
            "is_email_verified",
        )
        read_only_fields = ("id", "is_email_verified")

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user_instance = FgfUser.objects.create(**user_data)
        # Set the password using set_password
        user_instance.set_password(user_data["password"])
        user_instance.save()
        contributor_instance = Contributor.objects.create(user=user_instance, **validated_data)
        return contributor_instance

class MasterSerializer(WritableNestedModelSerializer):
    is_email_verified = serializers.ReadOnlyField(source="user.is_email_verified")
    user = UserSerializer()

    class Meta:
        model = Master
        fields = (
            "id",
            "user",
            "date_of_birth",
            "gender",
            "profession",
            "is_email_verified",
        )
        read_only_fields = ("id", "is_email_verified")

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user_instance = FgfUser.objects.create(**user_data)
        # Set the password using set_password
        user_instance.set_password(user_data["password"])
        user_instance.save()
        master_instance = Master.objects.create(user=user_instance, **validated_data)
        return master_instance



