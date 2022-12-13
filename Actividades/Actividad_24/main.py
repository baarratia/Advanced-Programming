# -*- coding: utf-8 -*-
__author__ = 'Benja'
from Servidor import *
from Cliente import *

def Interfaz():
    while True:
        print('\n             Bienvenidos al Chat de Guguul :D\n'
              '\n(1)    Actuar como Servidor\n(2)    Actuar como cliente\n(0)    Salir\n')
        c = ':c'
        while c != ':)':
            try:
                num = int(input('Ingrese el número correspondiente a lo que desea hacer:  ').strip())
                if num < 0 or num > 2:
                    raise ValueError
                else:
                    c = ':)'
            except:
                print('Dato no valido, intente nuevamente...\n')
        if num == 0:
            print('\nHasta pronto!!!')
            break
        if num == 1:
            serv = Servidor()
            serv.run()

        if num == 2:
            print('\nCliente')
            port = 12345
            host = "Benja"
            MAX_SIZE = 1000
            nombre = "Antonio"

            c = Cliente(port, host, MAX_SIZE, nombre)
            c.conectar()
            mensaje = "hola"
            while mensaje != "":
                mensaje = input("{}: ".format(c.usuario))
                c.enviar_mensaje(mensaje)
                c.recibir_mensaje()
            c.desconectar()

Interfaz()