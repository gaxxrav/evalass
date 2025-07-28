"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
>>>>>>> a4ab7fa (Project commit)
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
=======
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
>>>>>>> a4ab7fa (Project commit)

application = get_wsgi_application()
