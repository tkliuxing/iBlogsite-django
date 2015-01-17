# -*- coding: utf-8 -*-
# Django settings for iblog project.
import os

PROJECTROOT = os.path.dirname(os.path.abspath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': 'blog',
        'USER': 'blog',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

SITE_NAME = 'iBlog'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECTROOT, "upload/")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECTROOT, "assets/")
#'/home/b/Code/website/iblog/static'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECTROOT, "static/"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django_assets.finders.AssetsFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "iblog.context_processors.site_env",
    "iblog.context_processors.request",
    "iblog.context_processors.google_analytics",
    # 如果你想使用此内容，需要在settings中配置GA_CODE项。
    "iblog.context_processors.tag_manager",
    "iblog.context_processors.show_profile",
)

ROOT_URLCONF = 'iblog.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'iblog.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECTROOT, "templates/"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'django.contrib.flatpages',
    'django.contrib.admindocs',
    'django.contrib.admin',
    'south',
    'less',
    'disqus',
    'django_markdown',
    'universaltag',
    'django_gravatar',
    'django_pygments',
    'iblog.blog',
    'iblog.homepage',
    'iblog.toupiao',
)

AUTH_PROFILE_MODULE = 'homepage.UserProfile'
LOGIN_URL = '/login/'

INSTALLED_APPS += ('django_assets', )
ASSETS_DEBUG = False
ASSETS_URL_EXPIRE = True
SASS_DEBUG_INFO = False

MARKDOWN_EDITOR_SKIN = 'simple'
UNIVERSALTAG_AUTHOR_ATTRS = 'user'

try:
    from local_settings import *
except:
    pass
