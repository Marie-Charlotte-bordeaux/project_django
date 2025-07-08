from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Avg, Count
from .models import JobRecord

# Create your views here.
def jobs_record(request):
    # Exemple de stats (à adapter à ton besoin réel)
    total_jobs = JobRecord.objects.count()
    average_salary = JobRecord.objects.aggregate(Avg('salary_in_usd'))['salary_in_usd__avg']
    countries_count = JobRecord.objects.values('company_location').distinct().count()

    return render(request, 'jobs/jobs.html', {
        'total_jobs': total_jobs,
        'average_salary': round(average_salary or 0, 2),
        'countries_count': countries_count
    })