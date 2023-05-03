'''
Clase 2: Manejo de Archivos
Laboratorio III: PYTHON
Team: The Informatic Hamsters
Scrum Master: Giuliana Dealbera Etchechoury
'''

# 2.1 Introducción a lo que es el manejo de archivos - Alumno: 

# 2.2 Especificar el juego de caracteres de un archivo de texto - Alumno: 

# 2.3 Lectura de archivos - Alumno: 

# 2.4 Más formas de trabajar con archivos - Alumno: Marcelo Quispe
# Declaramos una variable
try:
    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Los acentos son importantespara las palabras\n')
    archivo.write('como por ejemplo : acción, ejecución y producción \n')
    archivo.write('Las letras son :\nr read leer, \na append anexa, \nw write escribe, \nx crea un archivo')
    archivo.write('\nt es para texto o text, \nb archivos binarios, \nw+ lee y escribe son iguales r+\n')
    archivo.write('Saludos a todos los alumnos de la tecnicatura\n')
    archivo.write('Con esto terminamos')
except Exception as e:
    print(e)
finally:  # siempre se ejecuta
    archivo.close()  # con esto se debe cerrar el archivo
# archivo.write('Todo quedo perfecto') # es es un error


# 2.5 Uso de WITH, archivos y contexto Manager I - Alumno: 

with open('prueba.txt', 'r', encoding='utf8') as archivo:
    print(archivo.read())

# 2.6 Uso de WITH, archivos y contexto Manager II - Alumno: 