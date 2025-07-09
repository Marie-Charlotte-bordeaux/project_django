from django.db import models

# Modèles complémentaires

class Contract(models.Model):
    type_code = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.type_code


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class Industry(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=100)
    industry = models.ForeignKey(Industry, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class JobRecord(models.Model):
    EXPERIENCE_LEVEL_CHOICES = [
        ('EN', 'Entry-level'),
        ('MI', 'Mid-level'),
        ('SE', 'Senior-level'),
        ('EX', 'Executive-level'),
    ]

    COMPANY_SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    ]

    work_year = models.PositiveIntegerField()
    experience_level = models.CharField(max_length=2, choices=EXPERIENCE_LEVEL_CHOICES)
    employment_type = models.ForeignKey(Contract, on_delete=models.SET_NULL, null=True, related_name='job_records')
    job_title = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    salary_currency = models.CharField(max_length=10)
    salary_in_usd = models.DecimalField(max_digits=10, decimal_places=2)
    employee_residence = models.CharField(max_length=100)
    remote_ratio = models.PositiveSmallIntegerField(help_text="Percentage of remote work (0-100)")
    company_location = models.CharField(max_length=100)
    company_size = models.CharField(max_length=1, choices=COMPANY_SIZE_CHOICES)
    industry = models.ForeignKey(Industry, on_delete=models.SET_NULL, null=True, blank=True)
    Contract = models.ForeignKey(Contract, on_delete=models.SET_NULL, null=True, blank=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.SET_NULL, null=True, blank=True, related_name='job_records')
    skills = models.ManyToManyField(Skill, related_name='candidates')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.job_title} ({self.work_year})"