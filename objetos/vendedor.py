from objetos.persona import Persona

class Vendedor(Persona):
    def __init__(self, pNombre, pApellido, pDni, pFechaNac, pCargo):
        super().__init__(pNombre, pApellido, pDni, pFechaNac)
        self.Cargo = pCargo
    def verDatos(self):
        super().verDatos()
        print("Cargo: ",self.Cargo)
        