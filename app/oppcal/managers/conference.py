from django.urls import path

from oppcal.models.conference import Conference
from oppcal.models.serializers.conference import ConferenceSerializer

from rest_framework.response import Response
from rest_framework.exceptions import APIException


class ConferenceManager:
    @staticmethod
    def create_conference(
        title, url, date, description, location, eligibility, deadline
    ):
        serializer = ConferenceSerializer(
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

        raise APIException(serializer.errors, "New Conference could not be created")

    @staticmethod
    def get_conferences():
        queryset = Conference.objects.all()
        serializer = ConferenceSerializer(queryset, many=True)
        return serializer.data
