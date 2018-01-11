from Grafo import Grafo
from Dominio.Persona import Persona

grafo = Grafo.Grafo(10)

print("Grafo recien inicialziado con cantidad actual = "+str(grafo.cantidadActual))
print("Grafo recien inicialziado con cantidad maxima = "+str(grafo.cantidadMaxima))
print("Grafo recien inicialziado con cantidad objetos = "+str(len(grafo.objetos)))

print("Vamos a agregar cuatro puntos al grafo")
#Generamos 4 personas
p1 = Persona("Peter", "Parker", 33333333, 0.0, 0.0)
p2 = Persona("Jack", "Bauer", 11111111, 0.0, 0.0)
p3 = Persona("Maria", "Carey", 22222222, 0.0, 0.0)
p4 = Persona("Madam", "Curie", 44444444, 0.0, 0.0)

grafo.agregarElemento(p1)
grafo.agregarElemento(p2)
grafo.agregarElemento(p3)
grafo.agregarElemento(p4)

print("Grafo  inicialziado con datos nuevos,  cantidad actual = "+str(grafo.cantidadActual))
print("Grafo  inicialziado con datos nuevos, cantidad maxima = "+str(grafo.cantidadMaxima))
print("Grafo  inicialziado con datos nuevos, cantidad objetos = "+str(len(grafo.objetos)))

print("En la posicion 0 de la lista tenemos a "+grafo.objetos[0].nombre)

posicionP3 = grafo.buscarIndiceDeUnObjeto(p3)
print("El elemento P3 esta en el indice "+str(posicionP3))

print("Agreguemos tramos")
grafo.agregarTramo(p1, p2, 100, True)
grafo.agregarTramo(p1, p3, 90, False)

print("Vamos a ver cuantos tramos tenemos")
print("Tenemos en P1 la cantidad de "+str(grafo.listasAdy[0].cantidad)+" tramos")
print("Como uno de los tramos no era dirigido la lista de p2 debe tener "+str(grafo.listasAdy[1].cantidad)+" tramos")