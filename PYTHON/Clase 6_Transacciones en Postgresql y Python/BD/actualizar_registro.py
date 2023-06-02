import psycopg2 # Sirve para poder conectarnos a Postgre

conexion = psycopg2.connect(user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s' # Sirve para actualizar los registros en la base de datos
            valores = ('Juan Carlos', 'Roldan', 'rcarlos@mail.com', 1)
            cursor.execute(sentencia, valores)
            registros_actualizados = cursor.rowcount
            print(f'Los registros actualizados son: {registros_actualizados}')

except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
    
    