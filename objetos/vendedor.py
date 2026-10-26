from objetos.persona import Persona

class Vendedor(Persona):
    def __init__(self, pNombre, pApellido, pDni, pFechaNac, pLegajo, pCargo):
        super().__init__(pNombre, pApellido, pDni, pFechaNac)
        self.Legajo = pLegajo
        self.Cargo = pCargo