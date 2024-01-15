import io
import logging
from rest_framework import serializers
from phone_field import PhoneField
from django.conf import settings
from django.contrib.auth.models import User
from djoser.serializers import UserCreateSerializer
from drf_writable_nested import WritableNestedModelSerializer
from drf_extra_fields.fields import Base64FileField, Base64ImageField
from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist
from drf_writable_nested.serializers import WritableNestedModelSerializer

from .models import FgfUser, Contributor, Master, EmailVerificationToken

logger = logging.getLogger(__name__)

class UserSerializer(UserCreateSerializer):
    first_name = serializers.CharField(required=True, allow_blank=True)
    last_name = serializers.CharField(allow_blank=True, required=True)
    email = serializers.EmailField(allow_blank=True, required=True)
    password = serializers.CharField(
        style={"input_type": "password"}, min_length=6, max_length=68, write_only=True
    )
    username = serializers.CharField(allow_blank=True, required=True)

    def validate_email(self, email):
        if User.objects.filter(email=email):
            raise serializers.ValidationError(f"The email '{email}' is already taken")
        return email

    def validate_username(self, username):
        if User.objects.filter(username=username):
            raise serializers.ValidationError(
                f"The username '{username}' is already taken"
            )
        return username

    class Meta(UserCreateSerializer.Meta):
        model = FgfUser
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
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

class EmailVerificationTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailVerificationToken
        fields = "__all__"

class TokenSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    id = serializers.SerializerMethodField()

    class Meta:
        model = Token
        fields = ("id", "role", "key")

    def get_role(self, obj):
        return self._role_and_id(obj)["role"]

    def get_id(self, obj):
        return self._role_and_id(obj)["id"]

    def _role_and_id(self, obj):
        try:
            if obj.user.contributor:
                return {"role": "CONTRIBUTOR", "id": obj.user.contributor.id}
        except ObjectDoesNotExist:
            pass

        try:
            if obj.user.master:
                return {"role": "MASTER", "id": obj.user.master.id}
        except ObjectDoesNotExist:
            pass

        if obj.user.is_staff:
            return {"role": "ADMIN", "id": obj.id}
        else:
            return {"role": "ANONYMOUS", "id": None}
