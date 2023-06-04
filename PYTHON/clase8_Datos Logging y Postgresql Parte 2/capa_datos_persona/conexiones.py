'''
Clase 8: Capa de Datos Logging y Postgresql Parte 2
Laboratorio III: PYTHON
Team: The Informatic Hamsters
Scrum Master: Miguel Rodriguez Saquilan
'''

# lo que se importe va aca arriba corroborar que no se importe dos veces
import psycopg2 as bd

from logger_base import log 
 
import sys


# 8.3 Creación de la Clase Conexion: Parte 1 -- Alumno Miguel Rodriguez Saquilan

class Conexion:
    _DATABASE = 'test_bd'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _conexion = None
    _cursor = None



#8.3 Creación de la Clase Conexion: Parte 2 -- Alumno : Nadia Acosta

@classmethod 
def obtenerConexion(cls):
    if cls._conexion is None:
        try: 
            cls._conexion = bd.connect(host=cls._HOST,
                                        user=cls._USERNAME,
                                        password=cls._PASSWORD,
                                        port=cls._DB_PORT,
                                        database=cls._DATABASE)
            log.debug(f'Conexion exitosa: {cls._conexion}')
            return cls._conexion
        except Exception as e:
            log.error(f'Ocurrio un error: {e}')
            sys.exit()
    else:
        return cls._conexion

# 8.3 Creación de la Clase Conexion: Parte  3 -- Alumno: Juan Pablo Nolan

@classmethod
def obtenerCursor(cls):
    if cls._cursor is None:
        try:
            cls._cursor = cls.obtenerConexion().cursor()
            log.debug(f'Se abrio correctamente el cursor: {cls._cursor}')
            return cls._cursor
        except  Exception as e:
            log.error(f'Ocurrio un error de tipo: {e}')
            sys.exit()
    else:
        return cls._cursor

if __name__ == '__main__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()