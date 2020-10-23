from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from oppcal.managers.job import JobManager
from rest_framework import status


class JobCreateController(APIView):
    def post(self, request):
        data = request.data
        manager = JobManager()
        job = manager.create_job(
            data["jobId"],
            data["jobURL"],
            data["title"],
            data["company"],
            data["jobDescription"],
            data["location"],
            data["eligibility"],
            data["deadline"],
        )
        return Response(job)


class JobListController(APIView):
    def get(self, request):
        manager = JobManager()
        job_list = manager.get_jobs()
        return Response(job_list)


class JobPatchController(APIView):
    def patch(self, request, job_id):
        return Response({"detail": "Patch"}, status=200)


class JobDeleteController(APIView):
    def delete(self, request, job_id):
        return Response({"detail : deleted"}, status=200)

