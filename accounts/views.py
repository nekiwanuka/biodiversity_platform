from django.db.models import Q
from django.contrib.auth.models import Group
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView
from rest_framework import generics
from .serializers import CustomFgfUserRegistrationSerializer, FgfUserSerializer, FgfUserLoginSerializer
from .models import FgfUser
from rest_framework.generics import ListAPIView



class BaseRoleRegistrationView(RegisterView):
    serializer_class = CustomFgfUserRegistrationSerializer

    def get_queryset(self):
        # Filter users based on verified email status
        return FgfUser.objects.filter(is_verified=True)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        # Add any additional logic after user creation if needed
        return response

class ContributorRegistrationView(BaseRoleRegistrationView):
    pass
    # No need to set role here, it's handled in the serializer

class MasteruserRegistrationView(BaseRoleRegistrationView):
    pass
    # No need to set role here, it's handled in the serializer

class SuperuserRegistrationView(BaseRoleRegistrationView):
    pass
    # No need to set role here, it's handled in the serializer







class ContributorListView(generics.ListAPIView):
    serializer_class = FgfUserSerializer

    def get_queryset(self):
        return FgfUser.objects.filter(is_contributor=True)

class MasterUserListView(generics.ListAPIView):
    serializer_class = FgfUserSerializer

    def get_queryset(self):
        return FgfUser.objects.filter(is_masteruser=True)




class FgfUserLoginView(LoginView):
    serializer_class = FgfUserLoginSerializer

class FgfUserLogoutView(LogoutView):
    pass
