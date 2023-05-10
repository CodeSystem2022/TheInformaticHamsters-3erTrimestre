'''
Clase 4: Postgresql y Python
Laboratorio III: PYTHON
Team: The Informatic Hamsters
Scrum Master: Giuliana Paola Diaz Luna
'''


# 4.2 Creamos un base de datos llamada prueba_bd y cargamos una tabla con sus columnas - Alumno: 


# 4.3 Consultas con código Query en Postgresql Parte 1 - Alumno: 


# 4.4 Consultas con código Query en Postgresql Parte 2 - Alumno: 



# 4.6 Conexión hacia la base de datos en Python con el método fetchall() - Alumno: Juan Pablo Nolan

import psycopg2 #Esto es para poder conectarnos a la base creada mediante postgress

conexion = psycopg2.connect(
    user='postgres',
    password='Lautaro-1',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)

cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona WHERE id_persona = 1'
cursor.execute(sentencia) #De esta manera ejecutamos la sentencia
registros = cursor.fetchall() #Recuperamos todos los registros que seran una lista
print(registros)

# 4.7 Cerramos la conexión y la consulta - Alumno: 


