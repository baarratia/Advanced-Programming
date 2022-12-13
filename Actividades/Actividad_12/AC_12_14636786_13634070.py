__author__ = 'Benja'
from collections import deque
from random import uniform

# Varaibles de estado: Las dos colas y sus contenidos

# Eventos relevantes para el control del tiempo: La entrada o salida de clientes en las colas

class cliente:
    def __init__(self):
        pass


class caja:
    def __init__(self):
        self.cola = deque()

    def llega(self):
        self.cola.append(cliente())

    def sale(self):
        self.cola.popleft()


class banco:
    def __init__(self, rango_llegada, rango_salida):
        self.caja1 = caja()
        self.caja2 = caja()
        self.rango_llegada = rango_llegada
        self.rango_salida = rango_salida
        self.evento_actual = None
        self.c_caja1 = 0
        self.c_caja2 = 0


    def cambiar_de_cola(self):

        if len(self.caja1.cola) < len(self.caja2.cola):
            self.caja1.cola.append(self.caja2.cola.pop())

        if len(self.caja2.cola) < len(self.caja1.cola):
            self.caja2.cola.append(self.caja1.cola.pop())


class Simulacion:
    def __init__(self, tiempo_maximo, rango_llegada, rango_salida):
        self.tiempo_maximo = tiempo_maximo
        self.banco = banco(rango_llegada, rango_salida)
        self.current_time = 0
        self.tiempo_total = 0

    def run(self):

        self.current_time += uniform(self.banco.rango_llegada)
        self.banco.caja1.llega()

        while True:
            arr_time_1 = uniform(self.banco.rango_llegada)
            arr_time_2 = uniform(self.banco.rango_llegada)
            exit_time_1 = uniform(self.rango_salida)
            exit_time_2 = uniform(self.rango_salida)

            self.current_time = min(arr_time_1, arr_time_2, exit_time_1, exit_time_2)
            self.tiempo_total += self.current_time

            if current_time == arr_time_1:
                self.banco.caja1.llega()
                print('llega una persona a la caja 1')
                self.c_caja1 += 1
            if current_time == arr_time_2:
                self.banco.caja2.llega()
                print('llega una persona a la caja 2')
                self.c_caja2 += 1
            if current_time == exit_time_1:
                self.banco.caja1.sale()
                print('sale una persona de la caja 1')
            if current_time == exit_time_2:
                self.banco.caja2.sale()
                print('sale una persona de la caja 2')

            arr_time_1 -= self.current_time
            arr_time_2 -= self.current_time
            exit_time_1 -= self.current_time
            exit_time_2 -= self.current_time

            for time in [arr_time_1, arr_time_2]:
                if time == 0:
                    time = uniform(self.banco.rango_llegada)
            for time in [exit_time_1, exit_time_2]:
                if time == 0:
                    time = uniform(self.rango_salida)

            if self.tiempo_total == self.tiempo_maximo:
                break

        print('Numero Personas caja 1: {0}\nNumero Personas caja 2: {1}\nTiempo de atencion promedio: {3}'.format(
            self.c_caja1), self.c_caja2, (self.c_caja1 + self.c_caja2) / self.tiempo_total)


s = Simulacion(80, (1,3),(1,10))
s.run()
