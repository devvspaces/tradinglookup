from django.contrib import admin

# Register your models here.
from .models import Ticker, Sector, Industry

admin.site.register([Ticker, Sector, Industry])