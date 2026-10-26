from objetos.tipoDescuento import TipoDescuento

class Descuento:
    def __init__(self, pId, pDescripcion, pMarca, pCategoria, pTipo, pValor):
        self.Id = pId
        self.Descripcion = pDescripcion
        self.Marca = pMarca
        self.Categoria = pCategoria
        self.Tipo = pTipo
        self.Valor = pValor
    def verDatos(self):
        print("Id: ",self.Id)
        print("Descripcion: ",self.Descripcion)
        print("Marca: ",self.Marca)
        print("Categoria: ",self.Categoria)
        print("Tipo: ",self.Tipo.name)
        print("Valor: ",self.Valor)

    def calcularMonto(self, pCantidad, pPrecioUnitario):
        montoADescontar = 0
        if self.Tipo == "DOS_POR_UNO":
            totalUnidades = pCantidad // 2
            montoADescontar = totalUnidades * pPrecioUnitario
        elif self.Tipo == "PORCENTAJE":
            montoADescontar = pCantidad * pPrecioUnitario * self.Valor / 100
        return montoADescontar