from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authtoken import views
from django.conf.urls.static import static


admin.site.site_header = "FGF SYSTEMS"
admin.site.site_title = "Welcome to FGF systems "
admin.site.index_title = "Admin Dashboard"


class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["http", "https"]
        return schema

# The documentation
schema_view = get_schema_view(
    openapi.Info(
        title="UGANDA'S BIODIVERSITY PLATFORM",
        default_version="v1",
        description="Design to access endpoints for the learning platform",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="info@fgf.com"),
        license=openapi.License(name="FUTURE GENERATIONS FOUNDATION"),
    ),
    public=True,
    generator_class=BothHttpAndHttpsSchemaGenerator,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    #path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('allauth/', include('allauth.urls')),
    path('allauth/account/', include('allauth.account.urls')),
    path('allauth/socialaccount/', include('allauth.socialaccount.urls')),

    path("", include(("cultures.urls", "cultures"))),
    path("", include(("plants.urls", "plants"))),
    path("", include(("animals.urls", "animals"))),
    path("", include(("accounts.urls", "accounts"))),
    path(
        "swagger<format>/",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    # Media path
    re_path(
        r"^media/(?P<path>.*)$",
        serve,
        {
            "document_root": settings.MEDIA_ROOT,
        },
    ),
]
