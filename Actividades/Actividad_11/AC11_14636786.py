__author__ = 'Benja'

from abc import ABCMeta, abstractmethod, abstractproperty
from math import sqrt

class Figura(metaclass= ABCMeta):

    def __init__(self, centro):
        self.centro = centro

    def __repr__(self):
        return '{0} - Perimetro: {1}, Area: {2}, Centro: {3}'.format(type(self), self.perimetro, self.area, self.centro)

    @property
    def Centro(self):
        return self.centro

    @Centro.setter
    def Centro(self, x):
        self.centro = x

    @abstractproperty
    def perimetro(self):
        pass

    @abstractproperty
    def area(self):
        pass

    def trasladar(self, x, y):
        self.centro = (self.centro[0] + x, self.centro[1] + y)

    @abstractmethod
    def crecer_area(self):
        pass

    @abstractmethod
    def crecer_perimetro(self):
        pass

class Rectangulo(Figura):
    def __init__(self, centro, largo, ancho):
        super().__init__(centro)
        self.largo = largo
        self.ancho = ancho

    @property
    def dimensiones(self):
        return 'Largo: {0} - Ancho: {1}'.format(self.largo, self.ancho)

    @dimensiones.setter
    def dimenciones(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    @property
    def perimetro(self):
        return self.largo*2 + self.ancho*2

    @property
    def area(self):
        return self.largo*self.ancho

    def crecer_area(self, num):
        self.ancho = self.ancho*sqrt(num)
        self.largo = self.largo*sqrt(num)

    def crecer_perimetro(self, num):
        self.ancho = self.ancho*(num/4)
        self.largo = self.largo*sqrt(num/4)




class Triangulo_Equilatero(Figura):

    def __init__(self, centro, lado):
        super().__init__(centro)
        self.lado = lado

    @property
    def Lado(self):
        return 'Lado: {0}'.format(self.lado)

    @Lado.setter
    def dimenciones(self, lado):
        self.lado = lado

    @property
    def perimetro(self):
        self.P = self.lado*3
        return self.P

    @property
    def area(self):
        self.A = ((self.lado**2)*sqrt(3))/4
        return self.A

    def crecer_area(self, num):
        self.lado = self.lado*sqrt(num)

    def crecer_perimetro(self, num):
        self.lado = self.lado + num/3


