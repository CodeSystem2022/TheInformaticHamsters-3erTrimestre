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


# 3.3 Creación de la clase catalogo_peliculas - Alumno: Marcelo Quispe
import os

class CatalogoPeliculas:

    ruta_archivo = 'pelicula.txt'

    @classmethod
    def agregar_peliculas(cls, pelicula):
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
            print(f'Catalogo de pelicula'.center(50, '-'))
            print(archivo.read())

    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'Achivo eliminado :{cls.ruta_archivo}')

# 3.4 Creación test_catalogo_peliculas - Alumno:

# 3.5  Comenzamos con las pruebas ingresando las otras clases - Alumno:




