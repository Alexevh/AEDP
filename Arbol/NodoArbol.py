
class NodoArbol():

    def __init__(self, persona=None):
        if persona is not None:
            self.persona = persona
            self.NodoIzquierdo = None
            self.NodoDerecho = None
        else:
            self.persona = None
            self.NodoIzquierdo = None
            self.NodoDerecho = None