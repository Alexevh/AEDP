
from Dominio.Persona import Persona
from Arbol.NodoArbol import NodoArbol

p1 = Persona("Peter", "Parker", 754874, 0.0, 0.0)


nodo1 = NodoArbol(p1)
nodo2 = NodoArbol()

print("El nodo 1 tiene una persona , se llama "+nodo1.persona.nombre)

