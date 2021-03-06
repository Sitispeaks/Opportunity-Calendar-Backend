from django.urls import path, include

app_name = "oppcal"

urlpatterns = [
    path("intern/", include("oppcal.urls_folder.intern")),
    path("competition/", include("oppcal.urls_folder.competition")),
    path("job/", include("oppcal.urls_folder.job")),
    path("conference/", include("oppcal.urls_folder.conference")),
    path("hackathon/", include("oppcal.urls_folder.hackathon")),
    path("scholarship/", include("oppcal.urls_folder.scholarship")),
]
