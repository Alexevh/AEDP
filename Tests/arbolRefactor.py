from Arbol.Arbol import Arbol, NodoArbol
from Dominio.Persona import Persona
import unittest


#Generamos 3 personas
p1 = Persona("Peter", "Parker", 33333333, 0.0, 0.0)
p2 = Persona("Jack", "Bauer", 11111111, 0.0, 0.0)
p3 = Persona("Maria", "Carey", 22222222, 0.0, 0.0)
p4 = Persona("Madam", "Curie", 44444444, 0.0, 0.0)


arbol = Arbol()

arbol.insertarOrdenado(p1)
arbol.insertarOrdenado(p2)
arbol.insertarOrdenado(p3)

arbol.listarAscendente()

p1pertenece = arbol.pertenece(p3)
p4pertenece = arbol.pertenece(p4)

print("Si todo funciona bien p1 pertenece = "+p1pertenece.__str__()+" pero p4 tiene el valor "+p4pertenece.__str__())

arbol.eliminarMinimo()
print("Luego de eliminar el minimo nos queda")
arbol.listarAscendente()

print("Vamos a buscar un nodo")
nodoBuscado = arbol.buscarElemento(p1)
print("El nodo P1 se encontro y el valor es :"+nodoBuscado.objeto.nombre)
print("Vamos a buscar un nodo que no exista")
nodoBuscado2 = arbol.buscarElemento(p4)
print("El nodo P4 no se encontro y el valor es :"+str(nodoBuscado2))

print("Vamos a probar la cantidad de Hojas")
cantidadHojas = arbol.cantidadHojas()
print("El arbol tiene : "+str(cantidadHojas)+" hojas ")

print("Obtenemos la altura del arbol")
altura = arbol.altura()
print("la altura del arbol es de "+str(altura))

print("Voy a contar los nodos")
cantNodos = arbol.cantidadNodos()
print("El arbol tiene "+str(cantNodos)+" nodos")

esVacio = arbol.esVacio()
print("El arbo es vacio? "+str(esVacio))

arbol.borrarElemento(p1)
print("Luego de borrar a P2 listo elarbol")
arbol.listarAscendente()

