'''
Clase 11: Pool de conexiones con Python y Postgresql Parte 2
Laboratorio III: PYTHON
Team: The Informatic Hamsters
Scrum Master: Marcelo Alejandro Quispe

'''

# 11.3 Creamos la Clase CursorDelPool -> Parte 1 y 2 -- Alumno : Nadia Acosta

from logger_base import log
from conexion import Conexion

class CursorDelPool:
    def __int__(self):
        self._conexion = None
        self._cursor = None


    def __enter__(self):
        log.debug('Inicio del metodo with y __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_exception, valor_exception, detalle_exception):
        log.debug('Se ejecuta el metodo exit')
        if valor_exception:
            self._conexion.rollback()
            log.debug(f'Ocurrio una exception: {valor_exception}')
        else:
            self._conexion.commit()
            log.debug('Commit de la transaccion')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

# 11.4 Pruebas del CursorDelPool -> Parte 1 y 2 --  Alumno : Miguel Rodriguez Saquilan

if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM persona')
        log.debug(cursor.fetchall())
