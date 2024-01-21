from dj_rest_auth.registration.views import RegisterView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserSerializer, SuperuserSerializer, MasteruserSerializer, ContributorSerializer
from rest_framework import generics
from dj_rest_auth.views import LoginView, LogoutView
from dj_rest_auth.serializers import UserDetailsSerializer
from .serializers import CustomUserLoginSerializer




class CustomUserRegistrationView(RegisterView):
    serializer_class = CustomUserSerializer

class SuperuserRegistrationView(RegisterView):
    serializer_class = SuperuserSerializer

class MasteruserRegistrationView(RegisterView):
    serializer_class = MasteruserSerializer

class ContributorRegistrationView(RegisterView):
    serializer_class = ContributorSerializer



# class CustomUserLoginView(TokenObtainPairView):
#     serializer_class = UserLoginSerializer
#     permission_classes = []
    
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         if serializer.is_valid():
#             data = serializer.validated_data
#             return Response(data, status.HTTP_200_OK)


# @login_required
# # class seeView(generics.ListAPIView):
# def see(request):
#     # Your view logic here
#     return JsonResponse({'message': 'Hello, this is the see view!'})

class CustomUserLoginView(LoginView):
    serializer_class = CustomUserLoginSerializer

class CustomUserDetailsView(generics.RetrieveUpdateAPIView):
    serializer_class = UserDetailsSerializer

    def get_object(self):
        return self.request.user
    

class CustomUserLogoutView(LogoutView):
    pass