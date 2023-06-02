import psycopg2 as bd # Esto es para poder conectarnos a Postgre

conexion = bd.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    #conexion.autocommit = False # al no hacer un commit no se guarda los cambios, si ponemos true no es una buena practica, esta liena no deberia estar
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    valores = ('Maria', 'Esparza', 'mesparza@mail.com')
    cursor.execute(sentencia, valores) #conexion
    conexion.commit() # hacemos el commit manualmente porque no se agrego el registro a la base de datos
    print('Termina la transacción')
except Exception as e:
    conexion.rollback() # no se guarda nada en la bd
    print(f"Ocurrió un error, se hizo un rollback: {e}")
finally:
    conexion.close()
    