from django.db import models 
from rest_framework import serializers
from oppcal.models.job import Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model:Job
        fields:['jobId','jobURL','title','company','jobDescription','location','eligibility','deadline']
