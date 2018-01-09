"""
La idea es que cada nodo guarda un objeto, cada nodo debe tener una propiedad con la que compararse
esto nos permite  guardar cualquier objeto de clase.

La unica restricciones que el objeto debe implementar las funciones de compararse con otros tanto como saber si es
igual __eq__ como saber si esmayor o menor __lt__
"""
class NodoArbol():

    def __init__(self, objeto=None):
        if objeto is not None:
            self.objeto = objeto
            self.NodoIzquierdo = None
            self.NodoDerecho = None
        else:
            self.objeto = None
            self.NodoIzquierdo = None
            self.NodoDerecho = None