SECRET_KEY = 'django-insecure-oz&!3thv+3-j%*scw^%33=!&fovpaakcl_s_!!-uzq1depa#xq'
ADMIN_SITE_URL = 'root'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'x.public.profile@gmail.com'
EMAIL_HOST_PASSWORD = 'bdwludpqybezusha'
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
