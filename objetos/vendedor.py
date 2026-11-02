from objetos.persona import Persona

class Vendedor(Persona):
    def __init__(self, pId, pNombre, pApellido, pDni, pFechaNac, pCargo):
        super().__init__(pId, pNombre, pApellido, pDni, pFechaNac)
        self.Cargo = pCargo
    def obtenerDatos(self):
            return str(self.Id) + " - " + self.Nombre + " - " + self.Apellido + " - " + self.Dni + " - " + str(self.FechaNacimiento) + " - " + str(self.Cargo) 
        