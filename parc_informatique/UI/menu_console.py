from database.init_db import init_db
from Models.models import add_employee, list_employees

def menu():
    init_db()

    while True:
        print("\n=== Gestion du Parc Informatique ===")
        print("1. Ajouter un employé")
        print("2. Lister les employés")
        print("3. Quitter")

        choice = input("Choisir une option : ")

        if choice == '1':
            name = input("Nom : ")
            dept = input("Département : ")
            add_employee(name, dept)
        elif choice == '2':
            list_employees()
        elif choice == '3':
            break
        else:
            print("Option invalide.")

if __name__ == "__main__":
    menu()
import sqlite3