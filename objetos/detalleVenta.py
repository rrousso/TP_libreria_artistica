class DetalleVenta:
    def __init__(self, pProducto, pCantidad, pPrecioUnitario, pDescuentoAplicado):
        self.Producto = pProducto
        self.Cantidad = pCantidad
        self.PrecioUnitario = pPrecioUnitario
        self.DescuentoAplicado = pDescuentoAplicado

    def verDatos(self):
        print("Producto: ",self.Producto.Descripcion)
        print("Cantidad: ",self.Cantidad)
        print("PrecioUnitario: ",self.PrecioUnitario)
        print("DescuentoAplicado: ",self.DescuentoAplicado)

    def calcularSubtotal(self):
        return self.Cantidad * self.PrecioUnitario - self.DescuentoAplicado

    def aplicarMejorDescuento(self, pDescuentos):
        mejor = 0
        for descuento in pDescuentos:
            monto = descuento.calcularMonto(self.Cantidad, self.PrecioUnitario)
            if monto > mejor:
                mejor = monto
        self.DescuentoAplicado = mejor
