from objetos.vendedor import Vendedor
from datos.vendedorData import guardarVendedor, traerVendedores, traerVendedor, buscarVendedores, eliminarVendedor, modificarVendedor, existeDniVendedor
from datos.ventaData import vendedorTieneVentas
from presentacion.validaciones import pedirEntero, pedirFecha

def menuVendedores():
    while True:
        print("\nMenú de operaciones de Vendedores:")
        print("1. Agregar vendedor")
        print("2. Ver todos los vendedores")
        print("3. Ver vendedor por ID")
        print("4. Buscar vendedores")
        print("5. Modificar vendedor")
        print("6. Eliminar vendedor")
        print("7. Volver")

        opcion = input("Ingrese una opción (1-7): ")

        if opcion == "1":
            menuAgregarVendedor()
        elif opcion == "2":
            menuMostrarVendedores()
        elif opcion == "3":
            menuMostrarVendedor()
        elif opcion == "4":
            menuBuscarVendedores()
        elif opcion == "5":
            menuModificarVendedor()
        elif opcion == "6":
            menuElminarVendedor()
        elif opcion == "7":
            print("\nVolviendo a Menu Principal")
            break    
        else:
            print("\nOpción inválida")

def menuAgregarVendedor():
    nombre = input("Ingrese el Nombre: ")
    apellido = input("Ingrese el Apellido: ")
    dni = input("Ingrese el Dni: ")
    fechaNac = pedirFecha("Ingrese fecha de nacimiento:")
    cargo = input("Ingrese el Cargo: ")
    vendedor = Vendedor(None, nombre, apellido, dni, fechaNac, cargo)
    guardarVendedor(vendedor.Nombre, vendedor.Apellido, vendedor.Dni, vendedor.FechaNacimiento, vendedor.Cargo)
    print("vendedor guardado.")

def menuMostrarVendedores():
    vendedores = traerVendedores()
    print("\nLista de vendedores:")
    print("\nId - Nombre - Apellido - DNI - Fecha Nacimiento - Cargo")
    for ven in vendedores:
        ven.verDatos()

def menuMostrarVendedor():
    idVendedor = pedirEntero("Ingrese Id: ")
    vendedor = traerVendedor(idVendedor)
    if vendedor is None:
        print("No existe un vendedor con ese id.")
    else:
        print("\nDatos de vendedor:")
        print("\nId - Nombre - Apellido - DNI - Fecha Nacimiento - Cargo")
        vendedor.verDatos()

def menuBuscarVendedores():
    idVendedor = input("Ingrese Nombre, apellido o DNI a buscar: ")
    vendedores = buscarVendedores(idVendedor)
    if len(vendedores) == 0:
        print("\nNo se encontraron vendedores.")
    else:
        print("\nLista de vendedores encontrados:")
        print("\nId - Nombre - Apellido - DNI - Fecha Nacimiento - Cargo")
        for ven in vendedores:
                ven.verDatos()

def menuModificarVendedor():
    idVendedor = input("Ingrese Id de usuario a modificar: ")
    vendedor = traerVendedor(idVendedor)
    if vendedor is None:
        print("No existe un vendedor con ese id.")
    else:
        print("\nPresione Enter si no desea modificar el campo:")
        nombre = input("Nombre (" + vendedor.Nombre + "):")
        if nombre != "":
            vendedor.Nombre = nombre

        apellido = input("Apellido (" + vendedor.Apellido + "):")
        if apellido != "":
            vendedor.Apellido = apellido
        
        dni = pedirEntero("Dni (" + vendedor.Dni + "):")
        
        if existeDniVendedor(dni):
            print("DNI ya existe en base de datos y debe ser un dato ùnico.")
            dni == ""
        if dni != "":
            vendedor.Dni = dni

        if vendedor.FechaNacimiento == None:
            textoFechaNac = "Sin Dato"
        else:
            textoFechaNac = vendedor.FechaNacimiento.strftime("%d/%m/%Y")

        fechaNac = pedirFecha("Fecha de nacimiento (" + textoFechaNac + "):")
        if fechaNac != None:
            vendedor.FechaNacimiento = fechaNac
        
        cargo = input("Cargo (" + vendedor.Cargo + "):")
        if cargo != "":
            vendedor.Cargo = cargo

        modificarVendedor(vendedor.Id, vendedor.Nombre, vendedor.Apellido, vendedor.Dni, vendedor.FechaNacimiento, vendedor.Cargo)
        print("Vendedor Modificado:" + vendedor.verDatos())


def menuEliminarVendedor():
    idVendedor = pedirEntero("Ingrese Id: ")
    vendedor = traerVendedor(idVendedor)
    if vendedor is None:
        print("No existe un vendedor con ese id.")
    elif vendedorTieneVentas(idVendedor):
        print("No se puede borrar: el vendedor tiene ventas registradas.")
    else:
        eliminarVendedor(vendedor.Id)
        print("\nVendedor Eliminado.")