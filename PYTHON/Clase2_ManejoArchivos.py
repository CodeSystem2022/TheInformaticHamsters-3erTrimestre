'''
Clase 2: Manejo de Archivos
Laboratorio III: PYTHON
Team: The Informatic Hamsters
Scrum Master: Giuliana Dealbera Etchechoury
'''

# 2.1 Introducción a lo que es el manejo de archivos - Alumno: 

# 2.2 Especificar el juego de caracteres de un archivo de texto - Alumno: Nadia Acosta
try:
    archivo = open('prueba.txt', 'w', encoding='utf8') #La w es de write
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Los acentos son importantes para las palabras\n')
    archivo.write('como por ejemplo: acción, ejecución y producción\n')
    archivo.write('Con eso terminamos.')
except Exception as e:
    print(e)
finally : #siempre se ejecuta
    archivo.close() #con esto se debe cerrar el archivo

# archivo.write('Todo quedó perfecto'): este es un error!

# 2.3 Lectura de archivos - Alumno: 

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