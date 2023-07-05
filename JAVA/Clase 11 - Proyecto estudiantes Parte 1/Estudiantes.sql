
-- Comenzamos con CRUD: create(inseertar), read(leer), update(actualizar), delete(eliminar)
-- Listar los estudiantes (read)
SELECT * FROM estudiantes2022;
-- Insertar estudiante
INSERT INTO estudiantes2022(nombre, apellido, telefono, email) VALUES ("Juan", "Perez", "123456", "jperez@mail.com");
-- Update (modificar)
UPDATE estudiantes2022 SET nombre="Juan Carlos", apellido="Garcia" WHERE idestudiantes2022=1;
-- Delete (eliminar)
DELETE FROM estudiantes2022 WHERE idestudiantes2022=5; 
-- Para modificar el idestudiantes2022 y comience con 1
ALTER TABLE estudiantes2022	AUTO_INCREMENT = 1;