from django.urls import path

from oppcal.models.competition import Competition
from oppcal.models.serializers.competition import CompetitionSerializer

from rest_framework.response import Response
from rest_framework.exceptions import APIException


class CompetitionManager:
    @staticmethod
    def create_competition(
        title, url, date, description, location, eligibility, deadline
    ):
        serializer = CompetitionSerializer(
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

        raise APIException(serializer.errors, "New Competition could not be created")

    @staticmethod
    def get_competitions():
        queryset = Competition.objects.all()
        serializer = CompetitionSerializer(queryset, many=True)
        return serializer.data
