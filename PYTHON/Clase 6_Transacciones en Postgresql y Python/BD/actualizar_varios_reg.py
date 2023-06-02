import psycopg2 # Esto es para conecar a PostgreSQL.tuve que instalar paquete.

#creo una variable para la conexion
conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test:bd'
)
try:
    with conexion:
        with conexion.cursor() as cursor: #DE ESTA MANERA YA NO TENEMOS QUE CERRAR NOSOSTROS EL CURSOR
            cursor=conexion.cursor()
            sentencia='UPDATE persona SET nombre=%s , apellido=%s , email = %s WHERE id_persona=%s'
            valores=(('Juan','Perez','jperez@mail.com',4),('Romina','Ayala','rayala@mail.com',5),)
        #es una Tupla de Tuplas
            cursor.executemany(sentencia,valores) #para ejecutar la sentencia que pasé como tupla
            registros_actualizados = cursor.rowcount #para recuperar todos los registros de la 'sentencia' que seran una lista
            print(f'Los registros actualizados son: {registros_actualizados}')


except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
    conexion.close()
    