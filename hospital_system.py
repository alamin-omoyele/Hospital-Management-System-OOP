import json
from patient import Patient


class HospitalSystem:
    def __init__(self):
        try:
            with open("patients.json", "r") as a:
                self.patients = {int(pid): Patient.from_dict(patient) for pid, patient in json.load(a).items()}
        except FileNotFoundError:
            print("File not found")
            self.patients = {}
        except IOError as e:
            print("There was a problem with the file", e)

        self.next_id = None
        if self.patients:
            self.next_id = max(pid for pid in self.patients.keys()) + 1
        else:
            self.next_id = 1001

    def add_patient(self, name, age, gender, contact, emergency_contact, insurance, status="Admitted"):
        patient_id = f"P-{self.next_id}"

        patient = Patient(patient_id, name, age, gender, contact, emergency_contact, insurance, status)
        self.patients[self.next_id] = patient

        self.next_id += 1

        print(f"Patient registered successfully with ID: {patient_id}")
        self.save_file()

    def view_patients(self):
        if self.patients:
            for pid, p in self.patients.items():
                print(p)
        else:
            print("No patients currently")

    def search_by_id(self, search_id):
        found = False

        for did, patient in self.patients.items():
            if patient.id == search_id:
                print("\n")
                print(patient)
                found = True
                break

        if not found:
            print("No patient with that ID.")

    def search_by_name(self, search_name):
        matches = [patient for patient in self.patients.values() if search_name in patient.name]

        if matches:
            print(f"\nFound {len(matches)} patient(s) with name '{search_name}':")
            for patient in matches:
                print(patient)
        else:
            print("No patient with that name.")

    def update_status(self, search_id):
        found = False

        for pid, patient in list(self.patients.items()):
            if patient.id == search_id:
                status = input("Status (Admitted/Discharged/Transferred): ")
                patient.status = status
                print(f"Patient {patient.name} ({patient.id}) has been {status}")
                found = True
                self.save_file()
                break

        if not found:
            print("No patient with that ID.")

    def add_appointment(self, patient_id, doctor, date):
        found = False

        for pid, patient in list(self.patients.items()):
            if patient.id == patient_id:
                appointment = {"doctor": doctor,
                               "date": date.strftime("%Y-%m-%d %H:%M")}

                patient.appointments.append(appointment)

                found = True
                self.save_file()
                break

        if not found:
            print("No patient with that ID.")

    def cancel_appointment(self, patient_id):
        found = False

        for pid, patient in list(self.patients.items()):
            if patient.id == patient_id:
                if patient.appointments:
                    patient.appointments.clear()
                    print(f"{patient_id}'s appointment has been cleared")
                else:
                    print("No scheduled appointment")

                found = True
                self.save_file()
                break

        if not found:
            print("No patient with that ID.")

    def view_appointment(self, patient_id):
        found = False

        for pid, patient in list(self.patients.items()):
            if patient.id == patient_id:
                if patient.appointments:
                    for a in patient.appointments:
                        print(f"Doctor: {a['doctor']}, Date: {a['date']}")

                else:
                    print("No scheduled appointment")

                found = True
                break

        if not found:
            print("No patient with that ID.")

    def save_file(self):
        try:
            with open("patients.json", "w") as a:
                json.dump({pid: patient.to_dict() for pid, patient in self.patients.items()},
                          a,
                          indent=4,
                          sort_keys=True)
        except IOError as e:
            print("There was a problem saving the file", e)

    def add_diagnosis(self, diagnosis, patient_id):
        found = False

        for pid, patient in self.patients.items():
            if patient.id == patient_id:
                patient.medical_history["Diagnoses"].append(diagnosis)
                found = True
                self.save_file()
                break

        if not found:
            print("No patient with that ID.")

    def add_surgeries(self, surgeries, patient_id):
        found = False

        for pid, patient in self.patients.items():
            if patient.id == patient_id:
                patient.medical_history["surgeries"].append(surgeries)
                found = True
                self.save_file()
                break

        if not found:
            print("No patient with that ID.")

    def add_past_illnesses(self, past_illnesses, patient_id):
        found = False

        for pid, patient in self.patients.items():
            if patient.id == patient_id:
                patient.medical_history["Past Illnesses"].append(past_illnesses)
                found = True
                self.save_file()
                break

        if not found:
            print("No patient with that ID.")

    def add_allergies(self, allergies, patient_id):
        found = False

        for pid, patient in self.patients.items():
            if patient.id == patient_id:
                patient.medical_history["allergies"].append(allergies)
                found = True
                self.save_file()
                break

        if not found:
            print("No patient with that ID.")

    def add_prescriptions(self, patient_id, date, doctor, prescription, instruction):
        found = False

        for pid, patient in self.patients.items():
            if patient.id == patient_id:
                prescription = {"date": date.strftime("%Y-%m-%d"),
                                "doctor": doctor,
                                "prescription": prescription,
                                "instruction": instruction,
                                }
                patient.prescriptions.append(prescription)
                found = True
                self.save_file()
                break

        if not found:
            print("No patient with that ID.")

    def add_progress_notes(self, patient_id, date, doctor, note):
        found = False

        for pid, patient in self.patients.items():
            if patient.id == patient_id:
                progress_notes = {"date": date.strftime("%Y-%m-%d"),
                                  "doctor": doctor,
                                  "note": note,
                                  }
                patient.progress_notes.append(progress_notes)
                found = True
                self.save_file()
                break

        if not found:
            print("No patient with that ID.")
