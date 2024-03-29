"""
Django settings for ecomprj project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

from os import getenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)akqpplpp@!!slxnmdm%a+%izno!a%ue53fge*i6ixh^=k512v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv("IS_DEVELOPMENT", True)

ALLOWED_HOSTS = [
    "127.0.0.1",
    ".vercel.app",
    "ecommerce-theta-steel.vercel.app",
    ]


# Application definition

INSTALLED_APPS = [
    # `'jazzmin',` is adding the Jazzmin package to the list of installed apps in the Django project.
    # Jazzmin is a customizable Django admin theme that provides a modern and responsive user
    # interface for the Django admin site. By adding `'jazzmin',` to the `INSTALLED_APPS` list, the
    # Jazzmin package will be included in the project and can be used to customize the admin
    # interface.
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #Custom Apps
    'core',
    'userauths',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecomprj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates"
            ],
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

WSGI_APPLICATION = 'ecomprj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'URL': 'postgresql://postgres:2g2D3De1E3bFDA53*GEd*DEdA2-dc61d@viaduct.proxy.rlwy.net:39177/railway',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': '2g2D3De1E3bFDA53*GEd*DEdA2-dc61d',
        'HOST': 'viaduct.proxy.rlwy.net',
        'PORT': '39177'
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = 'static/'



STATICFILES_DIRS = [
    BASE_DIR / 'static'
]


MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = '/media/'



# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


JAZZMIN_SETTINGS = {
    'site_header' : "Fast Food",
    'site_brand' : "Make Your Orders Now!",
    'site_logo' : "/images/favicon.png",
    'copyright' : "fast-food.com",
}

AUTH_USER_MODEL = 'userauths.User'