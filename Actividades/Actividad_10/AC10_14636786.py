# debes definir la metaclase 'Meta' a continuacion
from inspect import istraceback


class Meta(type):
    def __new__(meta, nombre, clases_base, diccionario):

        def comprobar(atributo, valor):
            if isinstance(valor, atributo):
                    print("Estas seteando {}".format(valor))
                    diccionario[str(atributo)] = valor
            else:
                print('Error')
        for i in diccionario:
            comprobar(i, diccionario[i])
        return super().__new__(meta, nombre, clases_base, diccionario)


# debes definir las clases 'Person' y 'Company' a continuacion

class Person(metaclass=Meta):
    age = int
    name = str


class Company(metaclass=Meta):
    name = str
    stock_value = float
    employees = list

# El resto es para probar tu programa
if __name__ == '__main__':
    c = Company()
    c.name = 'Apple'
    c.stock_value = 125.78
    c.employees = ['Tim Cook', 'Kevin Lynch']

    print(c.name, c.stock_value, c.employees, sep=', ')

    p = Person()
    p.name = 'Karim'
    p.age = 'hola'
    # Esto debiese imprimir 'ERROR'

    print(p.name, p.age, sep=', ')
