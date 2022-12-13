# -*- coding: utf-8 -*-
__author__ = 'Benja'
# código para el servidor que recibe datos y los envía de vuelta
import socket
import json
import threading


class Servidor(threading.Thread):
    def __init__(self):
        host = ''  # Symbolic name meaning all available interfaces
        port = 12345  # Arbitrary non-privileged port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(socket.gethostname() + ' iniciado, esperando usuario...')
        s.bind((host, port))
        s.listen(1)
        self.conn, addr = s.accept()
        print('Connected by', addr)

    def run(self):
        while True:
            data = json.loads(self.conn.recv(1024).decode('UTF-8'))
            print(data)
            if not data: break
            mensaje = input('{}: '.format(socket.gethostname()))
            message = json.dumps('{}: '.format(socket.gethostname()) + mensaje)
            self.conn.sendall(bytes(message, "UTF-8"))
        self.conn.close()
