from django.contrib import admin
from django.urls import path, include

from maindb.views import TickerList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', TickerList.as_view(), name='main')
]
