'''
Clase 11: Pool de conexiones con Python y Postgresql Parte 2
Laboratorio III: PYTHON
Team: The Informatic Hamsters
Scrum Master: Marcelo Alejandro Quispe

'''

# 11.4 Pruebas del CursorDelPool -> Parte 1 y 2 --  Alumno : Miguel Rodriguez Saquilan


from capa_datos_persona.Persona import Persona
from capa_datos_persona.conexion import Conexion

from capa_datos_persona.cursor_del_pool import CursorDelPool
from logger_base import log


class PersonaDAO:
    """
    DAO  significa : Data Access Object
    CRUD significa :
                    Create  --> Insertar
                    Read    --> Seleccionar
                    Update  --> Actualizar
                    Delete  --> Eliminar
    """
    _SELECCIONAR    = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR       = 'INSERT INTO persona( nombre, apellido, email) VALUES (%s, %s, %s)'
    _ACTUALIZAR     = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    _ELIMINAR       = 'DELETE FROM persona WHERE id_persona = %s'

    # Definicion de los metodos de clase
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.excecute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []  # Creamos una lista
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas




    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Persona Insertada:  {persona}')
            return cursor.rowcount




    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona actualizada : {persona}')
            return cursor.rowcount




    @classmethod
    def eliminar(cls, persona ):
        with CursorDelPool() as cursor :
            valores = (persona.id_persona)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f' Los objetos eliminados son: {persona}')
            return cursor.rowcount


# 11.5 Pruebas de personaDAO -> Parte 1 -- Alumno: Juan Pablo Nolan
# 11.5 Pruebas de personaDAO -> Parte 2 -- Alumna: Giuliana Paola Diaz Luna
if __name__ == '__main__':
    # Eliminar registro
    personas1 = Persona(id_persona=18)
    personas_eliminadas = PersonaDAO.eliminar(personas1)
    log.debug(f' Personas eliminadas : {personas_eliminadas}')


    #Actualizar un registro
    persona1 = Persona(1, 'Juan', 'Pena', 'jpena@mail.com')
    personas_actualizadas = PersonaDAO.actualizar(persona1)
    log.debug(f' Personas actualizadas : {personas_actualizadas}')



    # Insertar un registro
    persona1 = Persona(nombre = 'Mateo', apellido= 'Torres', email='Tmateo@mail.com')
    personas_insertadas = PersonaDAO.insertar(persona1)
    log.debug(f'Personas insertadas: {personas_insertadas}')


# Seleccionar Objetos
personas = PersonaDAO.seleccionar()
for persona in personas:
            log.debug(persona)
