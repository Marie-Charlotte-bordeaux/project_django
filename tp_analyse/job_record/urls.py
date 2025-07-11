from django.contrib import admin
from django.urls import include, path
from .views import job_detail, jobs_record, JobRecordViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'jobs', JobRecordViewSet, basename='jobrecord')

urlpatterns = [
    path('',jobs_record, name='home'),
    # path('<int:job_id>/', job_detail, name='job-detail'),  # détail job front

]
urlpatterns += router.urls
