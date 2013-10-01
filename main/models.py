
from django.contrib.gis.db  import models as gismodels


class Area(gismodels.Model):

    AREA_TYPES = (
        ('R', 'Residental'),
        ('N', 'Neighbourhood'),
        ('G', 'Geographic'),
    )

    name = gismodels.CharField(max_length=100)
    area_type = gismodels.CharField(max_length=2, choices=AREA_TYPES)

    geom = gismodels.MultiPolygonField(spatial_index=True)

    objects = gismodels.GeoManager()

    def __unicode__(self):
        return self.name