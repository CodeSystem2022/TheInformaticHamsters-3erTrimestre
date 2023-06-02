# Una transacción puede leer una o más sentencias que modifiquen el estado de la base de datos. 
# Al tener una sentencia de tipo INSERT se puden agregar más, por lo que después de ejecutar la primer sentencia se ejecutará una más.  

import psycopg2 as bd # Esto es para poder conectarnos a Postgre

conexion = bd.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
   # conexion.autocommit = False # Esto directamente no debería estar, inicia la transaccion
   cursor = conexion.cursor()
   sentencia = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'
   valores = ('Carlos', 'Lara', 'clara@mail.com')
   cursor.execute(sentencia, valores)

   sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
   valores = ('Juan', 'Juarez', 'jjuarez@mail', 1)
   cursor.execute(sentencia, valores) # incorporamos la sentencia y valores a la ejecucion

   conexion.commit() # Hacemos el commit manualmente, se cierra la transacción
   print('Termina la transacción')
except Exception as e:
    conexion.rollback()
    print(f"Ocurrió un , se hizo un rollback: {e}")
finally:
    conexion.close()
