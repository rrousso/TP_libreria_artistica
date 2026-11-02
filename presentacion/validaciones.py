from datetime import datetime, date

def pedirEntero(pMensaje):
    while True:
        texto = input(pMensaje)
        try:
            return int(texto)
        except ValueError:
            print("\nDebe ingresar un número.")

def pedirFecha(pMensaje):
    while True:
        texto = input(pMensaje + " (dd/mm/aaaa, Enter para omitir): ")
        if texto == "":
            return None
        try:
            fecha = datetime.strptime(texto, "%d/%m/%Y").date()
        except ValueError:
            print("\nFecha inválida, use el formato dd/mm/aaaa.")
            continue
        if fecha > date.today():
            print("\nLa fecha no puede ser futura.")
            continue
        return fecha