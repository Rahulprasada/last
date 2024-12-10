#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
from django.core.wsgi import get_wsgi_application
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproj.settings')

# This checks if the app is running in the Vercel environment
if os.environ.get('VERCEL'):
    # Use get_asgi_application() or get_wsgi_application() based on Vercel's requirements
    from myapp import application  # Assuming your app provides an ASGI or WSGI callable
    handler = application  # Set the application callable for Vercel
else:
    application = get_wsgi_application() 
