from django import views
from django.urls import path
from . import views
from .views import feedback_list
from job_record import views as job_views


urlpatterns = [
    path('job/<int:job_id>/', feedback_list, name='feedback-list'),
    path('job/<int:job_id>/add/', views.add_feedback, name='add-feedback'),
    path('jobs/', job_views.jobs_record, name='job-list'),

]