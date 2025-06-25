import datetime

class PatientRecord:
    def __init__(self, patient_id, name, date_of_birth, gender, contact_info, address):
        self.patient_id = patient_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.contact_info = contact_info
        self.address = address
        self.medical_history = []
        self.visits = []

    def add_medical_history(self, condition, notes, date=None):
        if date is None:
            date = datetime.date.today()
        self.medical_history.append({
            'date': date,
            'condition': condition,
            'notes': notes
        })

    def add_visit(self, doctor, reason, diagnosis, treatment, date=None):
        if date is None:
            date = datetime.date.today()
        self.visits.append({
            'date': date,
            'doctor': doctor,
            'reason': reason,
            'diagnosis': diagnosis,
            'treatment': treatment
        })

    def __str__(self):
        return f"Patient {self.patient_id}: {self.name} ({self.gender}, DOB: {self.date_of_birth})"

class MedicalRecordSystem:
    def __init__(self):
        self.records = {}

    def add_patient(self, patient_id, name, date_of_birth, gender, contact_info, address):
        if patient_id in self.records:
            print(f"Patient ID {patient_id} already exists.")
            return False
        self.records[patient_id] = PatientRecord(patient_id, name, date_of_birth, gender, contact_info, address)
        print(f"Added patient {name} with ID {patient_id}.")
        return True

    def get_patient(self, patient_id):
        return self.records.get(patient_id, None)

    def add_medical_history(self, patient_id, condition, notes, date=None):
        patient = self.get_patient(patient_id)
        if patient:
            patient.add_medical_history(condition, notes, date)
            print(f"Added history for {patient_id}: {condition}")
        else:
            print(f"Patient ID {patient_id} not found.")

    def add_visit(self, patient_id, doctor, reason, diagnosis, treatment, date=None):
        patient = self.get_patient(patient_id)
        if patient:
            patient.add_visit(doctor, reason, diagnosis, treatment, date)
            print(f"Added visit for {patient_id} with Dr. {doctor}")
        else:
            print(f"Patient ID {patient_id} not found.")

    def print_patient_record(self, patient_id):
        patient = self.get_patient(patient_id)
        if not patient:
            print(f"Patient ID {patient_id} not found.")
            return
        print(str(patient))
        print("Contact:", patient.contact_info)
        print("Address:", patient.address)
        print("\n--- Medical History ---")
        for entry in patient.medical_history:
            print(f"{entry['date']}: {entry['condition']} - {entry['notes']}")
        print("\n--- Visits ---")
        for visit in patient.visits:
            print(f"{visit['date']} | Doctor: {visit['doctor']} | Reason: {visit['reason']}")
            print(f"Diagnosis: {visit['diagnosis']} | Treatment: {visit['treatment']}")
            print("-" * 40)

# Example usage:
if __name__ == "__main__":
    mrs = MedicalRecordSystem()
    mrs.add_patient('P001', 'John Doe', '1980-01-01', 'Male', '555-1234', '123 Main St')
    mrs.add_patient('P002', 'Jane Smith', '1990-06-15', 'Female', '555-5678', '456 Elm Ave')

    mrs.add_medical_history('P001', 'Hypertension', 'Patient on medication since 2010')
    mrs.add_visit('P001', 'Dr. Adams', 'Routine Checkup', 'Blood pressure high', 'Adjusted medication')

    mrs.add_medical_history('P002', 'Asthma', 'Diagnosed in childhood')
    mrs.add_visit('P002', 'Dr. Baker', 'Asthma Attack', 'Acute episode', 'Nebulizer, prescribed inhaler')

    mrs.print_patient_record('P001')
    mrs.print_patient_record('P002')
