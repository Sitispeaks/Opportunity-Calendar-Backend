from django.db import models
from oppcal.models.hackathon import Hackathon
from rest_framework import serializers


class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = "__all__"
