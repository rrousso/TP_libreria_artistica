from objetos.producto import Producto
from datos.productoData import guardarProducto, traerProductos, traerProducto, buscarProductos, modificarProducto, eliminarProducto
from datos.ventaData import productoTieneVentas
from presentacion.validaciones import pedirEntero, pedirFecha, pedirEnteroOVacio, pedirTexto, pediDecimal, pedirDecimalOVacio

def menuClientes():
    while True:
        print("\nMenú de operaciones de Productos:")
        print("1. Agregar productos")
        print("2. Ver todos los productos")
        print("3. Ver producto por ID")
        print("4. Buscar producto")
        print("5. Modificar producto")
        print("6. Eliminar producto")
        print("7. Volver")

        opcion = input("Ingrese una opción (1-7): ")

        if opcion == "1":
            menuAgregarProducto()
        elif opcion == "2":
            menuMostrarProductos()
        elif opcion == "3":
            menuMostrarProducto()
        elif opcion == "4":
            menuBuscarProductos()
        elif opcion == "5":
            menuModificarProducto()
        elif opcion == "6":
            menuEliminarProducto()
        elif opcion == "7":
            print("\nVolviendo a Menu Principal")
            break    
        else:
            print("\nOpción inválida")

def menuAgregarProducto():
    descripcion = pedirTexto("Ingrese la descripción: ")
    marca = input("Ingrese marca: ")
    categoria = input("Ingrese categoria: ")
    presentacion = input("Ingrese presentación: ")
    unidades = pedirEntero("Ingrese unidades por paquete:")
    precio = pediDecimal("Ingrese precio")
    stock = pedirEntero("Ingrese cantidad de Stock disponible:")

    producto = Producto(None, descripcion, marca, categoria, presentacion, unidades, precio, stock)
    guardarProducto(producto.Descripcion, producto.Marca, producto.Categoria, producto.Presentacion, producto.Unidades, producto.Precio, producto.Stock)
    print("Poducto guardado.")

def menuMostrarProductos():
    productos = traerProductos()
    print("\nLista de Productos:")
    print("\nId - Descripción - Precio - Stock")
    for pro in productos:
        pro.verDatos()

def menuMostrarProducto():
    idProducto = pedirEntero("Ingrese Id: ")
    producto = traerProducto(idProducto)
    if producto is None:
        print("No existe un producto con ese id.")
    else:
        print("\nDatos de producto:")
        print("\nId - Descripción - Marca - Categoría - Presentación - Unidades - Precio - Stock")
        producto.verDatosCompletos()

def menuBuscarProductos():
    textoBusqueda = input("Ingrese Descripción, Marca, Categoría o Presentación a buscar: ")
    productos = buscarProductos(textoBusqueda)
    if len(productos) == 0:
        print("\nNo se encontraron productos.")
    else:
        print("\nLista de Clientes encontrados:")
        print("\nId - Descripción - Marca - Categoría - Presentación - Unidades - Precio - Stock")
        for pro in productos:
            pro.verDatosCompletos()

def menuModificarProducto():
    idProducto = pedirEntero("Ingrese Id de usuario a modificar: ")
    producto = traerProducto(idProducto)
    if producto is None:
        print("No existe un producto con ese id.")
    else:
        print("\nPresione Enter si no desea modificar el campo:")
        descripcion = input("Descripción (" + producto.Descripcion + "):").strip()
        if descripcion != "":
            producto.Descripcion = descripcion

        marca = input("Marca (" + producto.Marca + "):").strip()
        if marca != "":
            producto.Marca = marca

        categoria = input("Categoría (" + producto.Categoria + "):").strip()
        if categoria != "":
            producto.Categoria = categoria

        presentacion = input("Presentación (" + producto.Presentacion + "):").strip()
        if presentacion != "":
            producto.Presentacion = presentacion

        unidades = pedirEnteroOVacio("Unidades (" + producto.Unidades + "):")
        if unidades != None:
            producto.Unidades = unidades

        precio = pedirDecimalOVacio("Unidades (" + producto.Precio + "):")
        if precio != None:
            producto.Precio = precio

        stock = pedirEnteroOVacio("Stock (" + producto.Stock + "):")
        if stock != None:
            producto.Stock = stock

        modificarProducto(producto.Descripcion, producto.Marca, producto.Categoria, producto.Presentacion, producto.Unidades, producto.Precio, producto.Stock)
        print("Producto Modificado:")
        producto.verDatosCompletos()


def menuEliminarProducto():
    idProducto = pedirEntero("Ingrese Id: ")
    producto = traerProductos(idProducto)
    if producto is None:
        print("\nNo existe un producto con ese id.")
    elif productoTieneVentas(idProducto):
        print("\nNo se puede borrar: el producto tiene ventas registradas.")
    else:
        eliminarProducto(producto.Id)
        print("\nProducto Eliminado.")
