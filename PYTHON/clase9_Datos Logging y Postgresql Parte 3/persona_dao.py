'''
Clase 9: Capa de Datos Logging y Postgresql Parte 3
Laboratorio III: PYTHON
Team: The Informatic Hamsters
Scrum Master: Nadia Yanella Acosta
'''


from capa_datos.log.conexion import Conexion
import Persona


#  9.1 En la clase PersonaDao: método seleccionar: Alumno Miguel Rodriguez Saquilan

class PersonaDAO:
    """
    DAO significa: data access Object
    CRUD Significa:
                   Create ->  Insertar
                   Read   ->  Seleccionar
                   Update ->  Actualizar
                   Delete ->  Eliminar
    """

    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(id_persona,nombre, apellido, email) VALUES(%,%,%)'
    _ACTUALIZAR = ' UPDATE persona SET nombre=%s, apellido=%s, email=%s, WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    # definimos los metodos de clase 
    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fechall()
                personas = []
                for registro in registros:
                    persona = Persona(registro[0],registro[1], registro[2],registro[3])
                    personas.append(persona)

