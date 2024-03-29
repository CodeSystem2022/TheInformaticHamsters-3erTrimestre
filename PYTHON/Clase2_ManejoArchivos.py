'''
Clase 2: Manejo de Archivos
Laboratorio III: PYTHON
Team: The Informatic Hamsters
Scrum Master: Giuliana Dealbera Etchechoury
'''

# 2.1 Introducción a lo que es el manejo de archivos - Alumno: Quiquinto Romina Ayelen
try:
    archivo = open('prueba.txt','w')
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Con esto terminamos')
except Exception as e:
    print(e)
finally:
    archivo.close()

# 2.1 Introducción a lo que es el manejo de archivos - Alumno: Miguel Rodriguez Saquilan
    
# declaramos una variable
# usamos el metodo open que nos sirve para buscar un archivo o crear un nuevo archivo
# este metodo open puede arrogar una execpcion por lo que siempre va dentro 
# de un try
try:
   # la w es write(escribir)
   archivo = open('prueba.txt','w', encoding='utf8')# lo que estamos indicando es que si no esta el archivo lo cree
   archivo.write('Programamos con diferentes tipo de archivos, ahora .txt  \n')
   # lo que estamos haciendo ahora es modificar nuestro archivo
   archivo.write('Con esto terminamos')# .write es para escribir nuestro archivo
   
except   Exception as e :
  print(e)

finally: # siempre se ejecuta
    archivo.close()# con esto se debe cerrar el archivo


# 2.2 Especificar el juego de caracteres de un archivo de texto - Alumno: Giuliana Paola Diaz Luna

archivo = open('prueba.txt', 'w', encoding='utf8') # Si este archivo no existe, lo va a crear. 'w', de 'write', escribir

try:
    archivo.write("Programamos con diferentes tipos de archivos, ahora en .txt\n")
    archivo.write("Agrego palabras con acentos: \n")
    archivo.write("- Programación\n")
    archivo.write("- Introducción\n")
except Exception as ex:
    print(ex)
finally:
    archivo.close()

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


# 2.5 Uso de WITH, archivos y contexto Manager I - Alumno: Giuliana Dealbera Etchechoury

with open('prueba.txt', 'r', encoding='utf8') as archivo:
    print(archivo.read())

# 2.6 Uso de WITH, archivos y contexto Manager II - Alumno: Nicolas Segovia

# Importamos nuestro metodo de clase
# from ManejoArchivos import ManejoArchivos

# With pero con nuestra clase creada en ManejoArchivo.py
with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())