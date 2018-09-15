import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EC463_mini_project.settings')

application = get_wsgi_application()

