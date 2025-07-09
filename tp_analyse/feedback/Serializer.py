# Permet de traduire nos données en format json
# pour quelles soient exploitable en api
from rest_framework import serializers
from .models import Feedback
from job_record.Serializer import JobRecordSerializer, CandidateSerializer

class FeedbackSerializer(serializers.ModelSerializer):
  # ForeignKey affichés en détail (read_only)
  job = JobRecordSerializer(read_only=True)
  author_name = CandidateSerializer(read_only=True)

  class Meta:
    model = Feedback
    fields= ['id', 'job', 'author_name', 'comment', 'rating', 'created_at']
