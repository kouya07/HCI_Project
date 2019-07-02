"""
WSGI config for test1 project.

It exposes the WSGI callable as round_array module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test1.settings")

application = get_wsgi_application()