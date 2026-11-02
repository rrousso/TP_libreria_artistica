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
    cursor.execute("SELECT COUNT(*) FROM ventas WHERE dni = %s",(pIdVendedor,))
    fila = cursor.fetchone()
    cursor.close()
    conn.close()
    return fila[0] > 0