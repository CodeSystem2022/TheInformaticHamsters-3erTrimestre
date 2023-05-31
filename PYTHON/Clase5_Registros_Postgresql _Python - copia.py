'''
Clase 5: Postgresql y Python
Laboratorio III: PYTHON
Team: The Informatic Hamsters
Scrum Master: Miguel Rodriguez Saquilan
'''


import psycopg2 #Esto es para poder conectarnos a la base creada mediante postgress




# 5.1 Uso de with y psycopg2 -- Alumno : Nadia Acosta

try:
    with conexion:
        with conexion.cursor() as cursor:  # con este uso del with no tengo que cerrar de manera manual la bd
            sentencia = 'SELECT * FROM persona'
            cursor.execute(sentencia)
            registros = cursor.fetchall() # recuperamos todos los registros que seran una lista
            print(registros)
except Exception as e: 
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()    


# 5.2 Función fetchone en psycopg2   - Alumno: Miguel Rodriguez Saquilan

try:
    with conexion:
        with conexion.cursor() as cursor:  # con este uso del with no tengo que cerrar de manera manual la bd
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s' #placeholder
            id_persona = input('Digite un numero para el id_persona: ') 
            cursor.execute(sentencia,(id_persona,))# de esta manera ejecutamos la sentencia 
            registros = cursor.fetchone5() # este metodo nos permite recuperar los registros de la sentencia
            print(registros)
except Exception as e: 
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()    
       

# cerramos todo. mas adelante veremos otra forma de hacerlo

conexion.close() 


# 5.3 Función fechall en psycopg2 Parte 1  - Alumno: Juan Pablo Nolan

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona IN (1, 2, 3, 4, 5, 6, 7)' #Placeholder
            #entrada = input("Digite los id_persona a buscar (separados por coma): ")
            cursor.execute(sentencia) #De esta manera ejecutamos la sentencia
            registros = cursor.fetchall() #Recuperamos todos los registros que seran una lista
            for registro in registros:
                print(registro)

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

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

# 5.5 Insertar varios registros -Alumno: Giuliana Paola Diaz Luna 

import psycopg2  # Esto es para poder conectarnos a Postgre

conexion = psycopg2.connect(
    user = "postgres",
    password = "admin",
    host = "127.0.0.1",
    port = "5432",
    database = "test_bd"
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona (nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = (
                ('Carlos', 'Lara', 'clara@mail.com'),
                ('Marcos', 'Canto', 'mcantos@gmail.com'),
                ('Marcelo', 'Cuenca', 'cuencam@gmail.com')
            ) # Es una tupla de tuplas
            cursor.executemany(sentencia, valores) # De esta manera ejecutamos la sentencia
            #conexion.commit() # Esto se utiliza para guardar los cambios en la base de datos
            registros_insertados = cursor.rowcount
            print(f'Los registros insertados son: {registros_insertados}')


except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()


# 5.6 Actualizar o modificar un registro -Alumno: Marcelo A. Quispe
import psycopg2      # Esto hace que  podamos conectarnos a Postgre

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
try:
    with conexion:
         with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Juan Carlos', 'Roldan', 'rcarlos@mail.com', 1) # es una tupla
            cursor.execute(sentencia, valores) # De esta manera ejecutamos la sentencia
            registros_actualizados = cursor.rowcount
            print(f'Los registros actualizados son: {registros_actualizados}')


except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

