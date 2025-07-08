from django.contrib import admin
from django.urls import path
from .views import jobs_record

urlpatterns = [
    path('',jobs_record, name='home'),
]
