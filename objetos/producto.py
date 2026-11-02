class Producto:
    def __init__(self, pId, pDescripcion, pMarca, pCategoria, pPresentacion, pUnidadesPorPaquete, pPrecio, pStock):
        self.Id = pId
        self.Descripcion = pDescripcion
        self.Marca = pMarca
        self.Categoria = pCategoria
        self.Presentacion = pPresentacion
        self.UnidadesPorPaquete = pUnidadesPorPaquete
        self.Precio = pPrecio
        self.Stock = pStock
    def verDatos(self):
        print(str(self.Id) + " - " + self.Descripcion + " - " + self.Precio + " - " + self.Stock)

    def verDatosCompletos(self):
            print(str(self.Id) + " - " + self.Descripcion + " - " + self.Marca + " - " + self.Categoria + " - " + self.Presentacion + " - " + str(self.UnidadesPorPaquete) + " - " + str(self.Precio) + " - " + str(self.Stock))
        