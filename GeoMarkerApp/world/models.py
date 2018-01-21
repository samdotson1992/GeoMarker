from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class Letters(models.Model):
    text = models.CharField(max_length=1000)
    lon = models.FloatField()
    lat = models.FloatField()
    point = models.PointField()

'''
    def __str__(self):
        return ' '.join([
                self.text,
                self.lat,
                self.lon,
                self.point

            ])
'''