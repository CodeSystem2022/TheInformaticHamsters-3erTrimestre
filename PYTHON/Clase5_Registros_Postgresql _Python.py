'''
Clase 5: Postgresql y Python
Laboratorio III: PYTHON
Team: The Informatic Hamsters
Scrum Master: Miguel Rodriguez Saquilan
'''


import psycopg2 #Esto es para poder conectarnos a la base creada mediante postgress

conexion = psycopg2.connect(
    user='postgres',
    password='Lautaro-1',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)


# 5.1 Uso de with y psycopg2 -- Alumno : 



# 5.2 Función fetchone en psycopg2   - Alumno: 


# 5.3 Función fechall en psycopg2 Parte 1  - Alumno: 


# 5.3 Función fechall en psycopg2 Parte  2 -Alumno:



# 5.4 Insertar un registro con psycopg2 - Alumno: Giuliana Dealbera Etchechoury

import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona (nombre, apellido, email)VALUE (%s, %s, %s)'
            valores = ('Carlos', 'Lara', 'clara@mail.com')
            cursor.execute(sentencia, valores)
            registros_insertados = cursor.rowcount
            print(f'Los registros insertados son: {registros_insertados}')
except Exception as error:
    print(f'Ocurrió un error: {error}')
finally:
    conexion.close()

# 5.5 Insertar varios registros -Alumno:



# 5.6 Actualizar o modificar un registro -Alumno:


