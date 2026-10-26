class Persona:
    def __init__(self, pId, pNombre, pApellido, pDni, pFechaNacimiento):
        self.Id = pId
        self.Nombre = pNombre
        self.Apellido = pApellido
        self.Dni = pDni
        self.FechaNacimiento = pFechaNacimiento
    def obtenerDatos(self):
        return str(self.Id) + " - " + self.Nombre + " - " + self.Apellido + " - " + self.Dni + " - " + str(self.FechaNacimiento)

    def verDatos(self):
        print(self.obtenerDatos())