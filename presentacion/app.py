import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from presentacion.menuClientes import menuClientes
from presentacion.menuVendedores import menuVendedores
from presentacion.menuProductos import menuProductos
from presentacion.menuDescuentos import menuDescuentos
from presentacion.menuVentas import menuVentas

def menu():
    while True:
        print("\nMenú principal de operaciones de gestión:")
        print("1. Clientes")
        print("2. Vendedores")
        print("3. Productos")
        print("4. Descuentos")
        print("5. Ventas")
        print("6. Salir")

        opcion = input("Ingrese una opción (1-6): ")

        if opcion == "1":
            menuClientes()
        elif opcion == "2":
            menuVendedores()
        elif opcion == "3":
            menuProductos()
        elif opcion == "4":
            menuDescuentos()
        elif opcion == "5":
            menuVentas()    
        elif opcion == "6":
            print("\nSaliendo de la aplicación")
            break
        else:
            print("\nOpción inválida")

menu()