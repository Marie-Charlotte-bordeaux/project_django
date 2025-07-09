from django.urls import path
from .views import feedback_list

urlpatterns = [
    path('job/<int:job_id>/', feedback_list, name='feedback-list'),
]