import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from presentacion.menuClientes import menuClientes
from presentacion.menuVendedores import menuVendedores

def menu():
    while True:
        print("\nMenú principal de operaciones de gestión:")
        print("1. Clientes")
        print("2. Vendedores")
        print("6. Salir")

        opcion = input("Ingrese una opción (1-6): ")

        if opcion == "1":
            menuClientes()
        elif opcion == "2":
            menuVendedores()
        elif opcion == "6":
            print("\nSaliendo de la aplicación")
            break
        else:
            print("\nOpción inválida")

menu()