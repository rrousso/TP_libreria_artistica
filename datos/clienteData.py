from datos.db_config import conectar
from objetos.cliente import Cliente


def guardarCliente(pNom, pApe, pDni, pFechaNac):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clientes (nombre, apellido, dni, fecha_nacimiento, puntos_acumulados) values (%s,%s,%s,%s,0)",(pNom, pApe, pDni, pFechaNac))
    conn.commit()
    cursor.close()
    conn.close()

def traerClientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, apellido, dni, fecha_nacimiento, puntos_acumulados FROM clientes")
    filas = cursor.fetchall()
    cursor.close()
    conn.close()

    clientes = []
    for fila in filas:
        cliente = Cliente(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
        clientes.append(cliente)
    return clientes

def traerCliente(pIdCliente):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, apellido, dni, fecha_nacimiento, puntos_acumulados FROM clientes WHERE id = %s",(pIdCliente,))
    fila = cursor.fetchone()
    cursor.close()
    conn.close()

    if fila is None:
        return None
    return Cliente(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])

def buscarClientes(pTexto):
    conn = conectar()
    cursor = conn.cursor()
    textoCompleto = "%" + pTexto + "%"
    cursor.execute("SELECT id, nombre, apellido, dni, fecha_nacimiento, puntos_acumulados FROM clientes WHERE nombre LIKE %s OR apellido LIKE %s OR dni LIKE %s",(textoCompleto, textoCompleto, textoCompleto))
    filas = cursor.fetchall()
    cursor.close()
    conn.close()

    clientes = []
    for fila in filas:
        cliente = Cliente(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
        clientes.append(cliente)
    return clientes

def modificarCliente(pId, pNom, pApe, pDni, pFechaNac, pPuntos):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE clientes set nombre = %s, apellido = %s, dni = %s, fecha_nacimiento = %s, puntos_acumulados = %s WHERE id = %s",(pNom, pApe, pDni, pFechaNac, pPuntos, pId))
    conn.commit()
    cursor.close()
    conn.close()

def eliminarCliente(pIdCliente):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes where id = %s",(pIdCliente,))
    conn.commit()
    cursor.close()
    conn.close()
