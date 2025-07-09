from django.core.management.base import BaseCommand
from job_record.models import JobRecord, Candidate
from feedback.models import Feedback
import random
import os
import django

class Command(BaseCommand):
    help = "Seed feedback for existing job records"

    def handle(self, *args, **kwargs):
        job_records = JobRecord.objects.exclude(candidate=None)

        if not job_records.exists():
            self.stdout.write(self.style.WARNING("⚠️ No job records found with candidates."))
            return

        for job in job_records:
            Feedback.objects.create(
                job=job,
                author_name=job.candidate,
                comment=f"This job as {job.job_title} was a great opportunity.",
                rating=random.randint(1, 5)
            )

        self.stdout.write(self.style.SUCCESS("✅ Feedback seeded successfully."))
