from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer, UserDetailsSerializer, LoginSerializer
from rest_framework import serializers
from .models import CustomUser, Superuser, Masteruser, Contributor
from django.db import transaction


GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]

class CustomUserSerializer(RegisterSerializer):
    phone_number = serializers.CharField(max_length=30)
    gender = serializers.ChoiceField(choices=GENDER_CHOICES, allow_blank=True, allow_null=True)
    profession = serializers.CharField(max_length=30)

    class Meta:
        model = CustomUser
        fields = ('pk', 'email', 'phone_number', 'gender', 'profession', 'date_joined')
        read_only_fields = ('pk', 'email', 'date_joined')

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.phone_number = self.data.get('phone_number')
        user.gender = self.data.get('gender')
        user.profession = self.data.get('profession')
        user.save()
        return user

class SuperuserSerializer(CustomUserSerializer):
    class Meta(CustomUserSerializer.Meta):
        model = Superuser

class MasteruserSerializer(CustomUserSerializer):
    class Meta(CustomUserSerializer.Meta):
        model = Masteruser

class ContributorSerializer(CustomUserSerializer):
    class Meta(CustomUserSerializer.Meta):
        model = Contributor



class CustomUserSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        model = CustomUser
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'phone_number', 'gender', 'profession', 'date_joined')
        read_only_fields = ('id', 'email', 'username', 'date_joined', 'last_login')





class CustomUserLoginSerializer(LoginSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the 'username' field
        self.fields.pop('username', None)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs['username'] = attrs['email']  # Set 'username' to 'email'
        return attrs





