from django.urls import path
from django.contrib import admin
from django.conf.urls import include

# Use include() to add paths from the catalog application

urlpatterns = [
    path('admin/', admin.site.urls),
]

