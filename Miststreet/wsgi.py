"""
WSGI config for myproj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application # type: ignore

# Set the default settings module for the 'django' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Miststreet.settings')

# Get the WSGI application
application = get_wsgi_application()

# Vercel might specifically need this
app = application
