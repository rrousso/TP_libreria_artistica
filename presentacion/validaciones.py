from datetime import datetime, date
from decimal import Decimal, InvalidOperation


def pedirTexto(pMensaje):
    while True:
        texto = input(pMensaje).strip()
        if texto != "":
            return texto
        print("\nEl campo no puede estar vacío.")

def pedirDecimal(pMensaje):
    while True:
        texto = input(pMensaje)
        try:
            valor = Decimal(texto.replace(",", "."))
        except InvalidOperation:
            print("\nDebe ingresar un número.")
            continue
        if valor < Decimal("0"):
            print("\nEl número no puede ser negativo.")
            continue
        return valor  

def pedirDecimalOVacio(pMensaje):
    while True:
        texto = input(pMensaje)
        if texto == "":
            return None
        try:
            valor = Decimal(texto.replace(",", "."))
        except InvalidOperation:
            print("\nDebe ingresar un número.")
            continue
        if valor < Decimal("0"):
            print("\nEl número no puede ser negativo.")
            continue
        return valor  

def pedirEntero(pMensaje):
    while True:
        texto = input(pMensaje)
        try:
            valor = int(texto)
        except ValueError:
            print("\nDebe ingresar un número.")
            continue
        if valor < 0:
            print("\nEl número no puede ser negativo.")
            continue
        return valor  

def pedirEnteroOVacio(pMensaje):
    while True:
        texto = input(pMensaje)
        if texto == "":
            return None
        try:
            valor = int(texto)
        except ValueError:
            print("\nDebe ingresar un número.")
            continue
        if valor < 0:
            print("\nEl número no puede ser negativo.")
            continue
        return valor  
    
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

def elegirUnaOpcionDeDos(pMensaje, pOpcionUno, pOpcionDos):
    while True:
        print("\n" + pMensaje )
        print("1. " + pOpcionUno)
        print("2. " + pOpcionDos)
        print("3. Volver")

        opcion = input("Ingrese una opción (1-3): ")

        if opcion == "1":
            return True
        elif opcion == "2":
            return False
        elif opcion == "3":
            print("\nVolviendo a Menu Anterior")
            return    
        else:
            print("\nOpción inválida")

def pedirPorcentaje(pMensaje):
    while True:
        valor = pedirDecimal(pMensaje)
        if valor > Decimal("100"):
            print("\nEl número no puede superar 100.")
            continue
        return valor

def pedirPorcentajeOVacio(pMensaje):
    while True:
        valor = pedirDecimalOVacio(pMensaje)
        if valor is None:
            return None
        elif valor > Decimal("100"):
            print("\nEl número no puede superar 100.")
            continue
        return valor
