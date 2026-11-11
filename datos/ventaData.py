from datos.db_config import conectar
from objetos.venta import Venta

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