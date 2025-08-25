class Patient:
    def __init__(self, patient_id, name, age, gender, contact, emergency_contact, insurance, status="Admitted"):
        self.id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact
        self.emergency_contact = emergency_contact
        self.insurance = insurance
        self.status = status
        self.appointments = []

        # Phase 2 addition
        self.medical_history = {
            "diagnoses": [],
            "surgeries": [],
            "past illnesses": [],
            "allergies": [],
        }
        self.prescriptions = []
        self.progress_notes = []

    def __str__(self):
        return (f"\nID: {self.id}"
                f"\nName: {self.name}"
                f"\nAge: {self.age}"
                f"\nGender: {self.gender}"
                f"\nContact: {self.contact}"
                f"\nEmergency Contact: {self.emergency_contact}"
                f"\nInsurance: {self.insurance}"
                f"\nStatus: {self.status}"
                f"\nAppointments: {self.appointments}"
                f"\nMedical History: {self.medical_history}"
                f"\nPrescriptions: {self.prescriptions}"
                f"\nProgress Notes: {self.progress_notes}")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "contact": self.contact,
            "emergency_contact": self.emergency_contact,
            "insurance": self.insurance,
            "status": self.status,
            "appointments": self.appointments,
            "medical_history": self.medical_history,
            "prescriptions": self.prescriptions,
            "progress_notes": self.progress_notes,
        }

    @classmethod
    def from_dict(cls, data):
        patient = cls(
            patient_id=data['id'],
            name=data['name'],
            age=data['age'],
            gender=data['gender'],
            contact=data['contact'],
            emergency_contact=data['emergency_contact'],
            insurance=data['insurance'],
            status=data['status'],
        )
        patient.appointments = data.get("appointments", [])
        patient.medical_history = data.get("medical_history", {
            "diagnoses": [],
            "surgeries": [],
            "past Illnesses": [],
            "allergies": [],
        })
        patient.prescriptions = data.get("prescriptions", [])
        patient.progress_notes = data.get("progress_notes", [])
        return patient
