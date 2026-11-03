from decimal import Decimal

from objetos.descuento import Descuento
from objetos.tipoDescuento import TipoDescuento
from datos.descuentoData import guardarDescuento, traerDescuentos, traerDescuento, buscarDescuentos, modificarDescuento, eliminarDescuento
from presentacion.validaciones import pedirEntero, elegirUnaOpcionDeDos, pedirTexto, pedirPorcentaje, pedirPorcentajeOVacio

def menuDescuentos():
    while True:
        print("\nMenú de operaciones de Descuentos:")
        print("1. Agregar descuentos")
        print("2. Ver todos los descuentos")
        print("3. Ver descuento por ID")
        print("4. Buscar descuento")
        print("5. Modificar descuento")
        print("6. Eliminar descuento")
        print("7. Volver")

        opcion = input("Ingrese una opción (1-7): ")

        if opcion == "1":
            menuAgregarDescuento()
        elif opcion == "2":
            menuMostrarDescuentos()
        elif opcion == "3":
            menuMostrarDescuento()
        elif opcion == "4":
            menuBuscarDescuentos()
        elif opcion == "5":
            menuModificarDescuento()
        elif opcion == "6":
            menuEliminarDescuento()
        elif opcion == "7":
            print("\nVolviendo a Menu Principal")
            break    
        else:
            print("\nOpción inválida")

def menuAgregarDescuento():
    descripcion = pedirTexto("Ingrese la descripción: ")

    esMarca = elegirUnaOpcionDeDos("Elija como agrupar el descuento:", "Por Marca", "Por categoria")
    if esMarca is None:
        return
    elif esMarca:
        marca = pedirTexto("Ingrese marca: ")
        categoria = None
    else:
        marca = None
        categoria = pedirTexto("Ingrese categoria: ")

    esDosPorUno = elegirUnaOpcionDeDos("Elija el tipo de descuento:", "Dos por uno", "Porcentaje")
    if esDosPorUno is None:
        return
    elif esDosPorUno:
        tipo = TipoDescuento.DOS_POR_UNO
        valor = Decimal("0")
    else:
        tipo = TipoDescuento.PORCENTAJE
        valor = pedirPorcentaje("Ingrese el porcentaje: ")

    descuento = Descuento(None, descripcion, marca, categoria, tipo, valor)

    guardarDescuento(descuento.Descripcion, descuento.Marca, descuento.Categoria, descuento.Tipo, descuento.Valor)
    print("Descuento guardado.")

def menuMostrarDescuentos():
    descuentos = traerDescuentos()
    print("\nLista de Descuentos:")
    print("\nId - Descripcion - Por - Tipo")
    for desc in descuentos:
        desc.verDatos()

def menuMostrarDescuento():
    idDescuento = pedirEntero("Ingrese Id: ")
    descuento = traerDescuento(idDescuento)
    if descuento is None:
        print("No existe un descuento con ese id.")
    else:
        print("\nDatos de descuento:")
        print("\nId - Descripcion - Por - Tipo")
        descuento.verDatos()

def menuBuscarDescuentos():
    textoBusqueda = input("Ingrese Descripción, Marca o Categoría a buscar: ")
    descuentos = buscarDescuentos(textoBusqueda)
    if len(descuentos) == 0:
        print("\nNo se encontraron descuentos.")
    else:
        print("\nLista de descuentos encontrados:")
        print("\nId - Descripcion - Por - Tipo")
        for desc in descuentos:
            desc.verDatos()

def menuModificarDescuento():
    idDescuento = pedirEntero("Ingrese Id de descuento a modificar: ")
    descuento = traerDescuento(idDescuento)
    if descuento is None:
        print("No existe un descuento con ese id.")
    else:
        print("\nPresione Enter si no desea modificar el campo:")
        descripcion = input("Descripción (" + descuento.Descripcion + "):").strip()
        if descripcion != "":
            descuento.Descripcion = descripcion
        
        if descuento.Marca is None:
            categoria = input("Categoría (" + descuento.Categoria + "):").strip()
            if categoria != "":
                descuento.Categoria = categoria
        else:
            marca = input("Marca (" + descuento.Marca + "):").strip()
            if marca != "":
                descuento.Marca = marca

        if descuento.Tipo == TipoDescuento.PORCENTAJE:
            valor = pedirPorcentajeOVacio("Valor del Descuento (" + str(descuento.Valor) + "):")
            if valor != None:
                descuento.Valor = valor

        modificarDescuento(descuento.Id, descuento.Descripcion, descuento.Marca, descuento.Categoria, descuento.Valor)
        print("Descuento Modificado:")
        descuento.verDatos()


def menuEliminarDescuento():
    idDescuento = pedirEntero("Ingrese Id: ")
    descuento = traerDescuento(idDescuento)
    if descuento is None:
        print("\nNo existe un descuento con ese id.")
    else:
        eliminarDescuento(descuento.Id)
        print("\nDescuento Eliminado.")

