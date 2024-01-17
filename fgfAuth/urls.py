

# fgfAuth/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserList, MasterView, ContributorView #EmailVerificationView

router = DefaultRouter()
router.register(r'users', UserList, basename='user-list')
router.register(r'masteruser', MasterView, basename='masteruser')
router.register(r'contributor', ContributorView, basename='contributor')

urlpatterns = [
    path('', include(router.urls)),
    # path('verify-email/<str:token>/<str:user_id>/', EmailVerificationView.as_view(), name='verify-email'),
    # Include other custom views or endpoints if needed
]




# from rest_framework.routers import DefaultRouter
# from django.urls import path, include
# from .views import UserList, MasterView, ContributorView, EmailVerificationView

# router = DefaultRouter()
# router.register(r'list', UserList, basename='users')
# router.register(r'masteruser', MasterView, basename='masteruser')
# router.register(r'contributor', ContributorView, basename='contributor')

# urlpatterns = [
#     path('', include(router.urls)),
#     path('email-verification/<uuid:user_id>/<uuid:token>/', EmailVerificationView.as_view(), name='email-verification'),
# ]