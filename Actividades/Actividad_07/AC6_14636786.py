__author__ = 'Benja'
from Clase import *


arch = list(open('jugadores_sin_tildes.txt', 'r'))
funcion = lambda x: jugador(x.split(';'))
lista_jugadores = list(map(funcion,arch))

mismo_nombre = lambda lista: 'Benjamin' == lista.nombres.split(' ')[0] or 'Arratia' == lista.apellido_paterno
lista_iguales = list(filter(mismo_nombre, lista_jugadores))
print('Mismos nombres:')
for i in lista_iguales:
    print(i)
CYZ = lambda lista: 'Chile' == lista.pais and 'izquierdo' == lista.pie_habil
chileno_y_zurdo = list(filter(CYZ, lista_jugadores))
print('Chilenos y zurdos')
for i in chileno_y_zurdo:
    print(i)
edad = lambda lista: (lista.nombres, lista.apellido_paterno, lista.edad)
edades = list(map(edad, lista_jugadores))
print('Edades')
for i in edades:
    print(i)
Sub17 = lambda lista: lista.edad <= 17
nombre_apellido = lambda x: (x.nombres, x.apellido_paterno)

sub17 = list(map(nombre_apellido, list(filter(Sub17, lista_jugadores))))
print('sub17: ',sub17)