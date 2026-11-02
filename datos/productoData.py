from datos.db_config import conectar
from objetos.producto import Producto


def guardarProducto(pDescripcion, pMarca, pCategoria, pPresentacion, punidades_por_paquete, pPrecio, pStock):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO productos (descripcion, marca, categoria, presentacion, unidades_por_paquete, precio, stock) values (%s,%s,%s,%s,%s,%s,%s)",(pDescripcion, pMarca, pCategoria, pPresentacion, punidades_por_paquete, pPrecio, pStock))
    conn.commit()
    cursor.close()
    conn.close()

def traerProductos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, descripcion, marca, categoria, presentacion, unidades_por_paquete, precio, stock FROM productos")
    filas = cursor.fetchall()
    cursor.close()
    conn.close()

    productos = []
    for fila in filas:
        producto = Producto(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7])
        productos.append(producto)
    return productos

def traerProducto(pIdProducto):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, descripcion, marca, categoria, presentacion, unidades_por_paquete, precio, stock FROM productos WHERE id = %s",(pIdProducto,))
    fila = cursor.fetchone()
    cursor.close()
    conn.close()

    if fila is None:
        return None
    return Producto(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7])

def buscarProductos(pTexto):
    conn = conectar()
    cursor = conn.cursor()
    textoCompleto = "%" + pTexto + "%"
    cursor.execute("SELECT id, descripcion, marca, categoria, presentacion, unidades_por_paquete, precio, stock FROM productos WHERE descripcion LIKE %s OR marca LIKE %s OR categoria LIKE %s OR presentacion LIKE %s",(textoCompleto, textoCompleto, textoCompleto, textoCompleto))
    filas = cursor.fetchall()
    cursor.close()
    conn.close()

    productos = []
    for fila in filas:
        producto = Producto(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7])
        productos.append(producto)
    return productos

def modificarProducto(pIdProducto, pDescripcion, pMarca, pCategoria, pPresentacion, punidades_por_paquete, pPrecio, pStock):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE productos set descripcion = %s, marca = %s, categoria = %s, presentacion = %s, unidades_por_paquete = %s, precio = %s, stock = %s WHERE id = %s",(pDescripcion, pMarca, pCategoria, pPresentacion, punidades_por_paquete, pPrecio, pStock, pIdProducto))
    conn.commit()
    cursor.close()
    conn.close()

def eliminarProducto(pIdProducto):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos where id = %s",(pIdProducto,))
    conn.commit()
    cursor.close()
    conn.close()