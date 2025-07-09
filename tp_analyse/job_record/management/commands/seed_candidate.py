# job_record/management/commands/seed_candidate.py

from django.core.management.base import BaseCommand
from job_record.models import Candidate, Industry, Skill, JobRecord, Contract
import random
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tp-analyse.settings')
django.setup()
class Command(BaseCommand):
    help = "Seed candidates, industries, and skills"

    def handle(self, *args, **kwargs):
        # Industries
        industry_names = ['Tech', 'Finance', 'Healthcare', 'Education']
        industries = [Industry.objects.get_or_create(name=name)[0] for name in industry_names]

        # Skills
        skill_names = ['Python', 'Django', 'Excel', 'Machine Learning', 'Communication']
        skills = [Skill.objects.get_or_create(name=name)[0] for name in skill_names]

        # Contracts (obligatoire pour JobRecord)
        contract, _ = Contract.objects.get_or_create(type_code='FT', defaults={'description': 'Full Time'})

        for i in range(5):
            candidate = Candidate.objects.create(
                name=f"Candidate {i+1}",
                email=f"candidate{i+1}@example.com",
                location=random.choice(['Paris', 'London', 'Berlin']),
                industry=random.choice(industries)
            )

            job = JobRecord.objects.create(
                work_year=2025,
                experience_level=random.choice(['EN', 'MI', 'SE']),
                employment_type=contract,
                job_title=f"Developer {i+1}",
                salary=60000 + i * 1000,
                salary_currency='USD',
                salary_in_usd=60000 + i * 1000,
                employee_residence='Remote',
                remote_ratio=100,
                company_location='USA',
                company_size=random.choice(['S', 'M', 'L']),
                industry=random.choice(industries),
                candidate=candidate,
            )

            job.skills.set(random.sample(skills, k=random.randint(1, 3)))

        self.stdout.write(self.style.SUCCESS("✅ Candidates, Industries, and Skills seeded successfully."))
