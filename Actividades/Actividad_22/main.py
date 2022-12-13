import threading
import time
import random
from sympy.utilities.iterables import generate_oriented_forest

__author__ = 'Jm'


class Godzilla(threading.Thread):

    def __init__(self, hp):
        super().__init__()
        self.hp = hp
        self.vivo = True


    def run(self):
        print("{} entra en escena...".format(threading.currentThread().getName()))
        while self.hp>0:
            time.sleep(8)
            self.atacar()
            if len(guerreros) == 0:
                print('Godzilla Gana!!!')
                self.vivo = False


    def atacado(self, guerrero):
        self.hp -= guerrero.ataque
        if self.hp <= 0:
            self.vivo = False
            print("El Godzilla MURIO!!")
        else:
            print(
                "El Godzilla ha sido atacado! El " + str(guerrero.ID) +
                " le ha hecho " + str(guerrero.ataque) + " de dano" +
                ". HP Godzilla " + str(self.hp))
            guerrero.atacado(int(guerrero.ataque / 4))

    def atacar(self):
        global guerreros
        for guerrero in guerreros:
            guerrero.atacado(3)




class Guerrero(threading.Thread):

    def __init__(self, Godzilla, velocidad, hp, ataque):
        super().__init__()
        self.vivo = True
        self.Godzilla = Godzilla
        self.velocidad = velocidad
        self.hp = hp
        self.ID = next(Guerrero.get_i)
        self.ataque = ataque

    def run(self):
        print("{} se une al combate...".format(threading.currentThread().getName()))
        while self.vivo and self.Godzilla.vivo:
            time.sleep(self.velocidad)
            self.Godzilla.atacado(self)
        guerreros.remove(self)

    def atacado(self, ataque):
        self.hp -= ataque
        print("El guerrero" + str(self.ID) +
              " ha sido danado!! HP " + str(self.hp))
        if self.hp <= 0:
            self.vivo = False
            print("El guerrero" + str(self.ID) + " ha muerto :( !!!")

    def id_():
        i = 0
        while True:
            yield i
            i += 1

    get_i = id_()


def sumar_guerrero():
    while godzilla.isAlive():
        time.sleep(random.randrange(10,30))
        nuevo = Guerrero(godzilla, random.randrange(4, 19), 30, 20)
        guerreros.append(nuevo)
        nuevo.setDaemon(True)
        nuevo.start()

def comprobar_muerte():
    if not godzilla.vivo:
        godzilla.stop()
        print('El daño generado a algunos guerreros, tras la muerte de godzilla, se debe a la caida del mismo...')

if __name__ == "__main__":
    print("Comenzo la Simulacion!")
    guerreros = []
    godzilla = Godzilla(500)
    generador = threading.Thread(name='Bonus', target=sumar_guerrero)
    generador.setDaemon(True)
    la_muerte = threading.Thread(name='Bonus', target=comprobar_muerte)
    la_muerte.setDaemon(True)
    for i in range(5):
        nuevo = Guerrero(godzilla, random.randrange(4, 19), 30, 20)
        guerreros.append(nuevo)
        nuevo.setDaemon(True)
    godzilla.start()
    for i in guerreros:
        i.start()
    generador.start()
    la_muerte.start()




