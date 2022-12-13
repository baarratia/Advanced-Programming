__author__ = 'Benja'

class Arbol:
    def __init__(self, valor=None, padre=None):
        self.valor = valor
        self.padre = padre
        self.hijos = []

    def agregar_nodo(self, valor, padre=None):
        if padre == None:
                self.hijos.append(Arbol(valor))
        else:
                self.hijos.append(Arbol(valor, padre))

    def obtener_nodo(self, posicion):
        # obtiene el nodo siempre y cuando exista la posicion.
        if posicion < len(self.hijos):
            return self.hijos[posicion]

    def __repr__(self):
        #self.ret = str(self.valor)

        def recorrer_arbol(raiz):
            for hijo in raiz.hijos:
                self.ret+="padre: {0} -> valor: {1}\n".format(hijo.padre, hijo.valor)
                recorrer_arbol(hijo)
            return self

        self.ret = ''
        recorrer_arbol(self)
        return self.ret

class ArbolPreOrder(Arbol):

    def __repr__(self):
        def recorrer_arbol(raiz):
            self.ret += "padre: {0} -> valor: {1}\n".format(raiz.padre, raiz.valor)
            for hijo in raiz.hijos:
                recorrer_arbol(hijo)
            return self

        self.ret = ''
        recorrer_arbol(self)
        return self.ret