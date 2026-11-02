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

def productoTieneVentas(pIdProducto):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM productos WHERE producto_id = %s",(pIdProducto,))
    fila = cursor.fetchone()
    cursor.close()
    conn.close()
    return fila[0] > 0