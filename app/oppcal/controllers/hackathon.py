from django.conf import settings
from oppcal.managers.hackathon import HackathonManager
from rest_framework.response import Response
from rest_framework.views import APIView


class HackathonCreateController(APIView):
    def post(self, request):
        data = request.data
        manager = HackathonManager()
        Hackathon = manager.create_hackathon(
            data["title"],
            data["url"],
            data["date"],
            data["description"],
            data["location"],
            data["eligibility"],
            data["deadline"],
        )
        return Response(Hackathon)


class HackathonListController(APIView):
    def get(self, request):
        manager = HackathonManager()
        hackathon_list = manager.get_hackathons()
        return Response(hackathon_list)


class HackathonPatchController(APIView):
    def patch(self, request, hackathon_id):
        return Response({"detail": "Patch"}, status=200)


class HackathonDeleteController(APIView):
    def delete(self, request, hackathon_id):
        return Response({"detail : deleted"}, status=200)

