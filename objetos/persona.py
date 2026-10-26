class Persona:
    def __init__(self, pId, pNombre, pApellido, pDni, pFechaNacimiento):
        self.Id = pId
        self.Nombre = pNombre
        self.Apellido = pApellido
        self.Dni = pDni
        self.FechaNacimiento = pFechaNacimiento
    def verDatos(self):
        print("Id: ",self.Id)
        print("Nombre: ",self.Nombre)
        print("Apellido: ",self.Apellido)
        print("DNI: ",self.Dni)
        print("Fecha de Nacimiento: ",self.FechaNacimiento)
        