from objetos.tipoDescuento import TipoDescuento

class Venta:
    def __init__(self, pId, pFecha, pCliente, pVendedor):
        self.Id = pId
        self.Fecha = pFecha
        self.Cliente = pCliente
        self.Vendedor = pVendedor
        self.Detalles = []
        self.Subtotal = 0
        self.Total = 0
    def verDatos(self):
        print("Id: ",self.Id)
        print("Fecha: ",self.Fecha)
        print("Cliente: ",self.Cliente.Nombre ,self.Cliente.Apellido)
        print("Vendedor: ",self.Vendedor.Nombre, self.Vendedor.Apellido)

        print("Detalles:")
        
        for detalle in self.Detalles:
            detalle.verDatos()

        print("Descuentos:")
        for descuento in self.Descuentos:
            descuento.verDatos()

    def calcularSubtotal(self):
        subtotal = 0
        for detalle in self.Detalles:
            subtotal += detalle.Cantidad * detalle.PrecioUnitario
        return subtotal

    def calcularTotal(self):
        total = 0
        for detalle in sef.Detalles:
            total += detalle.calcularSubtotal()
        return total
    