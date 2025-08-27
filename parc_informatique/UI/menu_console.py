from database.init_db import init_db
from Models.models import (
    add_employee,
    list_employees,
    delete_employee,
    modify_employee_department,
    add_device,
    list_devices,
    delete_device,
    add_maintenance,
    list_maintenance_by_device
)

def menu():
    init_db()

    while True:
        print("\n=== Gestion du Parc Informatique ===")
        print("1. Ajouter un employé")
        print("2. Lister les employés")
        print("3. Supprimer un employé")
        print("4. Modifier le département d’un employé")
        print("5. Ajouter un appareil")
        print("6. Lister les appareils")
        print("7. Supprimer un appareil")
        print("8. Ajouter une maintenance")
        print("9. Lister les maintenances d’un appareil")
        print("0. Quitter")

        choice = input("Choisir une option : ")

        # --- Employés ---
        if choice == '1':
            name = input("Nom de l'employé : ")
            department = input("Département : ")
            add_employee(name, department)

        elif choice == '2':
            list_employees()

        elif choice == '3':
            emp_id = input("ID de l’employé à supprimer : ")
            if emp_id.isdigit():
                delete_employee(int(emp_id))
            else:
                print("❌ ID invalide.")

        elif choice == '4':
            emp_id = input("ID de l’employé à modifier : ")
            new_dept = input("Nouveau département : ")
            if emp_id.isdigit():
                modify_employee_department(int(emp_id), new_dept)
            else:
                print("❌ ID invalide.")

        # --- Appareils ---
        elif choice == '5':
            device_type = input("Type d'appareil (PC, écran...) : ")
            brand = input("Marque : ")
            serial = input("Numéro de série : ")
            emp_id = input("ID de l'employé (laisser vide si non affecté) : ")

            employee_id = int(emp_id) if emp_id.strip() != "" else None
            add_device(device_type, brand, serial, employee_id)

        elif choice == '6':
            list_devices()

        elif choice == '7':
            dev_id = input("ID de l’appareil à supprimer : ")
            if dev_id.isdigit():
                delete_device(int(dev_id))
            else:
                print("❌ ID invalide.")

        # --- Maintenances ---
        elif choice == '8':
            device_id = input("ID de l'appareil : ")
            date = input("Date de maintenance (AAAA-MM-JJ) : ")
            description = input("Description de la maintenance : ")

            if device_id.isdigit():
                add_maintenance(int(device_id), date, description)
            else:
                print("❌ ID invalide.")

        elif choice == '9':
            device_id = input("ID de l'appareil : ")
            if device_id.isdigit():
                list_maintenance_by_device(int(device_id))
            else:
                print("❌ ID invalide.")

        # --- Quitter ---
        elif choice == '0':
            print("👋 Au revoir.")
            break

        else:
            print("❌ Option invalide. Veuillez choisir un numéro de menu.")
