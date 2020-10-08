from django.contrib.postgres import fields
from django.db import models


class Hackathon(models.Model):
    title = models.CharField(max_length=200,blank=False)
    url = models.CharField(max_length=300,blank=False)
    date = models.DateField(blank=False)
    description = models.CharField(max_length=4000)
    location = models.CharField(max_length=200)
    eligibility = models.CharField(max_length=2000)
    deadline = models.DateField()

    class Meta:
        db_table = "hackathons"
