'''
Clase 7: Capa de Datos Logging y Postgresql Parte 1
Laboratorio III: PYTHON
Team: The Informatic Hamsters
Scrum Master: Marcelo Alejandro Quispe
'''





# 7.1 Explicación con el diagrama de clase UML (Tarea: hacer el diagrama UML) -- Alumno : 



# 7.2 Manejo de logging: Parte 1   - Alumno: Miguel Rodriguez Saquilan
import logging as log

# llamamos una configuracion basica
log.basicConfig(level=log.DEBUG)



# 7.3 Manejo de logging: Parte 2  - Alumno: Giuliana Paola Diaz Luna

import logging as log

log.basicConfig(level=log.DEBUG,
                # muestra fecha y hora, nivel, nombre del archivo, linea que se ejecuto y mensaje que se envia
                format='%(asctime)s:%(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                # formato de la fecha
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ]
                )

# 7.5 Video de otro proyecto llamado: Partículas -Alumno:





