from django.urls import path

from oppcal.models.intern import Intern
from oppcal.models.serializers.intern import InternSerializer

from rest_framework.response import Response
from rest_framework.exceptions import APIException


class InternManager:
    @staticmethod
    def create_intern(
        jobId, jobURL, title, company, jobDescription, location, eligibility, deadline
    ):
        serializer = InternSerializer(
            data={
                "jobId": jobId,
                "jobURL": jobURL,
                "title": title,
                "company": company,
                "jobDescription": jobDescription,
                "location": location,
                "eligibility": eligibility,
                "deadline": deadline,
            }
        )
        if serializer.is_valid():
            serializer.save()
            return serializer.data

        raise APIException(serializer.errors, "New Intern could not be created")

    @staticmethod
    def get_interns():
        queryset = Intern.objects.all()
        serializer = InternSerializer(queryset, many=True)
        return serializer.data
