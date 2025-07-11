from rest_framework.routers import DefaultRouter
from django import views
from django.urls import include, path

from . import views
from .views import feedback_list, FeedbackViewSet
from job_record import views as job_views


router = DefaultRouter()
router.register(r'feedbacks', FeedbackViewSet, basename='feedback')


urlpatterns = [
    path('job/<str:job_title>/', feedback_list, name='feedback-list'),
    path('job/<str:job_title>/add/', views.add_feedback, name='add-feedback'),
    path('jobs/', job_views.jobs_record, name='job-list'),
    
    path('', include(router.urls)), 
]