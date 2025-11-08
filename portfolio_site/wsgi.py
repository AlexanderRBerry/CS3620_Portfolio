"""
WSGI config for portfolio_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
print("WSGI starting…", file=sys.stderr)
print("DATABASE_URL:", os.environ.get("DATABASE_URL"), file=sys.stderr)
print("ALLOWED_HOSTS:", os.environ.get("ALLOWED_HOSTS"), file=sys.stderr)
application = get_wsgi_application()
