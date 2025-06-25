import csv

def export_patients_to_csv(patients, file_path):
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'Name', 'DOB', 'Gender', 'Contact', 'Address'])
        for p in patients:
            writer.writerow([p.id, p.name, p.date_of_birth, p.gender, p.contact_info, p.address])
