from django.contrib.gis import admin

from leaflet.admin import LeafletGeoAdmin
from .models import Area


admin.site.register(Area, LeafletGeoAdmin)