from django.urls import path
from oppcal.controllers.intern import (
    InternCreateController,
    InternDeleteController,
    InternListController,
    InternPatchController,
)

app_name = "oppcal"

urlpatterns = [
    path("create/", InternCreateController.as_view(), name="intern_create"),
    path("list/", InternListController.as_view(), name="intern_list"),
    path("patch/", InternPatchController.as_view(),name="intern_patch"),
    path("delete/", InternDeleteController.as_view(),name="intern_delete")
]
