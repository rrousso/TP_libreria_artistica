from objetos.venta import Venta
from presentacion.validaciones import pedirEntero, pedirFecha, pedirTexto

def menuVentas():
    while True:
        print("\nMenú de operaciones de Ventas:")
        print("1. Crear venta")
        print("2. Ver todas las ventas")
        print("3. Ver venta por nro de factura")
        print("4. Buscar venta por cliente")
        print("5. Eliminar venta")
        print("6. Volver")

        opcion = input("Ingrese una opción (1-6): ")

        if opcion == "1":
            menuCrearVenta()
        elif opcion == "2":
            menuMostrarVentas()
        elif opcion == "3":
            menuBuscarVentaPorNro()
        elif opcion == "4":
            menuBuscarVentaPorCliente()
        elif opcion == "5":
            menuEliminarVenta()
        elif opcion == "6":
            print("\nVolviendo a Menu Principal")
            break    
        else:
            print("\nOpción inválida")

def menuCrearVenta():
    print("pendiente")

def menuMostrarVentas():
    print("pendiente")

def menuBuscarVentaPorNro():
    print("pendiente")

def menuBuscarVentaPorCliente():
    print("pendiente")

def menuEliminarVenta():
    print("pendiente")