class Venta:
    def __init__(self, pId, pFecha, pCliente, pVendedor):
        self.Id = pId
        self.Fecha = pFecha
        self.Cliente = pCliente
        self.Vendedor = pVendedor
        self.Detalles = []
        self.Descuentos = []
    def verDatos(self):
        print("Id: ",self.Id)
        print("Fecha: ",self.Fecha)
        print("Cliente: ",self.Cliente.Nombre ,self.Cliente.Apellido)
        print("Vendedor: ",self.Vendedor.Nombre, self.Vendedor.Apellid)
        print("Detalles: ",self.Tipo.name)
        print("Descuentos: ",self.Valor)
        print("\nDetalles:")
        
        for detalle in self.Detalles:
            detalle.verDatos()

        print("\nDescuentos:")
        for descuento in self.Descuentos:
            descuento.verDatos()