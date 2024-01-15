from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *


router = DefaultRouter()
router.register(r'list', UserList, basename='users')
router.register(r'masteruser', MasterView, basename='masteruser')
router.register(r'contributor', ContributorView, basename='contributor')

urlpatterns =[
    path('', include(router.urls)),
    #path('masteruser/', MasterView.as_view(), name='masteruser'),
    #path('contributor/', MasterView.as_view(), name='contributor'),
]
#urlpatterns = router.urls