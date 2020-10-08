from django.db import models 
from rest_framework import serializers
from oppcal.models.scholarship import Scholarship

class ScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model:Scholarship
        fields:['title','url','description','eligibility','deadline']
