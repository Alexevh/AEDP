import algoritmos.sort as ordenar


#Probemos el Bubble Sort

myVector = [5,1,2,9,2,3,15,2]

ordenador = ordenar.Sort()

#ordenador.bubbleSort(myVector)
#ordenador.selectionSort(myVector)
ordenador.insertionSort(myVector)
print(myVector)