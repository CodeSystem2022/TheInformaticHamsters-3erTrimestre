import psycopg2 # Esto es para poder conectarnos a Postgre

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s' #Placeholder id
            id_persona = input('Ingrese un número para el id_persona: ')
            cursor.execute(sentencia, (id_persona,)) # De esta manera ejecutamos la sentencia
            registros = cursor.fetchone() #Recupera todos los registros de la sentencia que se ejecutó
            print(registros)
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    conexion.close()
