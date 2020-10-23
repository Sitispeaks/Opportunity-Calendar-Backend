from django.urls import path

from oppcal.models.hackathon import Hackathon
from oppcal.models.serializers.hackathon import HackathonSerializer

from rest_framework.response import Response
from rest_framework.exceptions import APIException


class HackathonManager:
    @staticmethod
    def create_hackathon(
        title, url, date, description, location, eligibility, deadline
    ):
        serializer = HackathonSerializer(
            data={
                "title": title,
                "url": url,
                "date": date,
                "description": description,
                "location": location,
                "eligibility": eligibility,
                "deadline": deadline,
            }
        )
        if serializer.is_valid():
            serializer.save()
            return serializer.data

        raise APIException(serializer.errors, "New Hackathon could not be created")

    @staticmethod
    def get_hackathons():
        queryset = Hackathon.objects.all()
        serializer = HackathonSerializer(queryset, many=True)
        return serializer.data
