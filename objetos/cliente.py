from objetos.persona import Persona

class Cliente(Persona):
    def __init__(self, pId, pNombre, pApellido, pDni, pFechaNac, pPuntosAcumulados):
        super().__init__(pId, pNombre, pApellido, pDni, pFechaNac)
        self.PuntosAcumulados = pPuntosAcumulados
    def obtenerDatos(self):
        return super().obtenerDatos() + " - " + str(self.PuntosAcumulados) 