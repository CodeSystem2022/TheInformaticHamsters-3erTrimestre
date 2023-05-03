'''
Clase 2: Manejo de Archivos
Laboratorio III: PYTHON
Team: The Informatic Hamsters
Scrum Master: Giuliana Dealbera Etchechoury
'''

# 2.1 Introducción a lo que es el manejo de archivos - Alumno: 

# 2.2 Especificar el juego de caracteres de un archivo de texto - Alumno: 

# 2.3 Lectura de archivos - Alumno: Juan Pablo Nolan

#archivo = open('prueba.txt', 'r', encoding='utf8') # 'r', de 'read', para leer
# print(archivo.read())

# parametro 'a', lo utilizamos para anexar informacion a un archivo que ya contiene cierta informarcion.
# de esta manera, cuando escribimos nueva informacion no se borra la anterior, sino se agrega.
archivo = open('prueba.txt', 'a', encoding='utf8')

# Especifico los caracteres a mostrar
print(archivo.read(16))
print(archivo.read(10))

# Leo toda una linea
print(archivo.readline())
print(archivo.readline())

# 2.4 Más formas de trabajar con archivos - Alumno: 

# 2.5 Uso de WITH, archivos y contexto Manager I - Alumno: Giuliana Dealbera Etchechoury

with open('prueba.txt', 'r', encoding='utf8') as archivo:
    print(archivo.read())

# 2.6 Uso de WITH, archivos y contexto Manager II - Alumno: Nicolas Segovia

# Importamos nuestro metodo de clase
# from ManejoArchivos import ManejoArchivos

# With pero con nuestra clase creada en ManejoArchivo.py
with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())