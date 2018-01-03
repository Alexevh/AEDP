
"""
Vamos a generar una clase en donde vamos a colocar todos los metodos de ordenacion
vamos a tener BubbleSort, MergeSort y QUick Sort como minimo

1. BubbleSort

El algoritmo funciona asi, tengo un vector con 3 numeros (hagamosla facil) [5,2,1]
voy a recorrer el vector, primero me paro en la posicion 0 y recorro todos los demas
preguntando si es mayor o menor.
Entonces, en la pasada 1 del for queda asi
a. i=0
b. v[j] > v[j+1]?, si, 5 es mayor que 2 que es el siguiente numero en la posicion, entonces guardo v[j] en una
variable temporal y cambio los lugares

"""

class Sort:

    def bubbleSort(self, v):

        n=len(v)
        for i in range (0, n-1):
            for j in range (0, n-1-i):
                if v[j]>v[j+1]:
                    temp = v[j]
                    v[j] = v[j+1]
                    v[j+1] = temp


    def selectionSort(self, v):
        n = len(v)

        for i in range (0, n):
            min =i
            for j in range (i+1, n):
                if v[j] < v[min]:
                    min =j

            if i!=min:
                aux = v[i]
                v[i]=v[min]
                v[min] = aux


    def insertionSort(self, v):
        n = len(v)

        for i in range (0, n):
            aux = v[i]
            j = i-1

            while (j>=0) &  (v[j]> aux):
                v[j+1] = v[j]
                j-=1

            v[j+1]=aux

