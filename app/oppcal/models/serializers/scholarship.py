from django.db import models
from oppcal.models.scholarship import Scholarship
from rest_framework import serializers


class ScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scholarship
        fields = "__all__"
