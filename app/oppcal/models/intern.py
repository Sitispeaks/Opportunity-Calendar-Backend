from django.contrib.postgres import fields
from django.db import models


class Intern(models.Model):
    jobId = models.CharField(max_length=200)
    jobURL = models.CharField(max_length=300,blank=False)
    title = models.CharField(max_length=200,blank=False)
    company = models.CharField(max_length=200,blank=False)
    JobDescription = models.CharField(max_length=4000)
    location = models.CharField(max_length=200)
    eligibility = models.CharField(max_length=2000)
    deadline = models.DateField()

    class Meta:
        db_table = "interns"
