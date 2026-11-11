class Venta:
    def __init__(self, pId, pFecha, pCliente, pVendedor):
        self.Id = pId
        self.Fecha = pFecha
        self.Cliente = pCliente
        self.Vendedor = pVendedor
        self.Detalles = []
        self.Subtotal = 0
        self.Total = 0

    def verDatosSinID(self):
        print("\nFecha: ",self.Fecha)
        print("Cliente: ",self.Cliente.Nombre ,self.Cliente.Apellido)
        print("Vendedor: ",self.Vendedor.Nombre, self.Vendedor.Apellido)
        print("Detalles(Descripción - Cantidad - Precio X Unidad - Descuento Aplicado):")

        for detalle in self.Detalles:
            detalle.verDatos()
            
        print(f"Subtotal: {self.Subtotal:.2f}")
        print(f"Total: {self.Total:.2f}")

    def verDatos(self):
        print("\nID: ",self.Id)
        print("Fecha: ",self.Fecha)
        print("Cliente: ",self.Cliente.Nombre ,self.Cliente.Apellido)
        print("Vendedor: ",self.Vendedor.Nombre, self.Vendedor.Apellido)
        print("Detalles(Descripción - Cantidad - Precio X Unidad - Descuento Aplicado):")

        for detalle in self.Detalles:
            detalle.verDatos()
            
        print(f"Subtotal: {self.Subtotal:.2f}")
        print(f"Total: {self.Total:.2f}")

    def calcularSubtotal(self):
        subtotal = 0
        for detalle in self.Detalles:
            subtotal += detalle.Cantidad * detalle.PrecioUnitario
        return subtotal

    def calcularTotal(self):
        total = 0
        for detalle in self.Detalles:
            total += detalle.calcularTotal()
        return total
    