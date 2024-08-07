"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from decouple import config, Csv # https://github.com/henriquebastos/python-decouple
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='django-insecure-=(75y8@$ql#q+rio914mn%3g0h!j!fhksrsfv==)mpd%21$ge8')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=Csv())


# Application definition

INSTALLED_APPS = [
    # ===[Default Django Apps]===
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # ======[External Apps]======
    'django_cas_ng',
    'hijack.contrib.admin',
    'hijack',
    'crispy_forms',
    'crispy_bootstrap4',
    # =======[My Own Apps]=======
    'apps.services',
    'apps.landingpage',
    'apps.authentication',
    'apps.adminpage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django_cas_ng.middleware.CASMiddleware',
    'hijack.middleware.HijackUserMiddleware',
]


ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'apps.services.context_processors.global_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
       'ENGINE'     : config('DB_ENGINE',   default='django.db.backends.postgresql'),
       'NAME'       : config('DB_NAME',     default='YOUR_DB_NAME'),
       'USER'       : config('DB_USER',     default='YOUR_DB_USER'),
       'PASSWORD'   : config('DB_PASSWORD', default='YOUR_DB_PASSWORD'),
       'HOST'       : config('DB_HOST',     default='127.0.0.1'),
       'PORT'       : config('DB_PORT',     default='5432', cast=int),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.AllowAllUsersModelBackend', # If activated at login is_active is checked manually not to be one in authenticate() function
    'django.contrib.auth.backends.ModelBackend', # For django cas
    # 'django_cas_ng.backends.CASBackend', # Default django cas backend
    'apps.services.djangocas.CustomCASBackend', # Custom django cas backend
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

if DEBUG:
    STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static') ]
else:
    STATIC_ROOT = os.path.join(BASE_DIR,'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'





# =====================================================================================================
#                                           EXTENDS SETTINGS
# =====================================================================================================

# =======[App Info]======
APP_SHORT_NAME          = 'Helpdesk'
APP_FULL_NAME           = 'Helpdesk BPSDM UMS'
APP_VERSION             = 'v1.0'
APP_YEAR                = '2023'
APP_DEVELOPER           = 'BTI'
APP_COMPANY_SHORT_NAME  = 'UMS'
APP_COMPANY_FULL_NAME   = 'BPSDM UMS'
APP_LOGO                = os.path.join(STATIC_URL,'images/logo/ums_logo_color.svg')
APP_FAVICON             = os.path.join(STATIC_URL,'images/logo/ums_logo_favicon.ico')
APP_BASE_URL            = config('APP_BASE_URL', default='') # for email verify



# =====[Media Files]=====
MEDIA_ROOT              = os.path.join(BASE_DIR,'media')
MEDIA_URL               = '/media/'


# ======[Login URL]======
LOGIN_URL               = 'authentication:signin'
LOGIN_REDIRECT_URL      = 'authentication:signin'


# ========[CSRF]=======
CSRF_TRUSTED_ORIGINS = [
    "https://*.ums.ac.id",
]


# ======[Django Cas]=====
CAS_SERVER_URL          = 'https://auth.ums.ac.id/cas/'
CAS_ADMIN_PREFIX        = 'admin' # Set to -> '/admin' if you want to login to the admin using cas
CAS_CREATE_USER         = True
CAS_LOGIN_MSG           = 'Login succeeded. Welcome, %s.'
CAS_LOGGED_MSG          = 'You are logged in as %s.'
CAS_LOGIN_URL_NAME      = 'authentication:cas_ng_login'
CAS_LOGOUT_URL_NAME     = 'authentication:cas_ng_logout'
CAS_LOGOUT_COMPLETELY   = True
CAS_IGNORE_REFERER      = True
CAS_REDIRECT_URL        = '/authentication/signin' # The default is '/'
CAS_VERSION             = '2'


# =====[API GATEWAY]=====
# It is used to sync cas login data with Sihrd API (apps.services.utils.profilesync)
# if you don't have an apigateway account, please create an account at https://api.ums.ac.id/admin/
API_GATEWAY_URL         = config('API_GATEWAY_URL',      default='https://api.ums.ac.id/') # or -> http://172.16.10.241:8008/
API_GATEWAY_USERNAME    = config('API_GATEWAY_USERNAME', default='YOUR_APIGATEWAY_USERNAME')
API_GATEWAY_PASSWORD    = config('API_GATEWAY_PASSWORD', default='YOUR_APIGATEWAY_PASSWORD')


# =======[API STAR]======
# this is only optional if you don't use apistar it can be ignored
API_STAR_URL            = config('API_STAR_URL',        default='https://star.ums.ac.id/abubakar/') # set it to -> '' if you don't use this
API_STAR_USERNAME       = config('API_STAR_USERNAME',   default='YOUR_APISTAR_USERNAME')
API_STAR_PASSWORD       = config('API_STAR_PASSWORD',   default='YOUR_APISTAR_PASSWORD')


# ========[EMAIL]========
EMAIL_VERIFICATION      = False # If set to true, the user needs to verify email during registration (Fill in the data below if set to true)
EMAIL_BACKEND           = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER         = config('EMAIL_HOST_USER',     default='YOUR_EMAIL@GOOGLE.COM')
EMAIL_HOST_PASSWORD     = config('EMAIL_HOST_PASSWORD', default='YOUR_PASSWORD')
EMAIL_HOST              = 'smtp.gmail.com'
EMAIL_PORT              = 587
EMAIL_USE_TLS           = True


# ========[WABLAS]=======
WABLAS_URL              = config('WABLAS_URL',          default='https://eu.wablas.com')
WABLAS_TOKEN            = config('WABLAS_TOKEN',        default='YOUR_TOKEN')


# ========[CRISPY]=======
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"