from django_filters import rest_framework as filters
from django import views
from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, filters, permissions
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.status import HTTP_200_OK,HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.views import APIView 
from fgfAuth.models import *
from .permissions import AllowAnonymousPost 
from .serializers import *

class UserList(AllowAnonymousPost, viewsets.ModelViewSet):
    serializer_class = UserSerializer
    filterset_fields = ("username", "email", "first_name", "last_name")
    pagination_class = PageNumberPagination
    http_method_names = ["get", "post", "retrieve", "put", "patch"]
    queryset = User.objects.all()


    # def list(self, request):
    #     queryset = User.objects.all()
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def create(self, request):
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=HTTP_201_CREATED)
    #     return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    # def retrieve(self, request, pk=None):
    #     queryset = User.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)

    # def update(self, request, pk=None):
    #     instance = User.objects.get(id=pk)
    #     serializer = UserSerializer(instance, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    # def destroy(self, request, pk=None):
    #     instance = User.objects.get(id=pk)
    #     instance.delete()
    #     return Response(status=HTTP_204_NO_CONTENT)


class MasterView(viewsets.ModelViewSet):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer
    http_method_names = ["get", "post", "retrieve" ]


class ContributorView(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    http_method_names = ["get", "post", "retrieve" ]






class EmailVerificationView(views.APIView):
    def get(self, request, **kwargs):
        token_id, user_id = kwargs["token"], kwargs["user_id"]
        token = EmailVerificationToken.objects.get(id=token_id)
        if not token.verified and token.is_valid():
            token.verified = True
            token.save()
            return Response(
                {"message": "Email successfully verified"}, status=HTTP_200_OK
            )
        else:
            return Response(
                {"error": "Verification token is invalid"}, status=HTTP_400_BAD_REQUEST
            )
