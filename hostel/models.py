from django.db import models

class Hostel(models.Model):
    hostel_id = models.IntegerField()
    hostel_score = models.FloatField()
    hostel_name = models.CharField(max_length=50)
    hostel_addrs = models.CharField(max_length=100)
    hostel_review = models.CharField(max_length=255)
