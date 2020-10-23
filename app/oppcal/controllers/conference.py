from django.conf import settings
from oppcal.managers.conference import ConferenceManager
from rest_framework.response import Response
from rest_framework.views import APIView


class ConferenceCreateController(APIView):
    def post(self, request):
        data = request.data
        manager = ConferenceManager()
        Conference = manager.create_conference(
            data["title"],
            data["url"],
            data["date"],
            data["description"],
            data["location"],
            data["eligibility"],
            data["deadline"],
        )
        return Response(Conference)


class ConferenceListController(APIView):
    def get(self, request):
        manager = ConferenceManager()
        conference_list = manager.get_conferences()
        return Response(conference_list)


class ConferencePatchController(APIView):
    def patch(self, request, conference_id):
        return Response({"detail": "Patch"}, status=200)


class ConferenceDeleteController(APIView):
    def delete(self, request, conference_id):
        return Response({"detail : deleted"}, status=200)

