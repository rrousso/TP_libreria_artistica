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
        print("Categoria: ",self.Categoria)
        print("Tipo: ",self.Tipo)
        print("Valor: ",self.Valor)
        