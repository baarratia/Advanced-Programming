import matplotlib.pyplot as plt
from energia import obtener_funcion_energia, funcion_generadora
from generadora import generadora
lista_plantas = ["eolica", "solar", "nuclear"]
lista_tiempo = generadora()
for i in lista_plantas:
    if i == "eolica":
        color = "blue"
    elif i == "solar":
        color = "yellow"
    else:
        color = "red"
    lista_energia = funcion_generadora(i)
    print("Informacion de la planta {}".format(i))
    plt.scatter(<lista_tiempo>, <lista_energia>, c=color, edgecolors='None')
plt.show()