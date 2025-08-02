from database.init_db import init_db
from Models.models import (
    add_employee,
    list_employees,
    add_device,
    add_maintenance,
)

def menu():
    init_db()

    while True:
        print("\n=== Gestion du Parc Informatique ===")
        print("1. Ajouter un employé")
        print("2. Lister les employés")
        print("3. Ajouter un appareil")
        print("4. Ajouter une maintenance")
        print("5. Quitter")

        choice = input("Choisir une option : ")

        if choice == '1':
            name = input("Nom de l'employé : ")
            department = input("Département : ")
            add_employee(name, department)

        elif choice == '2':
            list_employees()

        elif choice == '3':
            device_type = input("Type d'appareil (PC, écran...) : ")
            brand = input("Marque : ")
            serial = input("Numéro de série : ")
            emp_id = input("ID de l'employé (laisser vide si non affecté) : ")

            employee_id = int(emp_id) if emp_id.strip() != "" else None
            add_device(device_type, brand, serial, employee_id)

        elif choice == '4':
            device_id = input("ID de l'appareil : ")
            date = input("Date de maintenance (AAAA-MM-JJ) : ")
            description = input("Description de la maintenance : ")

            if device_id.isdigit():
                add_maintenance(int(device_id), date, description)
            else:
                print("❌ ID de l'appareil invalide.")

        elif choice == '5':
            print("👋 Au revoir.")
            break

        else:
            print("❌ Option invalide. Veuillez choisir un numéro de menu.")
