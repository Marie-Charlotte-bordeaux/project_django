from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Feedback
from job_record.models import JobRecord

def feedback_list(request, job_id):
    min_rating = request.GET.get('min_rating')
    job = get_object_or_404(JobRecord, id=job_id)

    feedbacks = job.feedbacks.all() # type: ignore
    
    if min_rating:
        try:
            min_rating = int(min_rating)
            feedbacks = feedbacks.filter(rating__gte=min_rating)
        except ValueError:
            return JsonResponse({"error": "min_rating must be an integer."}, status=400)

    data = [
        {
            "id": f.id,
            "author": f.author_name.name,
            "rating": f.rating,
            "comment": f.comment,
            "created_at": f.created_at.strftime("%Y-%m-%d %H:%M"),
        }
        for f in feedbacks
    ]

    return render(request, 'feedback/feedback_list.html', {
          'job': job,
          'feedbacks': feedbacks
      })