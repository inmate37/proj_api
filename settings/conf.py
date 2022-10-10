# Local
from . import get_env_variable

SECRET_KEY = get_env_variable('SECRET_KEY')
ADMIN_SITE_URL = 'root'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = get_env_variable('EMAIL_HOST')
EMAIL_HOST_USER = get_env_variable('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = get_env_variable('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

SHELL_PLUS_PRE_IMPORTS = [
    (
        'django.db',
        (
            'connection',
            'reset_queries',
            'connections',
        ),
    ),
    (
        'django.db.models',
        (
            'FloatField',
            'IntegerField',
        ),
    ),
    (
        'datetime',
        (
            'datetime',
            'timedelta',
            'date',
        ),
    ),
    (
        'json',
        (
            'loads',
            'dumps',
        ),
    ),
]
SHELL_PLUS_MODEL_ALIASES = {
    'auths': {
        'CustomUser': 'U',
    },
}
SHELL_PLUS = 'ipython'
SHELL_PLUS_PRINT_SQL = False
SHELL_PLUS_PRINT_SQL_TRUNCATE = 1000

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': (
        'rest_framework.pagination.PageNumberPagination',
    ),
    'PAGE_SIZE': 10
}
