# Jazzmin - settings import:
from .jazzmin import GLOBAL_JAZZMIN_SETTINGS

# Python - libraries import:
from pathlib import Path
import os

# Main application Constance's:
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', default=['*'])
DEBUG = int(os.environ.get('DEBUG', default=True))
BASE_DIR = Path(__file__).resolve().parent.parent
DJANGO_SETTINGS_MODULE = 'alpenwegs.settings'
APP_NAME = 'AlpenWegs'
VERSION = '0.1a'

# Database Constance's:
DB_PASS = os.environ.get('DB_PASS', default='jt3g339d25rg0ea24')
DB_USER = os.environ.get('DB_USER', default='postgres_admin')
DB_HOST = os.environ.get('DB_HOST', default='127.0.0.1')
DB_NAME = os.environ.get('DB_NAME', default='alpenwegs')
DB_TYPE = os.environ.get('DB_TYPE', default='sqlite3')
DB_PORT = os.environ.get('DB_PORT', default=5432)

# Redis Constance's:
REDIS_HOST = os.environ.get('REDIS_HOST', default='127.0.0.1')
REDIS_PORT = os.environ.get('REDIS_PORT', default=6379)

# Application keys Constance's:
SECRET_KEY = os.environ.get('SECRET_KEY',
    default='django-insecure-#8$u0eijwv%8v$fm!7z62ogxavmv-prab76=f2mg$63d&6kngj')
CRYPTO_KEY = os.environ.get('CRYPTO_KEY',
    default=b'kKMcugPPwQaft1m4-G9kx7urqWhz6sh0hKcJmFNqiOQ=')

# Application configuration:
INSTALLED_APPS = [
    # Django Jazzmin:
    'jazzmin',
    
    # Django apps:
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',

    # Celery and channels:
    'django_celery_beat',
    'channels',

    # Django rest framework:
    'rest_framework.authtoken',
    'rest_framework',
    'django_filters',
    'drf_spectacular',

    # AlpenWegs applications:
    'notifications.apps.NotificationsConfig',
    'profiles.apps.ProfilesConfig',
]

# Middleware configuration:
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Main URL file:
ROOT_URLCONF = 'alpenwegs.urls'

# Templates configuration:
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# WSGI and ASGI configuration:
WSGI_APPLICATION = 'alpenwegs.wsgi.application'
ASGI_APPLICATION = 'alpenwegs.asgi.application'

# Celery configuration:
CELERY_BROKER_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}'
CELERY_RESULT_BACKEND = f'redis://{REDIS_HOST}:{REDIS_PORT}'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
CELERY_IGNORE_RESULT = True

# Channel configuration:
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [f'redis://{REDIS_HOST}:{REDIS_PORT}'],
        },
    },
}

# Rest framework configuration:
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'alpenwegs.ashared.api.base_exception_handler.custom_exception_handler',
    'DEFAULT_PAGINATION_CLASS': 'alpenwegs.ashared.api.base_pagination.BasePaginator',
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissions',
    ],
}

# Schema configuration:
SPECTACULAR_SETTINGS = {
    'TITLE': 'AlpenWegs REST API',
    'LICENSE': {'name': 'Apache v2 License'},
    'VERSION': VERSION,
    'COMPONENT_SPLIT_REQUEST': True,
    'SERVE_PERMISSIONS': ['rest_framework.permissions.AllowAny'],
    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
        'persistAuthorization': True,
        'displayOperationId': True,
        'defaultModelsExpandDepth': 1,
        'defaultModelExpandDepth': 3,
        'docExpansion': 'none',
    },
}

# Database configuration:
if DB_TYPE == 'sqlite3':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
elif DB_TYPE == 'postgresql':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': DB_NAME,
            'USER': DB_USER,
            'PASSWORD': DB_PASS,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
        }
    }

# Password validation:
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Logger configuration:
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {'format': '[%(levelname)s] %(asctime)s %(name)s: %(message)s'},
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'ERROR',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False
        },
        'django.server': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False
        },
    },
}

# Internationalization:
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Language configuration:
LANGUAGE_CODE = 'en-us'
LANGUAGES = [
    ('en', 'English')
]
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

# Internationalization:
USE_I18N = True
USE_TZ = True

# Static files configuration:
STATIC_URL = '/assets/static/'
STATICFILES_DIRS = [
    BASE_DIR.joinpath('assets/static'),
    BASE_DIR.joinpath('assets/media'),
]
STATIC_ROOT = BASE_DIR.joinpath('staticfiles')
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
]

# Default primary key field type:
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Jazzmin configuration:
JAZZMIN_SETTINGS = GLOBAL_JAZZMIN_SETTINGS
JAZZMIN_UI_TWEAKS = {
    'theme': 'litera',
    'body_small_text': True,
    'brand_colour': 'navbar-light',
    'sidebar': 'sidebar-light-primary',
    'theme_color': 'indigo',
    'sidebar_nav_flat_style': True
}

# Default primary key field type:
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Default user model:
AUTH_USER_MODEL = 'profiles.MemberModel'
