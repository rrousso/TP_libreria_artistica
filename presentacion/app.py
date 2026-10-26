import sys
import os
from datetime import datetime, date
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from objetos.cliente import Cliente
from datos.clienteData import guardarCliente, traerClientes

def menu():
    while True:
        print("\nMenú principal de operaciones de gestión:")
        print("1. Clientes")
        print("6. Salir")

        opcion = input("Ingrese una opción (1-6): ")

        if opcion == "1":
            menuClientes()
        elif opcion == "6":
            print("\nSaliendo de la aplicación")
            break
        else:
            print("\nOpción inválida")

def menuClientes():
    while True:
        print("\nMenú de operaciones de Clientes:")
        print("1. Agregar cliente")
        print("2. Ver todos los clientes")
        print("3. Ver cliente por ID")
        print("4. Buscar clientes")
        print("5. Volver")

        opcion = input("Ingrese una opción (1-5): ")

        if opcion == "1":
            menuAgregarCliente()
        elif opcion == "2":
            menuMostrarClientes()
        elif opcion == "3":
            menuMostrarstrarCliente()
        elif opcion == "4":
            menuBuscarClientes()
        elif opcion == "5":
            print("\nVolviendo a Menu Principal")
            break    
        else:
            print("\nOpción inválida")

def menuAgregarCliente():
    nombre = input("Ingrese el Nombre: ")
    apellido = input("Ingrese el Apellido: ")
    dni = input("Ingrese el Dni: ")
    fechaNac = pedirFecha("Ingrese fecha de nacimiento")
    cliente = Cliente(None, nombre, apellido, dni, fechaNac, 0)
    guardarCliente(cliente.Nombre, cliente.Apellido, cliente.Dni, cliente.FechaNacimiento)
    print("Cliente guardado.")

def menuMostrarClientes():
    clientes = traerClientes()
    print("\nLista de Clientes:")
    print("\nId - Nombre - Apellido - DNI - Fecha Nacimiento - Puntos Acumulados")
    for cli in clientes:
        cli.verDatos()


def pedirFecha(pMensaje):
    while True:
        texto = input(pMensaje + " (dd/mm/aaaa, Enter para omitir): ")
        if texto == "":
            return None
        try:
            fecha = datetime.strptime(texto, "%d/%m/%Y").date()
        except ValueError:
            print("Fecha inválida, use el formato dd/mm/aaaa.")
            continue
        if fecha > date.today():
            print("La fecha no puede ser futura.")
            continue
        return fecha
    
menu()