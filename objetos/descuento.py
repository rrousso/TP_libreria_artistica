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
        if self.Marca is None:
            agrupado = "categoría/" + self.Categoria
        else:
            agrupado = "marca/" + self.Marca

        if self.Tipo == TipoDescuento.DOS_POR_UNO:
            tipo = self.Tipo.name
        else:
            tipo = self.Tipo.name + ": " + str(self.Valor) + "%"
        print(str(self.Id) + " - " + self.Descripcion + " - " + agrupado + " - " + tipo)

    def calcularMonto(self, pCantidad, pPrecioUnitario):
        montoADescontar = 0
        if self.Tipo == TipoDescuento.DOS_POR_UNO:
            totalUnidades = pCantidad // 2
            montoADescontar = totalUnidades * pPrecioUnitario
        elif self.Tipo == TipoDescuento.PORCENTAJE:
            montoADescontar = pCantidad * pPrecioUnitario * self.Valor / 100
        return montoADescontar