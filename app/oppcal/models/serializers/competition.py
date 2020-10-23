from django.db import models
from oppcal.models.competition import Competition
from rest_framework import serializers


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = "__all__"
