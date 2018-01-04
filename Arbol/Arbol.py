from Arbol.NodoArbol import NodoArbol


class Arbol():

    def __init__(self):
        self.NodoRaiz = None



    def insertarOrdenado(self, persona):
        """
        La funcion es accesoria, si el nodo raiz esta vacio entonces el arbol esta vacio y ponemos a la persona
        en la raiz ya que es el primer nodo.

        Si el nodo raiz esta ocupado entonces el arbol no esta vacio, y vamos a llamar a la funcion recursiva
        que va a insertar el elemento en donde corresponda

        :param persona:
        :return:
        """
        if self.NodoRaiz is None:
            nodo = NodoArbol(persona)
            self.NodoRaiz = nodo
        else:
            Arbol.insertarelemento(persona, self.NodoRaiz)



    def insertarelemento(persona, nodo):
        """
        Primero comparamos si el nodo que estamos visitando tiene un valor mayor a lo que nos estan pasando,
        o sea en el caso del ejemplo de persona si el documento de la nueva es mayor o menor a la que esta
        almacenada en el nodo que estamos visitando.

        Si el valor del elemento que nos pasan es menor al nodo que estamos visitando entonces vamos a intentar
        colocarlo a la izquierda, para ello nos fijamos si el nodo izquierdo esta vacio, si es asi entonces ponemos
        el nodo que nos pasaron a la izquierda.

        Si el nodo esta ocupado entonces hacemos la recursiva, sobre ese nodo, en cuyo caso se repetiran los casos
        anteriores.

        En cualquiera de esos pasos, si la comparativa da que el valor es mayor al nodo que estamos visitando entonces
        se hace la recursiva sobre el nodo derecho

        :param nodo:
        :return:
        """

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
        """
        El metodo recibe un objeto y devolvera True si el elemento se encuentra dentro del arbol y False en el
        caso contrario
        :param persona:
        :return: Boolean, True o False
        """
        return Arbol.personaPertenece(persona, self.NodoRaiz)

    def personaPertenece(persona, nodo):
        """
        Recursiva que implementa el pertenece

        Primero establecemos los casos base, si el nodo es Nulo devolvemos False y si la persona.documento
        es igual al nodo.persona.documento devolvemos True ya que significa que lo encontramos

        Si no, entonces nos fijamos, si el documento de la persona que nos pasan es menor al que esta en el nodo
        en el que estamos parados, si ese es el caso entonces hacemos la recursivasobre el izquierdo, de lo contrario
        lo hacemos sobre el derecho

        :param nodo:
        :return: True o False
        """
        if nodo is None:
            return False

        if persona.documento == nodo.persona.documento:
            return True

        if nodo.persona.documento > persona.documento:
            return Arbol.personaPertenece(persona, nodo.NodoIzquierdo)
        else:
            return Arbol.personaPertenece(persona, nodo.NodoDerecho)



    def listarAscendente(self):
        """
        Lista en pantalla el arbol en forma ascendente
        :return:
        """
        Arbol.listarAscendenteInOrder(self, self.NodoRaiz)

    def listarAscendenteInOrder(self, nodo):
        """
        Es una recorrida IN ORDER del arbol, esta implementada como una forma facil de recordar la recorrida
        :param nodo:
        :return:
        """

        if nodo is None:
            return None
        else:
            Arbol.listarAscendenteInOrder(self, nodo.NodoIzquierdo)
            print(nodo.persona.documento)
            Arbol.listarAscendenteInOrder(self, nodo.NodoDerecho)






