from mydj.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True    # Temporarily set to True to enable debug mode

# INSTALLED_APPS = []

ALLOWED_HOSTS = ["elns.ir", "www.elns.ir"]

# site framework
SITE_ID = 2

# CSRF_COOKIE_SECURE = True

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_ROOT = "/home/elnsir/public_html/static"
MEDIA_ROOT = "/home/elnsir/public_html/media"

SECURE_BROWSER_XSS_FILTER = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = "SAMEORIGIN"
