from objetos.persona import Persona

class Vendedor(Persona):
    def __init__(self, pId, pNombre, pApellido, pDni, pFechaNac, pCargo):
        super().__init__(pId, pNombre, pApellido, pDni, pFechaNac)
        self.Cargo = pCargo
    def verDatos(self):
        super().verDatos()
        print("Cargo: ",self.Cargo)
        