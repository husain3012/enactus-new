"""
WSGI config for EnSite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os, sys

# add the hellodjango project path into the sys.path
sys.path.append('app engine:/')

# add the virtualenv site-packages path to the sys.path
sys.path.append('app engine:/env/Lib/site-packages')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EnSite.settings')

from django.core.wsgi import get_wsgi_application


application = get_wsgi_application()
