import os
import json
with open('/home/dotcloud/environment.json') as f:
    env = json.load(f)

PROJECTROOT = os.path.dirname(os.path.abspath(__file__))
DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'iblog',
        'USER': env['DOTCLOUD_DB_SQL_LOGIN'],
        'PASSWORD': env['DOTCLOUD_DB_SQL_PASSWORD'],
        'HOST': env['DOTCLOUD_DB_SQL_HOST'],
        'PORT': int(env['DOTCLOUD_DB_SQL_PORT']),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'iblog',
#         'USER': 'blog',
#         'PASSWORD': 'squarenix',
#         'HOST': '10.211.55.4',
#         'PORT': '5432',
#     }
# }

SECRET_KEY = 'e&amp;pot@9lf(x3@)pgxvx+lzql=(gzubifprdw*vd4lyby0yq$05'

MEDIA_ROOT = '/home/dotcloud/data/media/'
STATIC_ROOT = '/home/dotcloud/volatile/static/'

# MEDIA_ROOT = '%s/upload' % PROJECTROOT
# STATIC_ROOT = '%s/assets' % PROJECTROOT

STATICFILES_DIRS = (
    os.path.join(PROJECTROOT, "static/"),
)

TEMPLATE_DIRS = (
    os.path.join(PROJECTROOT, "templates/"),
)

MEDIA_URL = '/media/'
STATIC_URL = '/static/'
GA_CODE = 'UA-20886379-1'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'log_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': '/var/log/supervisor/iblog.log',
            'maxBytes': 1024*1024*25, # 25 MB
            'backupCount': 5,
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'log_file', 'mail_admins'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console', 'log_file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console', 'log_file', 'mail_admins'],
            'level': 'INFO',
            'propagate': False,
        },
        # Catch All Logger -- Captures any other logging
        '': {
            'handlers': ['console', 'log_file', 'mail_admins'],
            'level': 'INFO',
            'propagate': True,
        }
    }
}
