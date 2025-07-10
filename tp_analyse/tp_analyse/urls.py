"""
URL configuration for tp_analyse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # FRONT
    path('', include('job_record.urls')),       # Front jobs
    path('feedback/', include('feedback.urls')), # Front feedback

    # APIs REST  
    path('api/', include('job_record.api_urls')),      # API jobs
    path('api/', include('feedback.api_urls')),   # API feedbacks
]