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
        print("Id: ",self.Id)
        print("Descripcion: ",self.Descripcion)
        print("Precio: ",self.Precio)
        print("Stock: ",self.Stock)
        