from django.db import models 
from rest_framework import serializers
from oppcal.models.competition import Competition

class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model:Competition
        fields:['title','url','date','description','location','eligibility','deadline']
