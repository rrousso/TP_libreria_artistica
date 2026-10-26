import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def menu():
    while True:
        print("Menú principal de operaciones de gestión:")
        print("1. Salir")
        print("6. Salir")

        opcion = int(input("Ingrese una opción (1-6): "))

        if opcion == 1:
            print("\n Saliendo de la aplicación")
            break
        elif opcion == 6:
            print("\n Saliendo de la aplicación")
            break
        else:
            print("ERROR !!! no existe la opción ingresada...")

menu()