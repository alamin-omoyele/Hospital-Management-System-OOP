from datetime import datetime
from hospital_system import HospitalSystem


system = HospitalSystem()


def get_input(prompt, validation_func=None, error_msg="Invalid input"):
    """
    Get input from the user and validate it.

    :param prompt: str, the message to show to the user
    :param validation_func: function, takes the input and returns True if valid
    :param error_msg: str, message to display when input is invalid
    :return: the validated input
    """
    while True:
        user_input = input(prompt).strip()
        if validation_func is None or validation_func(user_input):
            return user_input
        else:
            print(error_msg)


def menu():
    is_on = True
    while is_on:
        print("\nMain Menu")
        print("1. Patient Management"
              "\n2. Appointment Management"
              "\n3. Clinic Management"
              "\n4. Exit")

        menu_option = get_input("\nSelect an option",
                                lambda x: x.isdigit(), "Enter a valid number")

        match menu_option:
            case 1:
                patient_menu = True
                while patient_menu:
                    print("\n1. Register Patient"
                          "\n2. View all patient"
                          "\n3. Search patient"
                          "\n4. Update patient status"
                          "\n5. Back to Main Menu")

                    patient_menu_option = int(input("\nSelect an option: "))
                    match patient_menu_option:
                        case 1:
                            print("Register New Patient")
                            name = get_input("\nPatient's name: ", lambda x: x != "").title()
                            age = int(get_input("Patient's age: ", lambda x: x.isdigit() and int(x) >= 0))
                            gender = get_input("Patient's gender (F/M): ",
                                               lambda x: x != "" and x in ["F", "M"]).upper()
                            contact = get_input("Patient's contact: ", lambda x: x.isdigit() and len(x) == 11)
                            emergency_contact = get_input("Patient's emergency contact: ",
                                                          lambda x: x.isdigit() and len(x) == 11)
                            insurance = get_input("Patient's insurance: ",
                                                  lambda x: x != "", "Enter None if none")
                            status = get_input("Status (Admitted/Discharged/Transferred): ",
                                               lambda x: x in ["Admitted", "Discharged", "Transferred"])

                            system.add_patient(name, age, gender, contact, emergency_contact, insurance, status)

                        case 2:
                            system.view_patients()

                        case 3:
                            search_menu = True
                            while search_menu:
                                print("\n1. Search by ID"
                                      "\n2. Search by name"
                                      "\n3. Back to Main Menu")

                                try:
                                    search_option = int(input("\nSelect an option: "))
                                    match search_option:
                                        case 1:
                                            while True:
                                                search_id = input("Patient's ID: ").strip()
                                                if search_id:
                                                    system.search_by_id(search_id)
                                                    break
                                                else:
                                                    print("Invalid ID")
                                        case 2:
                                            while True:
                                                search_name = input("Patient's name: ").title().strip()
                                                if search_name:
                                                    system.search_by_name(search_name)
                                                    break
                                                else:
                                                    print("Invalid name")

                                        case 3:
                                            search_menu = False

                                        case _:
                                            print("Invalid option")

                                except ValueError:
                                    print("Invalid option")

                        case 4:
                            while True:
                                search_id = input("Patient's ID: ").strip()
                                system.update_status(search_id)
                                break

                        case 5:
                            patient_menu = False

                        case _:
                            print("Invalid option")

            case 2:
                appointment_menu = True
                while appointment_menu:
                    print("\n1. Schedule Appointment"
                          "\n2. Cancel Appointment"
                          "\n3. View Appointment"
                          "\n4. Back to Main Menu")

                    appointment_option = int(input("\nSelect an option: "))
                    match appointment_option:
                        case 1:
                            patient_id = input("Patient's ID: ").strip()
                            doctor = input("Doctor's Name: ")
                            while True:
                                date_input = input("Enter appointment date and time (YYYY-MM-DD HH:MM): ")
                                try:
                                    date = datetime.strptime(date_input, "%Y-%m-%d %H:%M")
                                    break
                                except ValueError:
                                    print("Invalid format. Please use YYYY-MM-DD HH:MM")
                            system.add_appointment(patient_id, doctor, date)

                        case 2:
                            patient_id = input("Patient's ID: ").strip()
                            system.cancel_appointment(patient_id)

                        case 3:
                            patient_id = input("Patient's ID: ").strip()
                            system.view_appointment(patient_id)

                        case 4:
                            appointment_menu = False  # exit the appointments loop

                        case _:
                            print("Invalid option")

            case 3:
                clinical_menu = True
                while clinical_menu:
                    print("\n1. add Diagnosis"
                          "\n2. Add Past Illness"
                          "\n3. Add Surgery"
                          "\4. Add Allergy"
                          "\n5. Add Prescription"
                          "\n6. Add Progress Note"
                          "\n7. Back to Main  Menu")

                    clinical_option = get_input("\nSelect an option",
                                                lambda x: x.isdigit(), "Enter a valid number")
                    match clinical_option:
                        case 1:
                            patient_id = input("Patient's ID: ").strip()
                            diagnosis = input("Diagnosis: ")
                            system.add_diagnosis(diagnosis, patient_id)

                        case 2:
                            patient_id = input("Patient's ID: ").strip()
                            past_illness = input("Past Illness: ")
                            system.add_past_illnesses(past_illness, patient_id)

                        case 3:
                            patient_id = input("Patient's ID: ").strip()
                            surgery = input("Surgery: ")
                            system.add_surgeries(surgery, patient_id)

                        case 4:
                            patient_id = input("Patient's ID: ").strip()
                            allergies = input("Allergies: ")
                            system.add_allergies(allergies, patient_id)

                        case 5:
                            patient_id = input("Patient's ID: ").strip()
                            doctor = input("Doctor's Name: ")
                            prescription = input("Prescription: ")
                            instruction = input("Instruction: ")

                            while True:
                                date_input = input("Enter date (YYYY-MM-DD): ")
                                try:
                                    date = datetime.strptime(date_input, "%Y-%m-%d")
                                    break
                                except ValueError:
                                    print("Invalid format. Please use YYYY-MM-DD")

                            system.add_prescriptions(patient_id, date, doctor, prescription, instruction)

                        case 6:
                            patient_id = input("Patient's ID: ").strip()
                            doctor = input("Doctor's Name: ")
                            note = input("Note: ")
                            while True:
                                date_input = input("Enter date (YYYY-MM-DD): ")
                                try:
                                    date = datetime.strptime(date_input, "%Y-%m-%d")
                                    break
                                except ValueError:
                                    print("Invalid format. Please use YYYY-MM-DD ")

                            system.add_progress_notes(patient_id, date, doctor, note)

                        case 7:
                            clinical_menu = False

                        case _:
                            print("Invalid Option")

            case 4:
                is_on = False

            case _:
                print("Invalid option")


menu()
