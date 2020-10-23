from django.urls import path

from oppcal.models.scholarship import Scholarship
from oppcal.models.serializers.scholarship import ScholarshipSerializer

from rest_framework.response import Response
from rest_framework.exceptions import APIException


class ScholarshipManager:
    @staticmethod
    def create_scholarship(
        title, url, date, description, eligibility, deadline
    ):
        serializer = ScholarshipSerializer(
            data={
                "title": title,
                "url": url,
                "date": date,
                "description": description,
                "eligibility": eligibility,
                "deadline": deadline,
            }
        )
        if serializer.is_valid():
            serializer.save()
            return serializer.data

        raise APIException(serializer.errors, "New Scholarship could not be created")

    @staticmethod
    def get_scholarships():
        queryset = Scholarship.objects.all()
        serializer = ScholarshipSerializer(queryset, many=True)
        return serializer.data
