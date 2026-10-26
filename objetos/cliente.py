from objetos.persona import Persona

class Cliente(Persona):
    def __init__(self, pNombre, pApellido, pDni, pFechaNac, pPuntosAcumulados):
        super().__init__(pNombre, pApellido, pDni, pFechaNac)
        self.PuntosAcumulados = pPuntosAcumulados
    def verDatos(self):
        super().verDatos()
        print("PuntosAcumulados: ",self.PuntosAcumulados)