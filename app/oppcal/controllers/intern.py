from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView

from ..utils.pagination import get_pagination_info


class InternCreateController(APIView):
    return Response({"detail": "Created"}, status=200)


class InternListController(APIView):
    pass


class InternPatchController(APIView):
    pass


class InternDeleteController(APIView):
    pass

