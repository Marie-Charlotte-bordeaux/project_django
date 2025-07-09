from django.core.management.base import BaseCommand
from job_record.models import JobRecord, Candidate
from feedback.models import Feedback
import random
import os
import django

class Command(BaseCommand):
    help = "Seed feedback for existing job records"

    def handle(self, *args, **kwargs):
        job = JobRecord.objects.exclude(candidate=None).order_by('?').first()

        if not job:
            self.stdout.write(self.style.WARNING("⚠️ No job records found with candidates."))
            return

        feedback_comments = [
            "Excellent experience overall!",
            "Challenging but rewarding.",
            "I loved working with the team.",
            "The salary was fair and benefits were good.",
            "Work-life balance could be improved.",
            "Remote setup worked perfectly.",
            "Great learning environment.",
            "Would recommend this job to others.",
            "Lots of growth potential.",
            "Not what I expected, but valuable nonetheless."
        ]

        num_feedbacks = 10
        for _ in range(num_feedbacks):
            Feedback.objects.create(
                job=job,
                author_name=job.candidate,
                comment=random.choice(feedback_comments),
                rating=random.randint(1, 5)
            )

        self.stdout.write(self.style.SUCCESS(
            f"✅ {num_feedbacks} feedbacks created for job: {job.job_title} ({job.id})" # type: ignore
        ))
