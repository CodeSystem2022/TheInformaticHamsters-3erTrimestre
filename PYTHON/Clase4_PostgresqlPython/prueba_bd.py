
# 4.6 Conexión hacia la base de datos en Python con el método fetchall() - Alumno: Nadia Acosta

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



