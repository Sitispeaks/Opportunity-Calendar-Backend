from django.db import models 
from rest_framework import serializers
from oppcal.models.conference import Conference

class ConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = '__all__'
