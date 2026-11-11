from objetos.venta import Venta
from datos.ventaData import
from presentacion.validaciones import pedirEntero, pedirFecha, pedirTexto

def menuVentas():
    while True:
        print("\nMenú de operaciones de Ventas:")
        print("1. Crear venta")
        print("2. Ver todas las ventas")
        print("3. Ver venta por nro de factura")
        print("4. Buscar venta por cliente")
        print("5. Anular venta")
        print("6. Volver")

        opcion = input("Ingrese una opción (1-6): ")

        if opcion == "1":
            menuCrearVenta()
        elif opcion == "2":
            menuMostrarVentas()
        elif opcion == "3":
            menuMostrarVenta()
        elif opcion == "4":
            menuBuscarVentaPorNro()
        elif opcion == "5":
            menuAnularVenta()
        elif opcion == "6":
            print("\nVolviendo a Menu Principal")
            break    
        else:
            print("\nOpción inválida")