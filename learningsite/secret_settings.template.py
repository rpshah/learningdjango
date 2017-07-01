# make sure a file named secret_settings.py exist as below

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'secret-hash'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbname',
        'USER': 'uername',
        'PASSWORD': 'secret-password',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}