from collections import deque
from paquete import Paquete
from botella import Botella

__author__ = 'patricio_lopez'


class Maquina:

    def procesar(self, linea_produccion_entrante):
        print("----------------------")
        print("La maquina {} comienza a trabajar.".format(
            self.__class__.__name__))


class Botellizamodulador(Maquina):

    def __init__(self):
        self.botellas_a_producir = 0

    def procesar(self, linea_produccion_entrante=None):
        super().procesar(linea_produccion_entrante)
        # ----------------
        lista_botellas=[]
        contador=0
        while botellas_a_producir !=0:
            if contador!=0 and contador%5==0:
                NB=Botella()
                NB.litros=lista_botellas[-1]*3
                lista_botellas.append(NB)
                botellas_a_producir-=1
                contador+=1
            if contador!=0 and contador%6==0:
                NB=Botella()
                NB.litros=(int(lista_botellas[-1].litros/2))+(lista_botellas[-2].litros*4)
                lista_botellas.append(NB)
                botellas_a_producir-=1
                contador+=1
            else:
                NB=Botella()
                lista_botellas.append(NB)
                botellas_a_producir-=1
                contador+=1
        # ----------------
        return lista_botellas


class LowFAT32(Maquina):

    def __init__(self):
        self.botellas_desechadas = []

    def desechar_botella(self, botella):
        self.botellas_desechadas.append(botella)

    def imprimir_botellas_desechadas(self):
        print("Se desecharon {} botellas".format(
            len(self.botellas_desechadas)))

    def procesar(self, linea_produccion_entrante):
        super().procesar(linea_produccion_entrante)
        # ----------------
        contador=0
        while len(linea_produccion_entrante)!=0:
            botella_actual=self.linea_produccion_entrante[contador]
            if botella_actual
                
        
        # Completar método
        # ----------------
        return None


class HashSoda9001(Maquina):

    def procesar(self, linea_produccion_entrante):
        super().procesar(linea_produccion_entrante)
        # ----------------
        # Completar método
        # ----------------
        return None


class PackageManager(Maquina):

    def procesar(self, linea_produccion_entrante):
        paquetes = deque()
        for pila in linea_produccion_entrante.values():
            paquete = Paquete()
            paquete.agregar_botellas(pila)
            paquetes.append(paquete)
        return paquetes


class Fabrica:

    def __init__(self):
        self.botellizamodulador = Botellizamodulador()
        self.lowFAT32 = LowFAT32()
        self.hashSoda9001 = HashSoda9001()
        self.packageManager = PackageManager()

    def producir(self, numero_botellas):
        self.botellizamodulador.botellas_a_producir = numero_botellas
        producto = None
        for maquina in [self.botellizamodulador,
                        self.lowFAT32,
                        self.hashSoda9001,
                        self.packageManager]:
            producto = maquina.procesar(producto)
        return producto


if __name__ == "__main__":

    numero_botellas = 423

    fabrica = Fabrica()
    output = fabrica.producir(numero_botellas)
    print("----------------------")
    print("Para {} botellas, se producen {} paquetes".format(
        numero_botellas, len(output)))
    for paquete in output:
        paquete.ver_contenido()
    print("----------------------")
