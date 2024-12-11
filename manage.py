import os
from django.core.wsgi import get_wsgi_application # type: ignore

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '.settings')

# This checks if the app is running in the Vercel environment
if os.environ.get('VERCEL'):
    # Use get_asgi_application() or get_wsgi_application() based on Vercel's requirements
    from Miststreet import application  # Assuming your app provides an ASGI or WSGI callable
    handler = application  # Set the application callable for Vercel
else:
    application = get_wsgi_application()  # For local or other environments, use the default WSGI application
