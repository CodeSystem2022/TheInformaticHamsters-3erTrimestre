'''
Clase 1: Excepciones
Laboratorio III: PYTHON
Team: The Informatic Hamsters
Scrum Master: Nicolas Segovia
'''

# 1.1 Manejo de errores o excepciones Parte 1 y parte 2 - Alumno: Nicolas Segovia

try:
    10/0
except ZeroDivisionError as ex:
    print(f'Ocurrio un error: {ex}')


# 1.2 Procesamiento de excepciones - Alumno: Giuliana Dealbera Etchechoury

result = None
a = 10
b = 0
try:
    result = a / b 
except ZeroDivisionError as error:
    print(f'Ocurrió un error: {error}')

print(f'El resultado es: {result}')

# 1.3 Procesar clases de exception más específicas - Alumno: Nadia Acosta

resultado = None
a = 10
b = 0
try:
    resultado = a / b
except TypeError as ex:
    print(f'TypeError - Ocurrio un error: {type(ex)}')
except ZeroDivisionError as ex:
    print(f'Ocurrio un error: {ex}')
except Exception as ex:
    print(f'Ocurrio un error: {ex}')
print(f'El resiltado es: {resultado}')
print(f'seguimos...')

# 1.4 Más de procedimientos de excepciones - Alumno: Giuliana Paola Diaz Luna

resultado = None
try:
    a = int(input("Digite el primer número: "))
    b = int(input("Digite el segundo número: "))
    resultado = a / b
except TypeError as ex:
    print(f'TypeError - Ocurrio un error: {type(ex)}')
except ZeroDivisionError as ex:
    print(f'Ocurrio un error: {ex}')
except Exception as ex:
    print(f'Ocurrio un error: {ex}')
print(f'El resiltado es: {resultado}')
print(f'seguimos...')


# 1.5 Bloques else y finally al manejar excepciones - Alumno: Juan Pablo Nolan

resultado = None
try:
    a = int(input("Digite el primer número: "))
    b = int(input("Digite el segundo número: "))
    resultado = a / b
except TypeError as ex:
    print(f'TypeError - Ocurrio un error: {type(ex)}')
except ZeroDivisionError as ex:
    print(f'Ocurrio un error: {ex}')
except Exception as ex:
    print(f'Ocurrio un error: {ex}')
else:
    print("No se arrojo ninguna excepcion") # El 'else' sera ejecutado en el caso que no se arroje ninguna excepcion.
finally:
    print("Ejecicion de este bloque finally")
print(f'El resiltado es: {resultado}')
print(f'seguimos...')

# 1.6 Creación de clases de Exception personalizadas - Alumno: Miguel Rodriguez Saquilan

class NumerosIgualesException (Exception): # Extiende de la clase
    def __init__(self, mensaje) -> None:
        self.message = mensaje
        


# 1.5 Bloques else y finally al manejar excepciones - Alumno: Marcelo Quispe

resultado = None
try:
    a = int(input("Digite el primer número: "))
    b = int(input("Digite el segundo número: "))
    resultado = a / b
except TypeError as ex:
    print(f'TypeError - Ocurrio un error: {type(ex)}')
except ZeroDivisionError as ex:
    print(f'Ocurrio un error: {ex}')
except Exception as ex:
    print(f'Ocurrio un error: {ex}')
else:
    print("No se arrojo ninguna excepcion") # El 'else' sera ejecutado en el caso que no se arroje ninguna excepcion.
finally:
    print("Ejecicion de este bloque finally")
print(f'El resiltado es: {resultado}')
print(f'seguimos...')


