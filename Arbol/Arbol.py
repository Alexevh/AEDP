from Arbol.NodoArbol import NodoArbol


class Arbol():

    def __init__(self):
        self.NodoRaiz = None



    def insertarOrdenado(self, persona):
        if self.NodoRaiz is None:
            nodo = NodoArbol(persona)
            self.NodoRaiz = nodo
        else:
            Arbol.insertarelemento(persona, self.NodoRaiz)


    #Funcion que inserta el elemento propiamente dicho
    def insertarelemento(persona, nodo):

        if nodo.persona.documento > persona.documento:
            if nodo.NodoIzquierdo is None:
                n = NodoArbol(persona)
                nodo.NodoIzquierdo = n
            else:
                Arbol.insertarelemento(persona, nodo.NodoIzquierdo)

        elif nodo.NodoDerecho is None:
            n = NodoArbol(persona)
            nodo.NodoDerecho = n
        else:
            Arbol.insertarelemento(persona, nodo.NodoDerecho)


    def pertenece(self, persona):
        return Arbol.personaPertenece(persona, self.NodoRaiz)

    def personaPertenece(persona, nodo):

        if nodo is None:
            return False

        if persona.documento == nodo.persona.documento:
            return True

        if nodo.persona.documento > persona.documento:
            return Arbol.personaPertenece(persona, nodo.NodoIzquierdo)
        else:
            return Arbol.personaPertenece(persona, nodo.NodoDerecho)
