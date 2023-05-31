'''
Clase 8: Capa de Datos Logging y Postgresql Parte 2
Laboratorio III: PYTHON
Team: The Informatic Hamsters
Scrum Master: Miguel Rodriguez Saquilan
'''
 
import sys


# 8.3 Creación de la Clase Conexion: Parte 1 -- Alumno



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

# 8.3 Creación de la Clase Conexion: Parte  3 -- Alumno