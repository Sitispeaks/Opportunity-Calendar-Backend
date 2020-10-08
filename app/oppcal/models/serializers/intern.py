from django.db import models 
from rest_framework import serializers
from oppcal.models.intern import Intern

class InternSerializer(serializers.ModelSerializer):
    class Meta:
        model:Intern
        fields:['jobId','jobURL','title','company','jobDescription','location','eligibility','deadline']
