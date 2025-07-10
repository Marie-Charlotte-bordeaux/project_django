from django.contrib import admin
from django.urls import include, path
from .views import job_detail, jobs_record
from rest_framework.routers import DefaultRouter
from .views import JobRecordViewSet

router = DefaultRouter()
router.register(r'jobrecord', JobRecordViewSet, basename='jobrecord')

urlpatterns = [
    path('', include(router.urls)), 
]
