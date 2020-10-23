from django.urls import path
from oppcal.controllers.hackathon import (
    HackathonCreateController,
    HackathonListController,
)

app_name = "oppcal"

urlpatterns = [
    path("create/", HackathonCreateController.as_view(), name="hackathon_create"),
    path("list/", HackathonListController.as_view(), name="hackathon_list"),
]
