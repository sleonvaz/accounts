
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '2pxs-u#yka15spn#yg943y$9onvhr4q4d=-$ck92*(65u_3mg!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


####################################################################################################
#                                         APPLICATIONS                                             #
####################################################################################################
PROJECT_APPS = [
    'applications.core',
    'applications.clients',
    'social_django',
]
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] + PROJECT_APPS

####################################################################################################
#                                         MIDDLEWARE                                               #
####################################################################################################

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

####################################################################################################
#                                         AUTHENTICATION_BACKENDS                                  #
####################################################################################################

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

####################################################################################################
#                                         GOOGLE SOCIAL CONFIGURATION                              #
####################################################################################################

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '671554445159-383ul1too3hfljf04au2hv3ii8cusknk.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'pe-fZ2N9SLvb05Ne1F8i7cVK'

SOCIAL_AUTH_URL_NAMESPACE = 'social'

LOGIN_URL = '/auth/login/google-oauth2/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

####################################################################################################
#                                           URL_CONF                                               #
####################################################################################################

ROOT_URLCONF = 'accounts_administrator.urls'


####################################################################################################
#                                          TEMPLATING                                              #
####################################################################################################

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

####################################################################################################
#                                           WSGI_PATH                                              #
####################################################################################################

WSGI_APPLICATION = 'accounts_administrator.wsgi.application'


####################################################################################################
#                                        DATABASE_CONFIG                                           #
####################################################################################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST':os.environ.get('DB_HOST'),
        'NAME':os.environ.get('DB_NAME'),
        'USER':os.environ.get('DB_USER'),
        'PASSWORD':os.environ.get('DB_PASS'),
    }
}


####################################################################################################
#                                     PASSWORD VALIDATIONS                                         #
####################################################################################################

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


####################################################################################################
#                                       INTERNACIONALIZATION                                       #
####################################################################################################

LANGUAGE_CODE = 'en-us'

TIME_ZONE = os.environ.get('TZ')

USE_I18N = True

USE_L10N = True

USE_TZ = True


####################################################################################################
#                                            STATIC_FILES                                          #
####################################################################################################

STATIC_URL = '/static/'
