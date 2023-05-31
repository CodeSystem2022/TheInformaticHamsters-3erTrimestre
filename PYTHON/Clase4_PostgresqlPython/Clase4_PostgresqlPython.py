'''
Clase 4: Postgresql y Python
Laboratorio III: PYTHON
Team: The Informatic Hamsters
Scrum Master: Giuliana Paola Diaz Luna
'''


# 4.2 Creamos un base de datos llamada prueba_bd y cargamos una tabla con sus columnas - Alumno: Giuliana Dealbera Etchechoury

'''
Instalamos el programa Postgresql. Dentro de Databases creamos una base de dato llamada "test_bd".
Luego nos dirigimos Schemas → Public y agregamos una tabla.
Esta tabla la llamamos persona y le agregamos 4 columnas: id_persona, nombre, apellido y email.
Al id_persona lo marcamos como una PK.
Ya teniendo la rama armada, seleccionamos la opción de VIEW y observamos el Query generado, y abajo, la tabla misma
dónde agregamos unos datos.
''' 


# 4.3 Consultas con código Query en Postgresql Parte 1 - Alumno: Nicolas Segovia


# 4.4 Consultas con código Query en Postgresql Parte 2 - Alumno: Giuliana Paola Diaz Luna

# 4.4 Consultas con código Query en Postgresql Parte 2 - Alumno: Miguel Rodriguez Saquilan


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

# 4.6 Conexión hacia la base de datos en Python con el método fetchall() - Alumno: Nadia Acosta
# ir a archivo prueba_bd

# 4.7 Cerramos la conexión y la consulta - Alumno: 


