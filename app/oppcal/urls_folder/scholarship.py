from django.urls import path
from oppcal.controllers.scholarship import (
    ScholarshipCreateController,
    ScholarshipListController,
)

app_name = "oppcal"

urlpatterns = [
    path("create/", ScholarshipCreateController.as_view(), name="scholarship_create"),
    path("list/", ScholarshipListController.as_view(), name="scholarship_list"),
]
