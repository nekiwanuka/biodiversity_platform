import os
from pathlib import Path
from dotenv import load_dotenv
from decouple import config, Csv
from datetime import timedelta
import dj_database_url
import environ

# Load environment variables from .env file
load_dotenv()

# Initialize environment variables
DEBUG = os.environ.get('DEBUG', False)
SECRET_KEY = os.environ.get('SECRET_KEY', '3$u^962jf6b$0m8v-(y0u&jvg!89t+s@74q72177!3u)_9y2o3')

BASE_DIR = Path(__file__).resolve().parent.parent


# Configure the database
DATABASES = {"default": dj_database_url.config(default=os.environ.get("DATABASE_URL"))}

ALLOWED_HOSTS = ["*"]

SITE_ID = 1

CORS_ALLOWED_ORIGINS = [
    "https://fgfoundation.onrender.com",
    "http://localhost:5173",
    "https://fgfplatformbackend.onrender.com",
]

INSTALLED_APPS = [
    # Django Default Apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.staticfiles",
    "django.contrib.sessions",
    "django.contrib.messages",

    # Third-party Apps
    "cloudinary_storage",
    "django_filters",
    "corsheaders",
    "rest_framework",
    'rest_framework_simplejwt',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'allauth.socialaccount.providers.google',
    "rest_framework.authtoken",
    "channels",
    "djoser",
    "drf_yasg",
    "phone_field",
    'huey.contrib.djhuey',
    "cultures",
    "plants",
    'animals',
    'accounts',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]
JWT_AUTH_COOKIE = 'my-app-auth'
ROOT_URLCONF = 'fgf_application.urls'

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    'allauth.account.auth_backends.AuthenticationBackend',
)

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),
    'REGISTER_SERIALIZER': 'users.serializers.FgfUserSerializer',
    'USER_DETAILS_SERIALIZER': 'dj_rest_auth.serializers.UserDetailsSerializer'
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'fgf_application.wsgi.application'

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
        'dj_rest_auth.authentication.AllAuthJWTAuthentication',
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 5,
}

REST_USE_JWT = True

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')



MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTH_USER_MODEL = "accounts.FgfUser"

# Token expiration settings
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

# Email configuration
EMAIL_BACKEND = config('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
EMAIL_HOST = config('EMAIL_HOST', default='')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_USE_SSL = config('EMAIL_USE_SSL', default=False, cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')

# Django-allauth settings
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True

ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False

LOGIN_URL = 'https://fgfplatformbackend.onrender.com/api/v1/register/contributor/'
