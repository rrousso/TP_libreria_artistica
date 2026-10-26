class DetalleVenta:
    def __init__(self, pProducto, pCantidad, pPrecioUnitario, pDescuentoAplicado):
        self.Producto = pProducto
        self.Cantidad = pCantidad
        self.PrecioUnitario = pPrecioUnitario
        self.DescuentoAplicado = pDescuentoAplicado

    def verDatos(self):
        print("Producto: ",self.Producto)
        print("Cantidad: ",self.Cantidad)
        print("PrecioUnitario: ",self.PrecioUnitario)
        print("DescuentoAplicado: ",self.DescuentoAplicado)

    def calcularSubtotal(self):
        return self.Cantidad * self.PrecioUnitario - self.DescuentoAplicado
