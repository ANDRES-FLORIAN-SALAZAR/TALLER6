Proyecto de Auditoría de Operaciones en Usuarios
Descripción del Proyecto
Este proyecto implementa un sistema de auditoría para la tabla principal usuarios, mediante la creación de tablas históricas (_log) y triggers en la base de datos. Las tablas históricas registran datos sobre operaciones realizadas, como inserciones, actualizaciones y eliminaciones, asegurando un seguimiento completo de las modificaciones.

Estructura de las Tablas
Tabla usuarios_insert_log
Registra nuevos usuarios creados.

Campo	Descripción
id	Identificador único
datos_originales	Información del usuario insertado
fecha_evento	Fecha y hora del evento
usuario_autenticado	Usuario que realizó la operación
Tabla usuarios_update_log
Registra actualizaciones realizadas sobre los usuarios.

Campo	Descripción
id	Identificador único
datos_originales	Información previa a la actualización
tipo_operacion	Tipo de operación realizada
fecha_evento	Fecha y hora del evento
usuario_autenticado	Usuario que realizó la operación
Tabla usuarios_delete_log
Registra usuarios eliminados.

Campo	Descripción
id	Identificador único
datos_originales	Información del usuario eliminado
fecha_evento	Fecha y hora del evento
usuario_autenticado	Usuario que realizó la operación
Implementación de Triggers
Trigger de Inserción
Al crear un nuevo usuario, se registra la información en usuarios_insert_log.

Trigger de Actualización
Al modificar un usuario, se registra la información previa en usuarios_update_log.

Trigger de Eliminación
Al eliminar un usuario, se registra la información en usuarios_delete_log.

Pruebas Funcionales
Se realizaron pruebas desde la interfaz de Django (y directamente sobre SQL, en caso necesario) para verificar:

La ejecución correcta de las operaciones (crear, actualizar, eliminar usuarios).

El almacenamiento de datos esperados en las tablas históricas (_log).

Ejemplos de Registros
Tabla usuarios_insert_log
id	datos_originales	fecha_evento	usuario_autenticado
1	{"nombre": "Juan"}	2025-04-19 10:00:00	admin
Tabla usuarios_update_log
id	datos_originales	tipo_operacion	fecha_evento	usuario_autenticado
1	{"nombre": "Juan"}	Actualización	2025-04-19 10:10:00	admin
Tabla usuarios_delete_log
id	datos_originales	fecha_evento	usuario_autenticado
1	{"nombre": "Juan"}	2025-04-19 10:20:00	admin
Dificultades Encontradas y Soluciones
Manejo de errores en triggers
Se implementó manejo de transacciones para asegurar consistencia en los datos.

Captura del usuario autenticado
Se utilizó una variable de sesión para pasar el usuario desde Django a la base de datos.
