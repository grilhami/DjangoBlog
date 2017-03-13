"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
import os
from unipath import Path

SECRET_KEY = os.environ['BATMAN_IS_BRUCE_WAYNE']

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).ancestor(2)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party libraries
    'pagedown',
    'crispy_forms',
    'mediumeditor',

    # local apps
    'authentication',
    'core',
    'posts',

]

CRISPY_TEMPLATE_PACK = 'bootstrap3'

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (BASE_DIR.child('templates'),),
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
        'default': {
        'ENGINE':'django.db.backends.mysql',
        'OPTIONS':{
            'read_default_file': os.path.join(BASE_DIR, 'dbconf.cnf')
           }
        }
        # 'default': {
        #     'ENGINE':'django.db.backends.postgresql',
        #     'NAME':'trydjango',
        #     'USER':'postgres',
        #     'PASSWORD':'password123',
        #     'HOST':'localhost',
        #     }
    #  'other': {
    #        'ENGINE':'mysql.connector.django',
    #        'NAME':'trydjango',
    #        'USER':'root',
    #        'PASSWORD':'password123',
    #        'HOST':'localhost',
    #        'OPTIONS':{
    #            'autocommit':True
    #            }

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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static")
        #'/var/www/static',
        ]

STATIC_ROOT = BASE_DIR.ancestor(1).child("static_cdn")

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR.ancestor(1).child("media_cdn")


# Theme options `default`, `roman`, `mani`, `flat`, `bootstrap`, `tim`, `beagle`
MEDIUM_EDITOR_THEME = 'beagle' # `default` is defualt theme
MEDIUM_EDITOR_OPTIONS = {
 'toolbar': {
        'static': True,
        'buttons': [
            'bold',
            'italic',
            'underline',
            # 'strikethrough',
            'subscript',
            'superscript',
            'h1',
            'h2',
            'h3',
            'quote',
        ]
    },
    'paste': {
        'imageDragging': True,
        'forcePlainText': True,
        'cleanPastedHTML': False,
        'cleanReplacements': [],
        'cleanAttrs': ['class', 'style', 'dir'],
        'cleanTags': ['meta']
    }

}
