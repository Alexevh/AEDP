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



    def eliminarMinimo(self):
        """
        Elimina el elemento con valor minimo en el arbol
        :return:
        """
        self.NodoRaiz = Arbol.eliminarMin(self, self.NodoRaiz)


    def eliminarMin(self, nodo):
        """
            El algoritmo recibe un nodo, si es nodo es null lregresa ese nodo

    Si el nodo que nos pasaron no es nulo,entonces se fija, si el nodo A tiene
    un nodo izquierdo distinto de null  trata de setear como nodoIZq el resultado
    de eliminarMin a su nodo izquierdo actual y regresa A, de lo contrario retrna
    a.nododerecho.

    Imaginemos lo siguiente, nos pasan la raiz que tiene un 10, el algoritmo se
    fija, a == null? la respuesta es NO, entonces sigue con lo demas, si hubiera
    sido null regresaba el nodo.

    Entonces se fija el nodo A tiene un valor en la izquierda distinto de null?
    si A tiene un valor en la izquierda distinto de null significa que ahi hay
    un nodo en cuyo caso va a hacer a.setnodoizquierdo eliminarminimo de su nodo
    izquierdo, si nodo izquierdo tiene un nodo izquierdo en null, se va a retornar
    A que es null, por lo que el nodo izquierdo anterio se elimina.

    Si el nodo izquierdo ya era null regersamos el nodo derecho como uevo valor
    de A
        """
        if nodo is None:
            return nodo

        if nodo.NodoIzquierdo is not None:
            nodo.NodoIzquierdo = self.eliminarMin(nodo.NodoIzquierdo)
            return nodo
        else:
            return nodo.NodoDerecho



    def buscarElemento(self, nodo):
        """
        Funcion que llama a la recursiva
        :param nodo:
        :return:
        """
        return Arbol.buscar(self.NodoRaiz, nodo)


    def buscar(nodo, elemento):
        """
        La recursiva va a buscar el elemento, comenzando en la raiz

        Los casos base son simples, si el nodo es null devolvemos null, si el nodo es lo que
        estamos buscando entonces encontramos el elemento y lo devolvemos

        :param elemento:
        :return:
        """

        if nodo is None:
            return None
        if nodo.persona.documento == elemento.documento:
            return nodo

        #Recursiva
        retorno = Arbol.buscar(nodo.NodoIzquierdo, elemento)
        if retorno==None:
            return Arbol.buscar(nodo.NodoDerecho, elemento)
        else:
            return retorno



    def cantidadHojas(self):
        return self.cantidadHojasRaiz(self.NodoRaiz)

    def cantidadHojasRaiz(self, nodo):
        """
        Es la recursiva que implementa el metodo anterior, una hoja en un arbol es aquel nodo que no tiene
        hijos

            /* El metodo va a contabilizar la cantidad de hojas a partir de un nodo
        normalmente lo vamos a llamar desde la raiz

        Si el nodo es null devolvemos cero, si el nodo no es null pero su nodo izq
        si es null retornamos 1+ el resultado del mismo metodo para el nododerecho
        en cambio si en nodoizq no es null retornamos la recursiva del nodoizquirdo + la
        recursiva del derecho

        Ejemplo

        Ejecutamos el procedimiento en la raiz que no es null y tiene un 10, el
        metodo se fija, el nodoiz es nulo? en este caso no, y tiene un valor de 9
        entonces como no es null va a ejecutar return recursiva(nodo.izq) + la
        recursiva(nodo.der)

        Imagineos que el nodo que tiene valor de 9 no tiene un izquierdo pero si
        un derecho, en esa segunda ejecucion la primera parte nos devuelve 1+ el
        resultado de la recursiva para el derecho.

        El derecho tiene un valor de 11, pero no tiene hijos, nos devuelve 1


        :param nodo:
        :return:
        """
        if nodo is None:
            return 0
        elif nodo.NodoIzquierdo is None:
            return 1+ self.cantidadHojasRaiz(nodo.NodoDerecho)
        else:
            return self.cantidadHojasRaiz(nodo.NodoIzquierdo)+ self.cantidadHojasRaiz(nodo.NodoDerecho)

    def altura(self):
        return self.obtenerAltura(self.NodoRaiz)


    def obtenerAltura(self, nodo):

        """
            El caso base es si el nodo == null devolvemos -1

    IMaginemos el arbol tiene el nodo raiz con un 10, se llama la funcion, el nodo
    no es null.

    La primera pasada se guardan dos enteros izq y der, si ambos tienen datos
    ninguno da -1 por lo que se repite la funcion.

    Imaginemos que el 10 tenia dos hijos, 9 y 11, esa pasada repite la funcion
    el 9 tiene un hijo 8 y el 11 no tiene ninguno.



    En la segunda pasada altura de derecha va a ser -1por lo que izquirda va a
    ser mayor por lo que devolvemos izq+1

    La recursiva altura(nodoizq) y derecho se ejecuta en el else hasta que
    encuentra el null.
        :param nodo:
        :return:
        """

        if nodo is None:
            return -1
        else:
            altIzq = self.obtenerAltura(nodo.NodoIzquierdo)
            altDer = self.obtenerAltura(nodo.NodoDerecho)

            if (altIzq > altDer):
                return altIzq+1
            else:
                return altDer+1


