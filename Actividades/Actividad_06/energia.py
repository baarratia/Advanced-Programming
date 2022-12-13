from funciones import eolica, solar, nuclear
import math

print("Para las funciones 'obtener_funcion_energia' y 'funcion_generadora',\n"
      "parametro debe ser 'eolica', 'solar', o 'nuclear'")
listado_energia_eolica = []
listado_energia_solar = []
listado_energia_nuclear = []
k = 0


def obtener_funcion_energia(tipo_energia=None):
    """ Funcion obtener energia
    debe ingresar el parametro especificado en el print"""
    if tipo_energia != "eolica" and tipo_energia != "solar" and tipo_energia != "nuclear":
        print("Parametro incorrecto, debe ser 'eolica', 'solar' o 'nuclear'")
        return False
    elif tipo_energia == "eolica":
        return eolica
    elif tipo_energia == "solar":
        return solar
    elif tipo_energia == "nuclear":
        return nuclear


def funcion_generadora(tipo_energia):
    global listado_energia_eolica, listado_energia_nuclear, listado_energia_solar, k
    k += 1
    n = 6
    if tipo_energia != "eolica" and tipo_energia != "solar" and tipo_energia != "nuclear":
        print("Parametro incorrecto, debe ser 'eolica', 'solar' o 'nuclear'")
        return False
    elif tipo_energia == "eolica":
        while k <= 1440:
            q = ((eolica(k / n) + eolica(k)) / 2) * (1 / n)

        return eolica
    elif tipo_energia == "solar":
        return solar
    elif tipo_energia == "nuclear":
        return nuclear


def integrar(funcion, k, n):
    p = 0


a = obtener_funcion_energia('eolica')
print(a(600)