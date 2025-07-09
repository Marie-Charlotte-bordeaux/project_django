from django.db import models
from job_record.models import JobRecord, Candidate

class Feedback(models.Model):
    job = models.ForeignKey(JobRecord, on_delete=models.CASCADE, related_name='feedbacks')
    author_name = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.author_name} for {self.job}"
