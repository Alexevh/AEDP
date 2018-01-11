from Grafo import  ListaAdy
"""
Vamos a implementar un grafo con lista de adyacencia, el grafo tiene como parametro de inicio la cantidad maxima
de nodos que va a aceptar, al iniciar se genera la lista de objetos con un None en cada uno

"""


class Grafo():

    def __init__(self, cantidad):
        self.cantidadActual =0
        self.cantidadMaxima = cantidad
        self.listasAdy = []
        self.objetos = []

        for i in range(0, cantidad):
            self.objetos.append(None)

        for i in range(0, cantidad):
            lista = ListaAdy.ListaAdy()
            self.listasAdy.append(lista)




    def estaLleno(self):
        """
        Nos devuelve true si el grafo ya esta lleno
        :return:
        """
        return self.cantidadActual == self.cantidadMaxima

    def buscarIndice(self):
        """
        Devuelve el indice, un lugar en la lista de objetos que este libre para poder ser insertado ahi
        :return:
        """
        indice =0
        if (self.estaLleno()):
            indice = -1
        else:
            encontre = False
            while (indice<self.cantidadMaxima) and (encontre==False):
                if self.objetos[indice] is None:
                    encontre = True
                else:
                    indice = indice+1

        return indice

    def agregarElemento(self, elemento):
        """
        Agregar un elemento busca un lugar libre en la lista y si lo encuentra lo coloca alli
        :param elemento:
        :return:
        """
        indice = self.buscarIndice()
        if (indice>=0):
            self.objetos[indice] = elemento
            self.cantidadActual = self.cantidadActual+1


    def buscarIndiceDeUnObjeto(self, objeto):
        """
        Dado un objeto me fijo en que posicion de la lista esta
        :param objeto:
        :return:
        """
        indice =0
        encontre = False

        while  (indice<self.cantidadMaxima) and (encontre==False):
            if objeto==self.objetos[indice]:
                encontre = True
            else:
                indice +=1

        if (encontre==False):
            indice =-1

        return indice

    def agregarTramo(self, objetoA, objetoB, peso=0, dirigido=True):
        origen = self.buscarIndiceDeUnObjeto(objetoA)
        destino = self.buscarIndiceDeUnObjeto(objetoB)
        self.agregarTramoLista(origen, destino, peso, dirigido)


    def agregarTramoLista(self, origen, destino, peso, dirigido):
        self.listasAdy[origen].insertar(destino, peso)
        if (dirigido==True):
            self.listasAdy[destino].insertar(origen, peso)
