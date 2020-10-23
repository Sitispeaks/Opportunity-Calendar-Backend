from django.urls import path
from oppcal.controllers.conference import (
    ConferenceCreateController,
    ConferenceListController,
)

app_name = "oppcal"

urlpatterns = [
    path("create/", ConferenceCreateController.as_view(), name="conference_create"),
    path("list/", ConferenceListController.as_view(), name="conference_list"),
]
