'''
Clase 10: Pool de conexiones con Python y Postgresql
Laboratorio III: PYTHON
Team: The Informatic Hamsters
Scrum Master: Giuliana Paola Diaz Luna
'''


# 10.1 POOL DE CONEXIONES CON PYTHON Y POSTGRESQL: Parte 1 -- Alumno : Giuliana Paola Diaz Luna

# Un pool de conexiones es un objeto que va a administrar a su vez los objetos de conexion hacia la base de datos
# Podemos tener 1 o mas poll de conexiones y cada pool de conexion va a administrar un número determinado de objetos de conexion hacia la base de datos.
# Una vez que cierto cliente necesite de un objeto de conexion hacia la base de datos, lo va a obtener del pool de conexiones.
# Y una vez que ha terminado su proceso, lo libera y el objeto regresa al pool de conexiones para que otro cliente pueda seguir uilizando los objetos disponibles.
# Dos clientes no pueden utilizar al mismo momento el mismo objeto del pool de conexiones. Sino que utiliza otro objeto para hacer esa conexion.  


# 10.1 POOL DE CONEXIONES CON PYTHON Y POSTGRESQL: Parte 2 -- Alumno :



# 10.2 Obtener una conexión a partir del Pool: Parte 1 -- Alumno : Nadia Acosta

@classmethod
def obtenerPool(cls):
    if cls._pool is None:
        try:
            cls._pool = pool.SimpleConnection(cls._MIN_CON,
                                              cls._MAX_CON,
                                              host=cls._HOST,
                                              user=cls._USERNAME,
                                              password=cls._PASSWORD,
                                              port=cls._DB_PORT,
                                              database=cls._DATABASE)
        log.debug(f'creación del pool exitosa: {cls._pool}')
        except Exception as e:
            log.error(f'Ocurrio un error al obtener el pool: {e}')
            sys.exit()
        else:
             return cls._pool

# 10.2 Obtener una conexión a partir del Pool: Parte 2 -- Alumno :



# 10.3 Pruebas creando objetos del Pool de conexiones -- Alumno : Miguel Rodriguez Saquilan
if __name__  == '__main__':
    Conexion1 = Conexion.obtenerConexion()
    Conexion2 = Conexion.obtenerConexion()
    Conexion3 = Conexion.obtenerConexion()
    Conexion4 = Conexion.obtenerConexion()
    Conexion5 = Conexion.obtenerConexion()
    # si ponemos otra conexion nos pasamos de las 5 objetos que teniamos permitidos

    




