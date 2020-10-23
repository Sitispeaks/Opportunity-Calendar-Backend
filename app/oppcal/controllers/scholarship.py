from django.conf import settings
from oppcal.managers.scholarship import ScholarshipManager
from rest_framework.response import Response
from rest_framework.views import APIView


class ScholarshipCreateController(APIView):
    def post(self, request):
        data = request.data
        manager = ScholarshipManager()
        Scholarship = manager.create_scholarship(
            data["title"],
            data["url"],
            data["date"],
            data["description"],
            data["eligibility"],
            data["deadline"],
        )
        return Response(Scholarship)


class ScholarshipListController(APIView):
    def get(self, request):
        manager = ScholarshipManager()
        scholarship_list = manager.get_scholarships()
        return Response(scholarship_list)


class ScholarshipPatchController(APIView):
    def patch(self, request, scholarship_id):
        return Response({"detail": "Patch"}, status=200)


class ScholarshipDeleteController(APIView):
    def delete(self, request, scholarship_id):
        return Response({"detail : deleted"}, status=200)

