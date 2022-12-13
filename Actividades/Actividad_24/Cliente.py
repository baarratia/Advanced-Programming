#cliente que envía los datos json, poner atención en la serialización y transformación a bytes.
import socket
import sys
import json


class Cliente:
    def __init__(self, port, host, MAX_SIZE, usuario):
        self.MAX_SIZE = MAX_SIZE
        self.server_host = host
        self.port = port
        self.usuario = usuario

    def conectar(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            print("Conectando....")
            self.s.connect((self.server_host, self.port))
            print("Conectado")
        except:
            print("Error: No pudo conectarse")
            sys.exit()
            
    def enviar_mensaje(self, mensaje):
        message = json.dumps("{}: {}".format(self.usuario,mensaje))
        self.s.sendall(bytes(message, "UTF-8"))

    def recibir_mensaje(self):
        data = json.loads(self.s.recv(self.MAX_SIZE).decode('UTF-8'))
        print(data)

    def desconectar(self):
        self.s.close()


    
