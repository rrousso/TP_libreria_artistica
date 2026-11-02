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