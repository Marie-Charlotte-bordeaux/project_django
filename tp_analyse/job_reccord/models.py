from django.db import models

# Modèles complémentaires

class Contract(models.Model):
    type_code = models.CharField(max_length=10, unique=True)  # ex: 'FT', 'PT'
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.type_code} - {self.description}"

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Industry(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Modèle principal (reprend ce que tu avais déjà)

class JobRecord(models.Model):
    work_year = models.PositiveIntegerField()
    experience_level = models.CharField(max_length=10)
    contract = models.ForeignKey(Contract, on_delete=models.SET_NULL, null=True)
    job_title = models.CharField(max_length=200)
    salary = models.FloatField()
    salary_currency = models.CharField(max_length=10)
    salary_in_usd = models.FloatField()
    employee_residence = models.CharField(max_length=50)
    remote_ratio = models.IntegerField()
    company_location = models.CharField(max_length=50)
    company_size = models.CharField(max_length=10)
    industry = models.ForeignKey(Industry, on_delete=models.SET_NULL, null=True, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.job_title} ({self.work_year})"
