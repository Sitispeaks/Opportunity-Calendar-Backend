from django.urls import path
from oppcal.controllers.job import (
    JobCreateController,
    JobListController,
)

app_name = "oppcal"

urlpatterns = [
    path("create/", JobCreateController.as_view(), name="job_create"),
    path("list/", JobListController.as_view(), name="job_list"),
]
