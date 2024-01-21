# urls.py

from django.urls import path
from .views import (CustomUserRegistrationView, 
                    SuperuserRegistrationView, 
                    MasteruserRegistrationView, 
                    ContributorRegistrationView, 
                    CustomUserLoginView, 
                    CustomUserDetailsView, 
                    CustomUserLogoutView)
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView
from dj_rest_auth.views import PasswordResetConfirmView


urlpatterns = [
    path('api/v1/registration/account-confirm-email/<str:key>/',ConfirmEmailView.as_view(),),
    path('api/v1/register/user/', CustomUserRegistrationView.as_view(), name='register-user'),
    path('api/v1/register/superuser/', SuperuserRegistrationView.as_view(), name='register-superuser'),
    path('api/v1/register/masteruser/', MasteruserRegistrationView.as_view(), name='register-masteruser'),
    path('api/v1/register/contributor/', ContributorRegistrationView.as_view(), name='register-contributor'),
    path('api/v1/fgf/account-confirm-email/',VerifyEmailView.as_view(),name='account_email_verification_sent'),
    path('api/v1/password/reset/confirm/<slug:uidb64>/<slug:token>/',PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('api/v1/logout/', CustomUserLogoutView.as_view(), name='custom-user-logout'),
    path('api/v1/login/', CustomUserLoginView.as_view(), name='user-login'),
    path('api/v1/profile/', CustomUserDetailsView.as_view(), name='custom-user-details'),
    

]

