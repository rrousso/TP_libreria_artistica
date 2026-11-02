from objetos.cliente import Cliente
from datos.clienteData import guardarCliente, traerClientes, traerCliente, buscarClientes, modificarCliente, eliminarCliente
from datos.ventaData import clienteTieneVentas
from presentacion.validaciones import pedirEntero, pedirFecha

def menuClientes():
    while True:
        print("\nMenú de operaciones de Clientes:")
        print("1. Agregar cliente")
        print("2. Ver todos los clientes")
        print("3. Ver cliente por ID")
        print("4. Buscar clientes")
        print("5. Modificar cliente")
        print("6. Eliminar cliente")
        print("7. Volver")

        opcion = input("Ingrese una opción (1-7): ")

        if opcion == "1":
            menuAgregarCliente()
        elif opcion == "2":
            menuMostrarClientes()
        elif opcion == "3":
            menuMostrarCliente()
        elif opcion == "4":
            menuBuscarClientes()
        elif opcion == "5":
            menuModificarCliente()
        elif opcion == "6":
            menuElminarCliente()
        elif opcion == "7":
            print("\nVolviendo a Menu Principal")
            break    
        else:
            print("\nOpción inválida")

def menuAgregarCliente():
    nombre = input("Ingrese el Nombre: ")
    apellido = input("Ingrese el Apellido: ")
    dni = input("Ingrese el Dni: ")
    fechaNac = pedirFecha("Ingrese fecha de nacimiento:")
    cliente = Cliente(None, nombre, apellido, dni, fechaNac, 0)
    guardarCliente(cliente.Nombre, cliente.Apellido, cliente.Dni, cliente.FechaNacimiento)
    print("Cliente guardado.")

def menuMostrarClientes():
    clientes = traerClientes()
    print("\nLista de Clientes:")
    print("\nId - Nombre - Apellido - DNI - Fecha Nacimiento - Puntos Acumulados")
    for cli in clientes:
        cli.verDatos()

def menuMostrarCliente():
    idCliente = pedirEntero("Ingrese Id: ")
    cliente = traerCliente(idCliente)
    if cliente is None:
        print("No existe un cliente con ese id.")
    else:
        print("\nDatos de Cliente:")
        print("\nId - Nombre - Apellido - DNI - Fecha Nacimiento - Puntos Acumulados")
        cliente.verDatos()

def menuBuscarClientes():
    idCliente = input("Ingrese Nombre, apellido o DNI a buscar: ")
    clientes = buscarClientes(idCliente)
    if len(clientes) == 0:
        print("\nNo se encontraron clientes.")
    else:
        print("\nLista de Clientes encontrados:")
        print("\nId - Nombre - Apellido - DNI - Fecha Nacimiento - Puntos Acumulados")
        for cli in clientes:
                cli.verDatos()

def menuModificarCliente():
    idCliente = input("Ingrese Id de usuario a modificar: ")
    cliente = traerCliente(idCliente)
    if cliente is None:
        print("No existe un cliente con ese id.")
    else:
        print("\nPresione Enter si no desea modificar el campo:")
        nombre = input("Nombre (" + cliente.Nombre + "):")
        if nombre != "":
            cliente.Nombre = nombre

        apellido = input("Apellido (" + cliente.Apellido + "):")
        if apellido != "":
            cliente.Apellido = apellido

        dni = input("Dni (" + cliente.Dni + "):")
        if dni != "":
            cliente.Dni = dni

        fechaNac = pedirFecha("Fecha de nacimiento (" + cliente.FechaNacimiento.strftime("%d/%m/%Y") + "):")
        if fechaNac != None:
            cliente.FechaNacimiento = fechaNac
        
        puntos = input("PuntosAcumulados (" + str(cliente.PuntosAcumulados) + "):")
        if puntos != "":
            cliente.PuntosAcumulados = puntos

        modificarCliente(cliente.Id, cliente.Nombre, cliente.Apellido, cliente.Dni, cliente.FechaNacimiento, cliente.PuntosAcumulados)


def menuElminarCliente():
    idCliente = pedirEntero("Ingrese Id: ")
    cliente = traerCliente(idCliente)
    if cliente is None:
        print("No existe un cliente con ese id.")
    elif clienteTieneVentas(idCliente):
        print("No se puede borrar: el cliente tiene ventas registradas.")
    else:
        eliminarCliente(cliente.Id)
        print("\nCliente Eliminado.")
