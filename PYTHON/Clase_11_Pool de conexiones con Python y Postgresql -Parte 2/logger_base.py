'''
Clase 11: Pool de conexiones con Python y Postgresql Parte 2
Laboratorio III: PYTHON
Team: The Informatic Hamsters
Scrum Master: Marcelo Alejandro Quispe

'''

import logging as log
#  Llamamos una configuracion basica

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s:%(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log', encoding='utf8'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug   ('Mensaje a nivel debug')
    log.info    ('Mensaje a nivel info')
    log.warning ('Mensaje nivel warning')
    log.error   ('Mnesaje nivel error')
    log.critical('Mensaje nivel critical')
