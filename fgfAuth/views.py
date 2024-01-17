# views.py

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, views, permissions
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from .models import FgfUser, Contributor, Master, EmailVerificationToken
from .permissions import AllowAnonymousPost
from .serializers import UserSerializer, ContributorSerializer, MasterSerializer #EmailVerificationTokenSerializer, TokenSerializer


class UserList(AllowAnonymousPost, viewsets.ModelViewSet):
    serializer_class = UserSerializer
    filterset_fields = ("email", "first_name", "last_name")
    pagination_class = PageNumberPagination
    http_method_names = ["get", "post", "retrieve", "put", "patch"]
    queryset = FgfUser.objects.all()


class MasterView(viewsets.ModelViewSet):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer
    http_method_names = ["get", "post", "retrieve"]


class ContributorView(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    http_method_names = ["get", "post", "retrieve"]


