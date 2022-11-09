from django.conf import settings
from django_hosts import host, patterns

host_patterns = patterns(
    '',
    # For Production
    host(r'', settings.ROOT_URLCONF, name='main'),
    host(r'academy', 'Academy.urls', name='academy'),
    host(r'mysecurity', 'PersonalSecurity.urls', name='mysecurity'),
    host(r'', settings.ROOT_URLCONF, name='blog'),
    host(r'', settings.ROOT_URLCONF, name='account'),
    host(r'', settings.ROOT_URLCONF, name='api'),


    # For Development
    # host(r'', settings.ROOT_URLCONF, name='main'),
    # host(r'', settings.ROOT_URLCONF, name='academy'),
    # host(r'', settings.ROOT_URLCONF, name='account'),
    # host(r'', settings.ROOT_URLCONF, name='mysecurity'),
    # host(r'', settings.ROOT_URLCONF, name='blog'),
)
