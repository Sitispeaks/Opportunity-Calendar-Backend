from django.urls import path

from app.oppcal.controllers.intern import InternCreateController

app_name = "oppcal"

urlpatterns = [path("create", InternCreateController.as_view(), name="intern_create")]

