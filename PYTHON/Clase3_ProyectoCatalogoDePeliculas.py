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



# 3.3 Creación de la clase catalogo_peliculas - Alumno: Giuliana Dealbera Etchechoury

import os

class CatalogoPeliculas:
    ruta_archivo = 'Pelicula.txt'

    @classmethod
    def agregar_peliculas(cls, pelicula):
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
            print(f'Catalogo de peliculas'.center(50, '-'))
            print(archivo.read())

    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo eliminado: {cls.ruta_archivo}')

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
            print(f'Catalogo de peliculas'.center(50, '-'))
            print(archivo.read())

    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo eliminado: {cls.ruta_archivo}')

# 3.4 Creación test_catalogo_peliculas - Alumno: Nicolas Segovia

opcion = None
while opcion != 4:
    try:
        print('Opciones: ')
        print('1. Agregar Pelicula')
        print('2. Listar las peliculas')
        print('3. Eliminar cat{alogo de peliculas}')
        print('4. Salir')
        opcion = int(input('Digite una opción de menú (1-4): '))
    except Exception as e:
        print(f'Ocurrió un error de tipo: {e}')
        opcion = None
    else:
        print('Salimos del programa')

# 3.5  Comenzamos con las pruebas ingresando las otras clases - Alumno: Juan Pablo Nolan

from dominio.Pelicula import Pelicula
from  servicio.catalogo_peliculas import CatalogoPeliculas as cp

opcion = None
while opcion != 4:
    try:
        print("Opciones: ")
        print("1. Agregar pelicula")
        print("2. Listar películas")
        print("3. Eliminar catálogo de peliculas")
        print("4. Salir")
        opcion = int(input("Digite una opcion de menu (1-4): "))
        if opcion == 1:
            nombre_pelicula = input("Digite el nombre de la pelicula: ")
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_peliculas(pelicula)
        elif opcion == 2:
            cp.listar_peliculas()
        elif opcion == 3:
            cp.eliminar_peliculas()
    except Exception as e:
        print(f"Ha ocurrido un error de tipo:{e}")
        opcion = None
    else:
        print("Salimos del programa")

# 3.2 Creación de la clase película - Alumno: Giuliana Paola Diaz Luna 

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





