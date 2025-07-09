from django import views
from django.urls import path
from . import views
from .views import feedback_list

urlpatterns = [
    path('job/<int:job_id>/', feedback_list, name='feedback-list'),
    path('job/<int:job_id>/add/', views.add_feedback, name='add-feedback'),

]