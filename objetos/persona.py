class Persona:
    def __init__(self, pNombre, pApellido, pDni, pFechaNacimiento):
        self.Nombre = pNombre
        self.Apellido = pApellido
        self.Dni = pDni
        self.FechaNacimiento = pFechaNacimiento
    def verDatos(self):
        print("Nombre: ",self.Nombre)
        print("Apellido: ",self.Apellido)
        print("DNI: ",self.Dni)
        print("Fecha de Nacimiento: ",self.FechaNacimiento)
        