from datos.db_config import conectar
from objetos.venta import Venta
from objetos.cliente import Cliente
from objetos.vendedor import Vendedor
from objetos.detalleVenta import DetalleVenta
from objetos.producto import Producto

def clienteTieneVentas(pIdCliente):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM ventas WHERE cliente_id = %s",(pIdCliente,))
    fila = cursor.fetchone()
    cursor.close()
    conn.close()
    return fila[0] > 0

def vendedorTieneVentas(pIdVendedor):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM ventas WHERE vendedor_id = %s",(pIdVendedor,))
    fila = cursor.fetchone()
    cursor.close()
    conn.close()
    return fila[0] > 0

def guardarVenta(pVenta):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO ventas (fecha, cliente_id, vendedor_id, subtotal, total) values (%s,%s,%s,%s,%s)",(pVenta.Fecha, pVenta.Cliente.Id, pVenta.Vendedor.Id, pVenta.Subtotal, pVenta.Total))
        idVenta = cursor.lastrowid
        for detalle in pVenta.Detalles:
            cursor.execute("INSERT INTO detalle_ventas (producto_id, venta_id, cantidad, precio_unitario, descuento_aplicado) values (%s,%s,%s,%s,%s)",(detalle.Producto.Id, idVenta, detalle.Cantidad, detalle.PrecioUnitario, detalle.DescuentoAplicado))
            cursor.execute("UPDATE productos set stock = stock - %s WHERE id = %s",(detalle.Cantidad,detalle.Producto.Id))
        conn.commit()
        return idVenta
    except Exception:
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()

def traerVentas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, fecha, cliente_id, vendedor_id, subtotal, total FROM ventas")
    filas = cursor.fetchall()
    
    ventas = []
    for fila in filas:
        venta = armarVenta(cursor, fila)
        ventas.append(venta)

    cursor.close()
    conn.close()    
    return ventas

def traerVentaPorFactura(pId):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, fecha, cliente_id, vendedor_id, subtotal, total FROM ventas WHERE id = %s",(pId,))
    fila = cursor.fetchone()
    venta = armarVenta(cursor, fila)
    cursor.close()
    conn.close()    
    return venta

def traerVentasPorCliente(pDni):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM clientes WHERE dni = %s",(pDni,))
    filaCliente = cursor.fetchone()
    if filaCliente is None:
        cursor.close()
        conn.close()   
        return None    
    cursor.execute("SELECT id, fecha, cliente_id, vendedor_id, subtotal, total FROM ventas WHERE cliente_id = %s",(filaCliente[0],))
    filas = cursor.fetchall()
    ventas = []
    for fila in filas:
        venta = armarVenta(cursor, fila)
        ventas.append(venta)
    cursor.close()
    conn.close()    
    return ventas

def armarVenta(pCursor,pFila):
    if pFila is None:
        return None
    pCursor.execute("SELECT id, nombre, apellido, dni, fecha_nacimiento, puntos_acumulados FROM clientes WHERE id = %s",(pFila[2],))
    filaCliente = pCursor.fetchone()

    pCursor.execute("SELECT id, nombre, apellido, dni, fecha_nacimiento, cargo FROM vendedores WHERE id = %s",(pFila[3],))
    filaVendedor = pCursor.fetchone()

    pCursor.execute("SELECT producto_id, venta_id, cantidad, precio_unitario, descuento_aplicado FROM detalle_ventas WHERE venta_id = %s", (pFila[0],))
    filasDetalles = pCursor.fetchall()        

    cliente = Cliente(filaCliente[0], filaCliente[1], filaCliente[2], filaCliente[3], filaCliente[4], filaCliente[5])
    vendedor = Vendedor(filaVendedor[0], filaVendedor[1], filaVendedor[2], filaVendedor[3], filaVendedor[4], filaVendedor[5])

    venta = Venta(pFila[0], pFila[1], cliente, vendedor)

    for filaDetalle in filasDetalles:
            pCursor.execute("SELECT id, descripcion, marca, categoria, presentacion, unidades_por_paquete, precio, stock FROM productos WHERE id = %s",(filaDetalle[0],))
            filaProducto = pCursor.fetchone()
            producto = Producto(filaProducto[0], filaProducto[1], filaProducto[2], filaProducto[3], filaProducto[4], filaProducto[5], filaProducto[6], filaProducto[7])
        
            detalle = DetalleVenta(producto, filaDetalle[2], filaDetalle[3], filaDetalle[4])    
            venta.Detalles.append(detalle)
    
    venta.Subtotal = pFila[4]
    venta.Total = pFila[5]
    return venta

def eliminarVentaPorFactura(pId):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT producto_id, cantidad FROM detalle_ventas WHERE venta_id = %s", (pId,))
        filasDetalles = cursor.fetchall()        

        for filaDetalle in filasDetalles:
            cursor.execute("UPDATE productos set stock = stock + %s WHERE id = %s",(filaDetalle[1],filaDetalle[0]))

        cursor.execute("DELETE FROM ventas where id = %s",(pId,))
        conn.commit()
    except Exception:
        conn.rollback()
        raise    
    finally:
        cursor.close()
        conn.close()