from django.db import models

# Create your models here.

class Hotplace(models.Model):
    place_name = models.CharField(max_length=50, null=False, primary_key=True)
    place_address = models.CharField(max_length=100, null=False)
    phone_num = models.CharField(max_length=20, null=False)
    review_num = models.IntegerField(null=False)
    score_rate = models.FloatField(null=False)



class Sample(models.Model):
    placeName = models.CharField(max_length=50, null=False)
    review_detail = models.CharField(max_length=2000, null=False)
    satisfaction_rate = models.IntegerField(null=False)