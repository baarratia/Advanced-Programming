__author__ = 'Benja'


class jugador:
    jugadores = []

    def __init__(self, lista_datos):
        self.nombres = lista_datos[0]
        self.apellido_paterno = lista_datos[1]
        self.apellido_materno = lista_datos[2]
        self.pais = lista_datos[3]
        self.pie_habil = lista_datos[4]
        self.dia_nacimiento = lista_datos[5]
        self.mes_nacimiento = lista_datos[6]
        self.ano_nacimiento = int(lista_datos[7])
        self.goles = lista_datos[8]
        self.altura = lista_datos[9]
        self.peso = lista_datos[10].strip()
        self.edad = 2015-self.ano_nacimiento
        jugador.jugadores.append(self)

    def __str__(self):
        return 'nombre: {0}, apellido: {1}'.format(self.nombres, self.apellido_paterno)