from django.db import models 
from rest_framework import serializers
from oppcal.models.hackathon import Hackathon

class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model:Hackathon
        fields: '__all__'
