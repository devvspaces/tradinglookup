from django.contrib import admin
from django.urls import path

from mainapp.views import search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', search, name='search'),
]
