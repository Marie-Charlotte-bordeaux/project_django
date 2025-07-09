from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from job_record.models import *
from job_record.serializers import JobRecordSerializer

class JobRecordSerializerTest1(APITestCase):
    def setUp(self):
        self.contract = Contract.objects.create(type_code="CDI", description="Contrat CDI")
        self.candidate = Candidate.objects.create(name="Jean", email="jean@test.com", location="Paris")
        self.industry = Industry.objects.create(name="Tech")
        self.category = Category.objects.create(name="Développement")
        self.skill = Skill.objects.create(name="Python")

    def test_valid_serializer(self):
        data = {
            "work_year": 2025,
            "experience_level": "SE",
            "employment_type_id": self.contract.id, # type: ignore
            "contract_id": self.contract.id,# type: ignore
            "candidate_id": self.candidate.id,# type: ignore
            "industry_id": self.industry.id,# type: ignore
            "category_id": self.category.id,# type: ignore
            "skills_ids": [self.skill.id],# type: ignore
            "job_title": "Dev Python",
            "salary": "60000",
            "salary_currency": "EUR",
            "salary_in_usd": "64000",
            "employee_residence": "France",
            "remote_ratio": 100,
            "company_location": "France",
            "company_size": "L"
        }

        serializer = JobRecordSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        instance = serializer.save()
        self.assertEqual(instance.job_title, "Dev Python")


from job_record.models import Contract, Candidate, Industry, Category, Skill

class JobRecordSerializerTest(TestCase):
    def test_jobrecord_serializer_valid(self):
        contract = Contract.objects.create(type_code="CDI", description="Contrat à durée indéterminée")
        industry = Industry.objects.create(name="Informatique")
        candidate = Candidate.objects.create(name="Alice", email="alice@example.com", location="Paris", industry=industry)
        category = Category.objects.create(name="Développement")

        job_data = {
            'work_year': 2025,
            'experience_level': 'SE',
            'employment_type': contract.id,
            'job_title': "Développeur Python",
            'salary': "50000.00",
            'salary_currency': "EUR",
            'salary_in_usd': "55000.00",
            'employee_residence': "France",
            'remote_ratio': 50,
            'company_location': "France",
            'company_size': "M",
            'industry': industry.id,
            'Contract': contract.id,
            'candidate': candidate.id,
            'skills': [],
            'category': category.id,
        }

        serializer = JobRecordSerializer(data=job_data)
        # Tester la validité
        print(serializer.is_valid())         # ✅ True attendu
        print(serializer.validated_data)     # Les données validées
        print(serializer.errors)             # S'il y a des erreurs

        self.assertTrue(serializer.is_valid(), serializer.errors)

