from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Avg
from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from django.urls import reverse

from .forms import FeedbackForm
from .serializers import FeedbackSerializer
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
            feedbacks = feedbacks.filter(rating=filter_value)
        except ValueError:
            filter_value = None 

    context = {
        'job': job,
        'feedbacks': feedbacks,
        'min_rating': min_rating ,
    }

    return render(request, 'feedback/feedback_list.html', context)

def add_feedback(request, job_id):
    job = get_object_or_404(JobRecord, id=job_id)
    feedbacks = job.feedbacks.all() # type: ignore
    average_rating = feedbacks.aggregate(avg=Avg('rating'))['avg']

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.job = job
            feedback.save()
            return redirect(reverse('feedback-list-front', kwargs={'job_id': job.id}))    
    else:
        form = FeedbackForm()

    return render(request, 'feedback/add_feedback.html', {
        'form': form,
        'job': job,
        'average_rating': average_rating,
        'feedbacks': feedbacks,
    })

# PoUR API REST
class FeedbackViewSet(viewsets.ModelViewSet):
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self) -> QuerySet:
        queryset = Feedback.objects.all()
        job_id = self.request.query_params.get('job')
        if job_id:
            queryset = queryset.filter(job_id=job_id)
        return queryset
