from django import views
from django.urls import include, path
from . import views
from job_record import views as job_views
from .views import feedback_list
from rest_framework.routers import DefaultRouter
from .views import FeedbackViewSet


router = DefaultRouter()
router.register(r'feedbacks', FeedbackViewSet, basename='feedback')


urlpatterns = [
    path('', include(router.urls)), 

]