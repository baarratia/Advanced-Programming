# Crea aquí tus decoradores
def guardar_instancias(clase):

    viejo_init = getattr(clase, '__init__')
    setattr(clase,'instancias',[])
    def _decorador(self,*args, **kwargs):
        viejo_init(self,*args, **kwargs)
        instancias.append(self)
    setattr(clase,'__init__',_decorador)
    return _decorador

#@comparar_por(atributo)
def cambiar_precio(function):
    def _mydecorator(*args, **kw):
        res = (((function(*args, **kw)-100)/1.19)*1/23)+100
        return res
    return _mydecorator
# Debes descomentar las tres líneas comentadas para probar tus decoradores

#@guardar_instancias
#  @comparar_por('diametro')
class Hamburguesa:

    def __init__(self, altura, diametro, cantidad_carnes):
        self.altura = altura
        self.diametro = diametro
        self.cantidad_carnes = cantidad_carnes

    def __repr__(self):
        return ('Hamburguesa de {0} cm de altura, '
                '{1} cm de diametro y '
                '{2} carnes').format(self.altura, self.diametro,
                                     self.cantidad_carnes)


@cambiar_precio
def precio_bruto_a_neto(precio_bruto):
    return (precio_bruto * 1.19 + 100)

if __name__ == "__main__":
    hamburguesa1 = Hamburguesa(10, 15, 2)
    hamburguesa2 = Hamburguesa(7, 10, 1)
    hamburguesa3 = Hamburguesa(10, 10, 2)

    '''print(hamburguesa2 > hamburguesa1)
    print(hamburguesa2 == hamburguesa3)
    print(hamburguesa1 < hamburguesa3)'''

    print(Hamburguesa.instancias)
    hamburguesa4 = Hamburguesa(12, 20, 4)
    print(Hamburguesa.instancias)

    print(precio_bruto_a_neto(2000))
