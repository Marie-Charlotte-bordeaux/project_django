from django.contrib import admin
from django.urls import path
from .views import job_detail, jobs_record


urlpatterns = [
    path('',jobs_record, name='home'),
    # path('<int:job_id>/', job_detail, name='job-detail'),  # détail job front

]
