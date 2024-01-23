from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer, UserDetailsSerializer
from rest_framework import serializers
from .models import FgfUser


GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]


class CustomFgfUserRegistrationSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=30, allow_blank=True, allow_null=True, required=True)
    last_name = serializers.CharField(max_length=30, allow_blank=True, allow_null=True, required=True)
    gender = serializers.ChoiceField(choices=GENDER_CHOICES, allow_blank=True, allow_null=True)
    phone_number = serializers.CharField(max_length=30)
    profession = serializers.CharField(max_length=30)


    class Meta:
        model = FgfUser
        fields = ('email', 'password', 'first_name', 'last_name', 'phone_number', 'gender', 'profession')

    def custom_signup(self, request, user):
        # Add logic to determine and set the role based on the registration view
        # You can access the view using self.context['view']
        user.is_verified = True
        from .views import ContributorRegistrationView, MasteruserRegistrationView, SuperuserRegistrationView  # Import the registration views

        view = self.context['view']

        if isinstance(view, ContributorRegistrationView):
            user.is_contributor = True
        elif isinstance(view, MasteruserRegistrationView):
            user.is_masteruser = True
        elif isinstance(view, SuperuserRegistrationView):
            user.is_superuser = True

        user.save()

class FgfUserSerializer(UserDetailsSerializer):
    class Meta:
        model = FgfUser
        fields = ('id', 'email', 'first_name', 'last_name', 'phone_number', 'gender', 'profession', 'date_joined', 'is_verified', 'is_contributor',)


class FgfUserLoginSerializer(LoginSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the 'username' field
        self.fields.pop('username', None)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs['username'] = attrs['email']  # Set 'username' to 'email'
        return attrs