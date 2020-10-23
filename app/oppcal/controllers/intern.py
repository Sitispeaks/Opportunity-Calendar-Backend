from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from oppcal.managers.intern import InternManager
from rest_framework import status
from oppcal.models.serializers.intern import InternSerializer

# # Controller me hi sab kuch kar pehle
# class InternCreateController(APIView):
#     def post(self, request):
#         serializer = InternSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class InternCreateController(APIView):
    def post(self, request):
        data = request.data
        manager = InternManager()
        intern = manager.create_intern(
            data["jobId"],
            data["jobURL"],
            data["title"],
            data["company"],
            data["jobDescription"],
            data["location"],
            data["eligibility"],
            data["deadline"],
        )
        return Response(intern)


class InternListController(APIView):
    def get(self, request):
        manager = InternManager()
        intern_list = manager.get_interns()
        return Response(intern_list)


class InternPatchController(APIView):
    def patch(self, request, intern_id):
        return Response({"detail": "Patch"}, status=200)


class InternDeleteController(APIView):
    def delete(self, request, intern_id):
        return Response({"detail : deleted"}, status=200)

