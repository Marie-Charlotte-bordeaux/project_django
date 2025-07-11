# Permet de traduire nos données en format json
# pour quelles soient exploitable en api
from rest_framework import serializers

from job_record.models import Candidate, JobRecord
from feedback.models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
  # ForeignKey affichés en détail (read_only)
  job = serializers.PrimaryKeyRelatedField(queryset=JobRecord.objects.all())
  author_name = serializers.PrimaryKeyRelatedField(queryset=Candidate.objects.all())


  class Meta:
    model = Feedback
    fields= ['id', 'job', 'author_name', 'comment', 'rating', 'created_at']
