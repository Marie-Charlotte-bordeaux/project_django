# [1] Lecture du fichier CSV
# [2] Pour chaque ligne :
#    [a] Chercher ou créer le JobTitle
#    [b] Chercher ou créer la résidence employé + localisation entreprise
#    [c] Chercher ou créer le contrat (FT, PT...)
#    [d] Vérifier si la ligne existe déjà dans JobRecord (job_title + work_year + location)
#    [e] Si non existant, créer un JobRecord
# [3] À la fin, afficher combien de lignes ont été créées
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

with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        job_title = row["job_title"].strip()
        work_year = int(row["work_year"])
        employee_residence = row["employee_residence"].strip()
        contract_code = row["employment_type"].strip()
        salary = float(row["salary"])
        salary_currency = row["salary_currency"].strip()
        salary_usd = float(row["salary_in_usd"])
        remote_ratio = int(row["remote_ratio"])
        company_location = row["company_location"].strip()
        company_size = row["company_size"].strip()
        experience_level = row["experience_level"].strip()

        # 1. Contrat : chercher ou créer 
        # get_or_create= réer sans doublon
        contract_obj, _ = Contract.objects.get_or_create(
            type_code=contract_code,
            defaults={"description": contract_code} 
        )

        # 2. Vérifie s’il existe déjà (doublon)
        if JobRecord.objects.filter(
            job_title=job_title,
            work_year=work_year,
            employee_residence=employee_residence
        ).exists():
            existing_count += 1
            continue

        # 3. Créer le job
        JobRecord.objects.create(
            job_title=job_title,
            work_year=work_year,
            employee_residence=employee_residence,
            contract=contract_obj,
            experience_level=experience_level,
            salary=salary,
            salary_currency=salary_currency,
            salary_in_usd=salary_usd,
            remote_ratio=remote_ratio,
            company_location=company_location,
            company_size=company_size
        )
        created_count += 1

print(f"✅ {created_count} enregistrements créés.")
print(f"⚠️ {existing_count} doublons ignorés.")

