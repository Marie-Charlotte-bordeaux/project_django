# Permet de traduire nos données en format json
# pour quelles soient exploitable en api
from rest_framework import serializers
from job_record.models import Category, Contract, Skill, Industry, Candidate, JobRecord

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields= ['id', 'name', 'created_at', 'updated_at']

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
      model = Contract
      fields= ['id', 'type_code', 'description', 'created_at', 'updated_at']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
      model = Skill
      fields= ['id', 'name', 'created_at', 'updated_at']

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
      model = Industry
      fields= ['id', 'name', 'created_at', 'updated_at']

class CandidateSerializer(serializers.ModelSerializer):
    industry = IndustrySerializer(read_only=True)

    class Meta:
      model = Candidate
      fields= ['id', 'name', 'email', 'location', 'industry', 'created_at', 'updated_at']

class JobRecordSerializer(serializers.ModelSerializer):
      # ForeignKey affichés en détail (read_only)
      employment_type = ContractSerializer(read_only=True)
      contract = ContractSerializer(read_only=True, source='Contract')
      candidate = CandidateSerializer(read_only=True)
      industry = IndustrySerializer(read_only=True)
      category = CategorySerializer(read_only=True)
      # ManyToMany affiché en détail (read_only)
      skills = SkillSerializer(many=True, read_only=True)
  
      class Meta:
        model = JobRecord
        fields= ['id', 
                'work_year',
                'experience_level',
                'employment_type',
                'job_title',
                'salary',
                'salary_currency',
                'salary_in_usd',
                'employee_residence',
                'remote_ratio',
                'company_location',
                'company_size',
                'industry',
                'contract',
                'candidate',
                'skills',
                'category', 
                'created_at', 
                'updated_at'
                ]