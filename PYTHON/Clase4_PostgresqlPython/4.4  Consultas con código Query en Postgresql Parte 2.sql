-- Consultas con código Query en Postgresql Parte 2 - Alumna: Giuliana Paola Diaz Luna
-- Para ejecutar selecciono la sentencia y F5 (no hace falta comentar)

-- SELECT *  FROM persona WHERE id_persona = 1
SELECT *  FROM
SELECT *  FROM persona WHERE id_persona in(1,2,3)

--insertar informacion a la tabla
INSERT INTO persona(nombre,apellido,email)VALUES('Susana','Lara','slara@mail.com')

--Modificar un valor
UPDATE persona SET nombre = 'Ivonne',apellido = 'Esparza', email='iesparza@mail.com' WHERE id_persona = 3

-- Consultamos los cambios
SELECT *  FROM persona

-- Eliminar registros
DELETE FROM persona -- elimina todos los registros
DELETE FROM persona WHERE id_persona =3

-- Consultamos la eliminacion del registro
SELECT *  FROM persona
