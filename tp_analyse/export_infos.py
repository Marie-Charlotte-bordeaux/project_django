from django.db.models import Avg, Count
import os
import csv
import django
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tp_analyse.settings')
django.setup()

from job_record.models import JobRecord, Contract, Industry, Candidate
# Charger le CSV
csv_path = "./datas/salaries.csv"
created_count = 0
existing_count = 0

# Préparation du fichier résultat
output_lines = []
output_lines.append(f"✅ {created_count} enregistrements créés.")
output_lines.append(f"⚠️ {existing_count} doublons ignorés.\n")

# 1. Les 5 jobs les mieux payés
top_jobs = (
    JobRecord.objects
    .values('job_title')
    .annotate(avg_salary=Avg('salary_in_usd'))
    .order_by('-avg_salary')[:5]
)
output_lines.append("🔥 Top 5 Job Titles les mieux payés (en USD) :")
for job in top_jobs:
    output_lines.append(f"- {job['job_title']}: {job['avg_salary']:.2f} USD")

# 2. Salaire moyen par niveau d'expérience
exp_avg = (
    JobRecord.objects
    .values('experience_level')
    .annotate(avg_salary=Avg('salary_in_usd'))
    .order_by('experience_level')
)
output_lines.append("\n📊 Salaire moyen par niveau d'expérience :")
for item in exp_avg:
    output_lines.append(f"- {item['experience_level']}: {item['avg_salary']:.2f} USD")

# 3. Nombre de jobs par localisation entreprise
loc_counts = (
    JobRecord.objects
    .values('company_location')
    .annotate(job_count=Count('id'))
    .order_by('-job_count')[:10]
)
output_lines.append("\n🌍 Nombre de jobs par localisation entreprise :")
for loc in loc_counts:
    output_lines.append(f"- {loc['company_location']}: {loc['job_count']} jobs")

# 4. Ratio de jobs 100% remote
total_jobs = JobRecord.objects.count()
remote_jobs = JobRecord.objects.filter(remote_ratio=100).count()
ratio_remote = (remote_jobs / total_jobs) * 100 if total_jobs else 0
output_lines.append(f"\n🌐 Ratio de jobs 100% remote : {ratio_remote:.2f}%")

# Sauvegarde dans fichier texte
with open("resultats_analyse.txt", "w", encoding="utf-8") as f:
    for line in output_lines:
        print(line)
        f.write(line + "\n")
