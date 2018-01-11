

class NodoGrafo():

    def __init__(self, destino, peso):
        self.destino = destino
        self.peso = peso
        self.anterior = None
        self.siguiente = None
