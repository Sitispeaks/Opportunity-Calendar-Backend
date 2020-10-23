from django.conf import settings
from oppcal.managers.competition import CompetitionManager
from rest_framework.response import Response
from rest_framework.views import APIView


class CompetitionCreateController(APIView):
    def post(self, request):
        data = request.data
        manager = CompetitionManager()
        competition = manager.create_competition(
            data["title"],
            data["url"],
            data["date"],
            data["description"],
            data["location"],
            data["eligibility"],
            data["deadline"],
        )
        return Response(competition)


class CompetitionListController(APIView):
    def get(self, request):
        manager = CompetitionManager()
        competition_list = manager.get_competitions()
        return Response(competition_list)


class CompetitionPatchController(APIView):
    def patch(self, request, competition_id):
        return Response({"detail": "Patch"}, status=200)


class CompetitionDeleteController(APIView):
    def delete(self, request, competition_id):
        return Response({"detail : deleted"}, status=200)

