__author__ = 'Benja'
import simpy
import random


class cliente:
    c = 0

    def __init__(self, Banco, env):
        self.nombre = 'Cliente ' + str(c)
        self.paciencia = random.uniform(50, 90)
        c += 1
        largos = []
        for i in Banco.cajas: # No se si funcione esto, pero es para que entre a la caja con menos cola
            largos.append(len(i.queue))
        num = min[largos]
        x = largos.index(num)
        yield (Banco.cajas[x]).request()

    @property
    def sale(self):
        self.paciencia -= env.now
        if self.paciencia <= 0:
            pass

class caja:
    def __init__(self, env, nombre):
        self.env = env
        self.nombre = nombre
        self.clientes = simpy.Resource(env)



class Banco:
    def __init__(self, env, numero_de_cajas):
        self.env = env
        self.cajas = []
        for i in range(numero_de_cajas):
            self.cajas.append(caja(env, i))

    def generador_clientes(self, env):
        while True:
            env.process(cliente(self, env))
            yield env.timeout(round(random.expovariate((1 / 10) + 0.5)))
            print('{0} llega al banco en {1:.2f}.'.format(cliente.nombre, env.now))
            yield env.timeout(round(random.expovariate((1 / 15) + 0.5)))
            print('{0} deja el banco en {1:.2f}.'.format(cliente.nombre, env.now))


env = simpy.Environment
x = Banco(env, 3)
env.run(until=10)