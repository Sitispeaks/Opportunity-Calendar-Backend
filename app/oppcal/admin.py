from django.contrib import admin

# Register your models here.
from .models import competition, conference, hackathon, intern, job, scholarship

admin.site.register(intern.Intern)
admin.site.register(job.Job)
admin.site.register(competition.Competition)
admin.site.register(hackathon.Hackathon)
admin.site.register(scholarship.Scholarship)
admin.site.register(conference.Conference)
