import csv
import os
from datetime import datetime
import django

os.environ["DJANGO_SETTINGS_MODULE"] = "employees.settings"
django.setup()

from employees_app.models import *

if __name__ == '__main__':

    with open('employees_data/persons.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            Person(id=int(row['id']), first_name=row['first_name'], last_name=row['last_name'],
                   personal_email=row['personal_email'], gender=row['gender'],
                   birth_date=datetime.strptime(row['birth_date'], "%m/%d/%Y")).save()

    with open('employees_data/companies.csv', 'r',encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            Company(id=int(row['id']), company_name=row['company_name'], country=row['country'],
                    city=row['city'], address=row['address'],
                    phone_num=row['phone_num']).save()

    with open('employees_data/employees.csv', 'r',encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            Employee.objects.create(id=row['id'], person_id=Person.objects.get(id=int(row['person_id'])),
                                    company_id=Company.objects.get(id=int(row['company_id'])),
                                    job_title=row['job_title'], is_current_job=row['is_current_job'].capitalize(),
                                    employee_email=row['company_email']).save()
