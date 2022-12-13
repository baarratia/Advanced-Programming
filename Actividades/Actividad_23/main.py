__author__ = ['Bastian','Jm']
import threading
import time
import random

class MegaGodzilla(threading.Thread):

    def __init__(self, hp):
        super().__init__()
        self.hp = hp

    @property
    def vivo(self):
        if self.hp > 0:
            return True
        return False


    def atacado(self, soldado):
        self.hp -= soldado.ataque
        if not self.vivo:
            print("MegaGodzilla ha muerto!!")
        else:
            print(
                "Mega-Godzilla ha sido atacado! El soldado le ha hecho " + str(
                    soldado.ataque) + " de dano" +
                ". HP Godzilla " + str(self.hp))
            soldado.atacado(int(soldado.ataque / 4))

    def atacar(self):
        global soldados
        choice = random.choice(('normal', 'Ultimate Mega-Godzilla Super Attack'))
        print("MegaGodzilla usa su {}!!".format(choice))
        for soldado in soldados:
            if soldado.vivo:
                if choice == 'normal':
                        soldado.atacado(3)
                else:
                    soldado.atacado(6)
                    if soldado.vivo:
                        print("Soldado {} es paralizado!".format(soldado.ID))
                        soldado.parar()
        print('Es super efectivo!')

    def run(self):
        while self.vivo:
            time.sleep(random.randint(3, 6))
            self.atacar()
            if len(soldados) == 0:
                print('Godzilla Gana!!!')
                break


class Soldado(threading.Thread):

    lock = threading.Lock()

    def __init__(self, MegaGodzilla, velocidad, hp, ataque):
        super().__init__()
        self.MegaGodzilla = MegaGodzilla
        self.velocidad = velocidad
        self.hp = hp
        self.ID = next(Soldado.get_i)
        self.ataque = ataque

    @property
    def vivo(self):
        if self.hp > 0:
            return True
        return False


    def atacado(self, ataque):
        self.hp -= ataque
        print("El soldado" + str(self.ID) +
              " ha sido danado!!  HP " + str(self.hp))
        if not self.vivo:
            print("El soldado" + str(self.ID) + " ha muerto :( !!!")

    def run(self):
        print("{} se une al combate...".format(threading.currentThread().getName()))
        self.paralizado = False
        while self.vivo and self.MegaGodzilla.vivo:
            if not self.paralizado:
                time.sleep(self.velocidad)
                with Soldado.lock:
                    time.sleep(random.randint(1, 3))
                    self.MegaGodzilla.atacado(self)
            else:
                time.sleep(10)
                self.paralizado = False
            if not self.vivo:
                soldados.remove(self)
        try:
            soldados.remove(self)
        except:
            pass

    def parar(self):
        self.paralizado = True

    def id_():
        i = 0
        while True:
            yield i
            i += 1

    get_i = id_()


if __name__ == "__main__":
    print("Comenzo la Simulacion!")
    soldados = []
    godzilla = MegaGodzilla(500)
    godzilla.start()
    for i in range(5):
        nuevo = Soldado(godzilla, random.randrange(4, 19), 30, 20)
        soldados.append(nuevo)
        nuevo.setDaemon(True)
        nuevo.start()

