from datos.db_config import conectar
from objetos.descuento import Descuento
from objetos.tipoDescuento import TipoDescuento

def guardarDescuento(pDescripcion, pMarca, pCategoria, pTipo, pValor):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO descuentos (descripcion, marca, categoria, tipo, valor) values (%s,%s,%s,%s,%s)",(pDescripcion, pMarca, pCategoria, pTipo.value, pValor))
    conn.commit()
    cursor.close()
    conn.close()

def traerDescuentos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, descripcion, marca, categoria, tipo, valor FROM descuentos")
    filas = cursor.fetchall()
    cursor.close()
    conn.close()

    descuentos = []
    for fila in filas:
        descuento = Descuento(fila[0], fila[1], fila[2], fila[3], TipoDescuento(fila[4]), fila[5])
        descuentos.append(descuento)
    return descuentos

def traerDescuento(pIdDescuento):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, descripcion, marca, categoria, tipo, valor FROM descuentos WHERE id = %s",(pIdDescuento,))
    fila = cursor.fetchone()
    cursor.close()
    conn.close()

    if fila is None:
        return None
    return Descuento(fila[0], fila[1], fila[2], fila[3], TipoDescuento(fila[4]), fila[5])

def buscarDescuentos(pTexto):
    conn = conectar()
    cursor = conn.cursor()
    textoCompleto = "%" + pTexto + "%"
    cursor.execute("SELECT id, descripcion, marca, categoria, tipo, valor FROM descuentos WHERE descripcion LIKE %s OR marca LIKE %s OR categoria LIKE %s",(textoCompleto, textoCompleto, textoCompleto))
    filas = cursor.fetchall()
    cursor.close()
    conn.close()

    descuentos = []
    for fila in filas:
        descuento = Descuento(fila[0], fila[1], fila[2], fila[3], TipoDescuento(fila[4]), fila[5])
        descuentos.append(descuento)
    return descuentos

def modificarDescuento(pIdDescuento, pDescripcion, pMarca, pCategoria, pValor):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE descuentos set descripcion = %s, marca = %s, categoria = %s, valor = %s WHERE id = %s",(pDescripcion, pMarca, pCategoria, pValor, pIdDescuento))
    conn.commit()
    cursor.close()
    conn.close()

def eliminarDescuento(pIdDescuento):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM descuentos where id = %s",(pIdDescuento,))
    conn.commit()
    cursor.close()
    conn.close()