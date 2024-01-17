from pathlib import Path

import os
from datetime import timedelta
from unittest.mock import DEFAULT
import dj_database_url
import environ



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Set the STATIC_ROOT
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Load environment variables from .env
env = environ.Env()
# environ.Env.read_env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-mm!0y=^l3jg0o&3r9eku8tst_q4ug#a!=2rdz25vp)6d09!#su'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ["*"]


# Whitelisting sites
CORS_ALLOWED_ORIGINS = [
    "https://fgfoundation.onrender.com",
    "http://localhost:5173",
]


# Application definition

INSTALLED_APPS = [
    #"daphne",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'fgfAuth',
    # third-party apps
    "cloudinary_storage",
    "cloudinary",
    "django_filters",
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "channels",
    "dj_rest_auth",
    "drf_yasg",
    "djoser",
    "phone_field",
    'huey.contrib.djhuey',
    "cultures",
    "plants",
    # "elasticemailbackend",
    # "djoser.webauthn",
    # local apps

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = 'fgf_application.urls'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = 'fgf_application.wsgi.application'


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        # "rest_framework.authentication.BasicAuthentication",
        # "rest_framework.authentication.SessionAuthentication",
        #"rest_framework.authentication.TokenAuthentication",
    ),
    #"DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 5,
}


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'


AUTH_USER_MODEL = 'fgfAuth.FgfUser'

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=3),
}



# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'fgfsytems@gmail.com'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'fgfsytems@gmail.com'
EMAIL_HOST_PASSWORD = 'ehadmponenmyvgcf'

HUEY = {
    'name': 'fgf_application',
    'backend': 'huey.RedisHuey',
    'backend_options': {
        'host': 'localhost',
        'port': 6379,
    },
    'consumer_options': {
        'workers': 2,  # Adjust the number of worker processes as needed
        'scheduler_interval': 1,
        'loglevel': 'info',
    },
}