from django.urls import path
from oppcal.controllers.competition import (
    CompetitionCreateController,
    CompetitionListController,
)

app_name = "oppcal"

urlpatterns = [
    path("create/", CompetitionCreateController.as_view(), name="competition_create"),
    path("list/", CompetitionListController.as_view(), name="competition_list"),
]
