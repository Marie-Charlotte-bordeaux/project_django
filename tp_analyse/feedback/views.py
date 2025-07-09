from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Feedback
from job_record.models import JobRecord

def feedback_list(request, job_id):
    job = get_object_or_404(JobRecord, id=job_id)

    feedbacks = job.feedbacks.all() # type: ignore
    feedbacks = feedbacks.order_by('-rating', '-created_at')
    min_rating = request.GET.get('min_rating')
    filter_value = None

    if min_rating:
        try:
            filter_value  = int(min_rating)
            feedbacks = feedbacks.filter(rating__gte=filter_value)
        except ValueError:
            filter_value = None 

    context = {
        'job': job,
        'feedbacks': feedbacks,
        'min_rating': min_rating ,
    }

    return render(request, 'feedback/feedback_list.html', context)