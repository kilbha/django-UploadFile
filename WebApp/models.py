from django.db import models

# Create your models here.
class StdModel(models.Model):
    StdNo = models.IntegerField()
    StdName = models.CharField(max_length = 300)
    StdPic = models.FileField(blank=True,null=True)
    stdAds = models.CharField(max_length = 300)