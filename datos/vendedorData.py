from datos.db_config import conectar
from objetos.vendedor import Vendedor

def guardarVendedor(pNom, pApe, pDni, pFechaNac, pCargo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO vendedores (nombre, apellido, dni, fecha_nacimiento, cargo) values (%s,%s,%s,%s,%s)",(pNom, pApe, pDni, pFechaNac, pCargo))
    conn.commit()
    cursor.close()
    conn.close()

def traerVendedores():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, apellido, dni, fecha_nacimiento, cargo FROM vendedores")
    filas = cursor.fetchall()
    cursor.close()
    conn.close()

    vendedores = []
    for fila in filas:
        vendedor = Vendedor(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
        vendedores.append(vendedor)
    return vendedores

def traerVendedor(pIdVendedor):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, apellido, dni, fecha_nacimiento, cargo FROM vendedores WHERE id = %s",(pIdVendedor,))
    fila = cursor.fetchone()
    cursor.close()
    conn.close()

    if fila is None:
        return None
    return Vendedor(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])

def buscarVendedores(pTexto):
    conn = conectar()
    cursor = conn.cursor()
    textoCompleto = "%" + pTexto + "%"
    cursor.execute("SELECT id, nombre, apellido, dni, fecha_nacimiento, cargo FROM vendedores WHERE nombre LIKE %s OR apellido LIKE %s OR dni LIKE %s",(textoCompleto, textoCompleto, textoCompleto))
    filas = cursor.fetchall()
    cursor.close()
    conn.close()

    vendedores = []
    for fila in filas:
        vendedor = Vendedor(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
        vendedores.append(vendedor)
    return vendedores

def modificarVendedor(pId, pNom, pApe, pDni, pFechaNac, pCargo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE vendedores set nombre = %s, apellido = %s, dni = %s, fecha_nacimiento = %s, cargo = %s WHERE id = %s",(pNom, pApe, pDni, pFechaNac, pCargo, pId))
    conn.commit()
    cursor.close()
    conn.close()

def eliminarVendedor(pIdVendedor):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM vendedores where id = %s",(pIdVendedor,))
    conn.commit()
    cursor.close()
    conn.close()

