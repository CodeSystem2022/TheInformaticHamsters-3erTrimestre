'''
Clase 11: Pool de conexiones con Python y Postgresql Parte 2
Laboratorio III: PYTHON
Team: The Informatic Hamsters
Scrum Master: Marcelo Alejandro Quispe
'''
# 11.1 Método liberarConexion()-Alumno: Marcelo Alejandro Quispe

from psycopg2 import pool
# psycopg2 as bd otra manera de importar el psycopg2
from logger_base import log
import sys


class Conexion:
    _DATABASE = 'test_bd'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = "127.0.0.1"
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexion obtenida del pool: {conexion}')
        return conexion



    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,
                                                      cls._MAX_CON,
                                                      user=cls._HOST,
                                                      host=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE)
                log.debug(f'creacion del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error al obtener el pool: {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod      # video 1
    def liberarConexion(cls, conexion):   # video 1
            cls.obtenerPool().putconn(conexion)     # video 1
            log.debug(f'Regresamos la conexion del pool: {conexion}')    #video 1

    @classmethod      #video 2
    def cerrarConexiones(cls):    #video 2
        cls.obtenerPool().closeall()   #video 2

if __name__ == '__name__':
   conexion1 = Conexion.obtenerConexion()
   Conexion.liberarConexion(conexion1)
   conexion2 = Conexion.obtenerConexion()
   Conexion.liberarConexion(conexion2)
   conexion3 = Conexion.obtenerConexion()
   Conexion.liberarConexion(conexion3)
   Conexion4 = Conexion.obtenerConexion()
   conexion5 = Conexion.obtenerConexion()
   conexion6 = Conexion.obtenerConexion()
