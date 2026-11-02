from datos.db_config import conectar
from objetos.detalleVenta import DetalleVenta

def productoTieneVentas(pIdProducto):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM detalle_ventas WHERE producto_id = %s",(pIdProducto,))
    fila = cursor.fetchone()
    cursor.close()
    conn.close()
    return fila[0] > 0