from django.db import models
from oppcal.models.intern import Intern
from rest_framework import serializers


class InternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intern
        fields = "__all__"

