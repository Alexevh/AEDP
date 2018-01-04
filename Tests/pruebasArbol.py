from Arbol.Arbol import Arbol, NodoArbol
from Dominio.Persona import Persona


#Generamos 3 personas
p1 = Persona("Peter", "Parker", 33333333, 0.0, 0.0)
p2 = Persona("Jack", "Bauer", 11111111, 0.0, 0.0)
p3 = Persona("Maria", "Carey", 22222222, 0.0, 0.0)
p4 = Persona("Madam", "Curie", 44444444, 0.0, 0.0)

arbol = Arbol()

arbol.insertarOrdenado(p1)
arbol.insertarOrdenado(p2)
arbol.insertarOrdenado(p3)

p1pertenece = arbol.pertenece(p2)
p4pertenece = arbol.pertenece(p4)

print("Si todo funciona bien p1 pertenece = "+p1pertenece.__str__()+" pero p4 tiene el valor "+p4pertenece.__str__())

arbol.listarAscendente()
