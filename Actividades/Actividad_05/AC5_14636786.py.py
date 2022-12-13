from estaciones_metro import Direccion, MapaMetro, Estacion
from Arboles import Arbol

# Retornar true si existe un camino desde la estacion_origen a
# la estacion_destino, false en caso contrario.
# Solo puede controlar las variables estacion_origen y
# estacion_destino , no el mapa.

# Por ejemplo puedes hacer:
#   estacion_origen.izquierda.izquierda


def camino(estacion_origen, estacion_destino):
    Recorridos=Arbol()
    estacion_actual=estacion_origen
    Recorridos.agregar_nodo(estacion_actual)
    while estacion_actual.derecha==None and estacion_actual.izquierda==None and estacion_actual.arriba==None and estacion_actual.abajo==None:

        if estacion_actual==estacion_destino:
            return True

        elif estacion_actual.derecha!=None:
            estacion_actual==estacion_actual.derecha
            Recorridos.agregar_nodo(estacion_actual)
            camino(estacion_actual, estacion_destino)

        elif estacion_actual.izquierda!=None:
            estacion_actual==estacion_actual.izquierda
            Recorridos.agregar_nodo(estacion_actual)
            camino(estacion_actual, estacion_destino)

        elif estacion_actual.arriba!=None:
            estacion_actual==estacion_actual.arriba
            Recorridos.agregar_nodo(estacion_actual)
            camino(estacion_actual, estacion_destino)


        elif estacion_actual.abajo!=None:
            estacion_actual==estacion_actual.derecha
            Recorridos.agregar_nodo(estacion_actual)
            camino(estacion_actual, estacion_destino)
        break
    if estacion_actual==estacion_destino:
        return True
    else:
        return False




if __name__ == "__main__":
    mapa = MapaMetro.mapa_de_ejemplo()
    print(camino(mapa.primera_estacion, mapa.estaciones[10]))
    print(camino(mapa.estaciones[1], mapa.primera_estacion))
    print(camino(mapa.estaciones[9], mapa.estaciones[14]))
    print(camino(mapa.primera_estacion, mapa.primera_estacion))
    print(camino(mapa.primera_estacion, mapa.ultima_estacion))
