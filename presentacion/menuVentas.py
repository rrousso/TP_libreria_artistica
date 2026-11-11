from datetime import datetime

from objetos.venta import Venta
from objetos.detalleVenta import DetalleVenta
from datos.ventaData import guardarVenta, traerVentas, traerVentaPorFactura, traerVentasPorCliente
from datos.vendedorData import traerVendedor
from datos.clienteData import traerCliente
from datos.productoData import traerProducto
from datos.descuentoData import traerDescuentosAplicables
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
            menuBuscarVentasPorCliente()
        elif opcion == "5":
            menuEliminarVenta()
        elif opcion == "6":
            print("\nVolviendo a Menu Principal")
            break    
        else:
            print("\nOpción inválida")

def menuCrearVenta():
    idVendedor = pedirEntero("Ingrese Id de vendedor: ")
    vendedor = traerVendedor(idVendedor)
    if vendedor is None:
        print("No existe un vendedor con ese id.")
        return
    idCliente = pedirEntero("Ingrese Id de cliente: ")
    cliente = traerCliente(idCliente)
    if cliente is None:
        print("No existe un cliente con ese id.")
        return
    venta = Venta(None, datetime.now(), cliente, vendedor)
    while True:
        idProducto = pedirEntero("\nIngrese Id del producto (0 para finalizar): ")
        if idProducto == 0:
            break

        producto = traerProducto(idProducto)
        if producto is None:
            print("No existe un producto con ese id.")
            continue

        cantidad = pedirEntero("Ingrese cantidad: ")
        if cantidad == 0:
            print("La cantidad debe ser mayor a 0.")
            continue
        if cantidad > producto.Stock:
            print("Stock insuficiente. Disponible: " + str(producto.Stock))
            continue

        detalle = DetalleVenta(producto, cantidad, producto.Precio, 0)
        detalle.aplicarMejorDescuento(traerDescuentosAplicables(producto))
        venta.Detalles.append(detalle)
        print("Agregado: " + producto.Descripcion +" X " + str(cantidad) + " - Descuento: " +  f"{detalle.DescuentoAplicado:.2f}" + " - Total línea: " + f"{detalle.calcularTotal():.2f}")

    if len(venta.Detalles) == 0:
        print("\nVenta cancelada: no se agregaron productos.")
        return

    venta.Subtotal = venta.calcularSubtotal()
    venta.Total = venta.calcularTotal()

    print("\nResumen de la venta:")
    venta.verDatosSinID()
    confirmar = input("\n¿Confirmar venta? (s/n): ").strip().lower()
    if confirmar != "s":
        print("Venta cancelada.")
        return

    try:
        idVenta = guardarVenta(venta)
        print("\nVenta Nro " + str(idVenta) + " guardada.")
    except Exception:
        print("\nNo se pudo guardar la venta.")


def menuMostrarVentas():
    ventas = traerVentas()
    if len(ventas) == 0:
            print("No hay ventas realizadas.")
    else:
        print("\nLista de Ventas:")
        for venta in ventas:
            venta.verDatos()
            print("****")

def menuBuscarVentaPorNro():
    idVenta = pedirEntero("Ingrese nro de factura: ")
    venta = traerVentaPorFactura(idVenta)
    if venta is None:
        print("\nNo hay ventas con ese nro de factura.")
    else:
        print("\nVentas nro " + str(idVenta) + ":")
        venta.verDatos()

def menuBuscarVentasPorCliente():
    dniCliente = pedirTexto("Ingrese DNI de cliente: ")
    ventas = traerVentasPorCliente(dniCliente)
    if ventas is None:
        print("\nNo hay clientes con ese DNI.")
    elif len(ventas) == 0:
        print("\nNo hay ventas con ese cliente.")
    else:
        for venta in ventas:
            venta.verDatos()
            print("****")

def menuEliminarVenta():
    print("pendiente")