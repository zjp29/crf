from django.contrib.gis import admin
from django.apps import apps
from .models import *

admin.site.register(NwicCcdCrf,admin.GeoModelAdmin)

