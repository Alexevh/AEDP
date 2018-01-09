import functools

"""
Esta clase va a ser usada en un arbol, es por eso que debe implementar los metodos para compararse con otras
__lt__ y __eq__
"""

@functools.total_ordering
class Persona():

    def __init__(self, nombre, apellido, documento, coordX, coordY):

        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.coordX = coordX
        self.coordY = coordY

    def __lt__(self, other):
        if self.documento == other.documento:
            return self.documento < other.documento
        return self.documento < other.documento

    def __eq__(self, other):
        return self.documento == other.documento


