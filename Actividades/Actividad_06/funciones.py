__author__ = 'Benja'

import math


def eolica(t=None):
    if t == None:
        t = float(input('Ingrese el tiempo de trabajo de la planta eolica:'))
    if t < 720:
        E = ((math.sin(t)) / 3) + ((math.sin(3 * t)) / 3) + 1 / 2
        return E
    if t >= 720:
        E = 1
        return E


def solar(t=None):
    if t == None:
        t = float(input('Ingrese el tiempo de trabajo de la planta solar:'))
    if t < 360 or t >= 1080:
        E = 1
        return E
    if t < 720 and t >= 360:
        E = (math.cos(t)) ^ 2
        return E
    elif t < 1080 and t >= 720:
        E = t / 360
        return E
    else:
        False


def nuclear(t=None):
    if t == None:
        t = float(input('Ingrese el tiempo de trabajo de la planta nuclear:'))
    E = 22 * math.exp(-0.05 * t)
    return E

