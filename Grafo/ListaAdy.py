from Grafo import NodoGrafo

class ListaAdy():

    def __init__(self):
        self.cantidad=0
        self.inicio = None


    def insertar(self, destino, peso):
        """
        /* Metodo para insertar un nodo
    Si tanto el destino como el peso son mayores o iguales a cero, creamos un
    nodo.

    Luego vemos, si en la lista de adyacencias el inicio no esta en null significa
    que no esta vacia, entonces seteamos como el nodo anterior al actual inicio
    el nodo nuevo y el nodo nuevo se convierte en el inicio.

    De lo contrario, la lista esta vacia y solo hacemos que el inicio sea el nodo nuevo

    EL grafo no contiene una lista de adyacencias, contiene un vector de listas
    cuyo tama;o es igual a la cantidad de verices, cada vertice mantiene su propia
    lista
        :param destino:
        :param peso:
        :return:
        """
        if(destino>=0) and (peso>=0):
            nodo = NodoGrafo.NodoGrafo(destino, peso)
            if (self.inicio is not None):
                self.inicio.anterior = nodo
                nodo.siguiente = self.inicio

            self.inicio = nodo
            self.cantidad +=1
