"""
Django settings for taobaok project.

Generated by 'django-admin startproject' using Django 1.9.13.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3!%i_+y$gv*+ur2m)94l!jexnjd_1g#4%po7pipmrjsnq#ib@c'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tkAPI',
    'rest_framework',
#    'tkAPI.apps.tkAPIConfig'
#    'django.contrib.sites',
    'users',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'taobaok.urls'

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

WSGI_APPLICATION = 'taobaok.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

TBK_PID = 'mm_40512286_19754960_68174640'
AUTH_USER_MODEL = 'users.User'

REST_FRAMEWORK = {
    # 使用Django的标准`django.contrib.auth`权限管理类,
    # 或者为尚未认证的用户，赋予只读权限.
    'DEFAULT_PERMISSION_CLASSES': [
#        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
         'rest_framework.permissions.AllowAny',
    ]
}


# django-user2
# settings
USERS_REGISTRATION_OPEN = True
 
USERS_VERIFY_EMAIL = True
 
USERS_AUTO_LOGIN_ON_ACTIVATION = True
 
USERS_EMAIL_CONFIRMATION_TIMEOUT_DAYS = 3
 
# Specifies minimum length for passwords:
USERS_PASSWORD_MIN_LENGTH = 5
 
# Specifies maximum length for passwords:
USERS_PASSWORD_MAX_LENGTH = None
 
# the complexity validator, checks the password strength
USERS_CHECK_PASSWORD_COMPLEXITY = True
 
USERS_SPAM_PROTECTION = False  # important!
 
 
#  ---------------------------------------------------------
#  Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
 
EMAIL_USE_TLS = False
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = ''
#  ---------------------------------------------------------


