SECRET_KEY = 'django-insecure-oz&!3thv+3-j%*scw^%33=!&fovpaakcl_s_!!-uzq1depa#xq'
ADMIN_SITE_URL = 'root'

# ------------------------------------------------
#
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
