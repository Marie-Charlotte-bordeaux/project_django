from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Avg, Count

from .serializers import JobRecordSerializer
from .models import JobRecord
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

# Create your views here.
def jobs_record(request):
    # Exemple de stats (à adapter à ton besoin réel)
    total_jobs = JobRecord.objects.count()
    average_salary = JobRecord.objects.aggregate(Avg('salary_in_usd'))['salary_in_usd__avg']
    countries_count = JobRecord.objects.values('company_location').distinct().count()
    jobs = JobRecord.objects.all()
    # ➜ Chaque job aura un attribut `avg_rating` note moeynne
    jobs = JobRecord.objects.annotate(avg_rating=Avg('feedbacks__rating'))
    return render(request, 'jobs/jobs.html', {
        'total_jobs': total_jobs,
        'average_salary': round(average_salary or 0, 2),
        'countries_count': countries_count,
        'jobs': jobs
    })

def job_detail(request, job_id):
    job = get_object_or_404(JobRecord, pk=job_id)
    return render(request, 'job_record/job_detail.html', {'job': job})

# une vue API REST (JobRecordViewSet) pour tes requêtes JSON.
class JobRecordViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]   
    queryset = JobRecord.objects.all()
    serializer_class = JobRecordSerializer