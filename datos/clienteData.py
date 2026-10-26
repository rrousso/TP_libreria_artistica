from datos.db_config import conectar
from objetos.cliente import Cliente


def guardarCliente(pNom, pApe, pDni, pFechaNac):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clientes (nombre, apellido, dni, fecha_nacimiento, puntos_acumulados) values (%s,%s,%s,%s)",(pNom, pApe, pDni, pFechaNac))
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
