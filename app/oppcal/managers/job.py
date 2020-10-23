from django.urls import path

from oppcal.models.job import Job
from oppcal.models.serializers.job import JobSerializer

from rest_framework.response import Response
from rest_framework.exceptions import APIException


class JobManager:
    @staticmethod
    def create_job(
        jobId, jobURL, title, company, jobDescription, location, eligibility, deadline
    ):
        serializer = JobSerializer(
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

        raise APIException(serializer.errors, "New Job could not be created")

    @staticmethod
    def get_jobs():
        queryset = Job.objects.all()
        serializer = JobSerializer(queryset, many=True)
        return serializer.data
