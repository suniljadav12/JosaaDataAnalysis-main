import csv
from .models import Admission

def populate_admissions():
    with open('modified_data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            admission = Admission(
                institute=row['Institute'],
                academic_program_name=row['Academic Program Name'],
                seat_type=row['Seat Type'],
                gender=row['Gender'],
                opening_rank=int(row['Opening Rank']),
                closing_rank=int(row['Closing Rank']),
                year=int(row['Year']),
                round=int(row['Round']),
                has_p=bool(row['Has_P'])
            )
            admission.save()

