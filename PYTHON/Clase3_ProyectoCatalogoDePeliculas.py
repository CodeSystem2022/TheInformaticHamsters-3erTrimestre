'''
Clase 3: Proyecto Catálogo De Peliculas
Laboratorio III: PYTHON
Team: The Informatic Hamsters
Scrum Master: Nadia Acosta
'''

# 3.2 Creación de la clase película - Alumno: Nadia Acosta

class Pelicula:
    def __init__(self, nombre):
        self._nombre = nombre

    def __str__ (self):
        return f'Pelicula: {self._nombre}'

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter 
    def nombre(self, nombre):
        self._nombre = nombre


# 3.3 Creación de la clase catalogo_peliculas - Alumno:


# 3.4 Creación test_catalogo_peliculas - Alumno:

# 3.5  Comenzamos con las pruebas ingresando las otras clases - Alumno:




