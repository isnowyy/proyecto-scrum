# Historias de Usuario – TaskFlow CLI

## Historia 1
**Como** usuario,  
**quiero** crear tareas,  
**para** registrar mis actividades pendientes.

### Criterios de aceptación
- El sistema debe permitir ingresar el nombre de una tarea desde la terminal.
- Cada tarea creada debe tener un identificador único.
- La tarea creada debe guardarse en el archivo JSON.
- La tarea debe aparecer al listar las tareas.

---

## Historia 2
**Como** usuario,  
**quiero** listar mis tareas,  
**para** visualizar mis actividades registradas.

### Criterios de aceptación
- El sistema debe mostrar todas las tareas almacenadas.
- Cada tarea debe mostrar al menos su ID, nombre y estado.
- Si no existen tareas, el sistema debe informar que no hay tareas registradas.

---

## Historia 3
**Como** usuario,  
**quiero** marcar una tarea como completada,  
**para** llevar control de mi progreso.

### Criterios de aceptación
- El sistema debe permitir seleccionar una tarea mediante su ID.
- La tarea seleccionada debe cambiar su estado a completada.
- El cambio debe guardarse en el archivo JSON.
- Al volver a listar, la tarea debe aparecer como completada.

---

## Historia 4
**Como** usuario,  
**quiero** eliminar tareas,  
**para** mantener actualizada mi lista de pendientes.

### Criterios de aceptación
- El sistema debe permitir eliminar una tarea mediante su ID.
- La tarea eliminada no debe volver a aparecer en la lista.
- El cambio debe guardarse en el archivo JSON.
- Si el ID no existe, el sistema debe mostrar un mensaje de error.

---

## Historia 5
**Como** usuario,  
**quiero** que mis tareas se guarden automáticamente,  
**para** no perder la información al cerrar el programa.

### Criterios de aceptación
- Todas las tareas deben almacenarse en un archivo JSON.
- El archivo JSON debe actualizarse cada vez que se cree, complete o elimine una tarea.
- La información debe permanecer disponible después de cerrar el programa.

---

## Historia 6
**Como** usuario,  
**quiero** que mis tareas se carguen al iniciar el programa,  
**para** continuar gestionándolas sin tener que volver a ingresarlas.

### Criterios de aceptación
- Al iniciar el programa, el sistema debe leer el archivo JSON existente.
- Las tareas guardadas previamente deben cargarse correctamente.
- Si el archivo no existe, el sistema debe iniciar con una lista vacía sin generar error.

---

## Historias opcionales

## Historia 7
**Como** usuario,  
**quiero** asignar prioridad a una tarea,  
**para** identificar cuáles actividades son más importantes.

### Criterios de aceptación
- El sistema debe permitir asignar prioridad baja, media o alta.
- La prioridad debe almacenarse en el archivo JSON.
- La prioridad debe visualizarse al listar tareas.

---

## Historia 8
**Como** usuario,  
**quiero** filtrar tareas por estado o prioridad,  
**para** consultar solo las tareas que me interesan.

### Criterios de aceptación
- El sistema debe permitir aplicar filtros por estado.
- El sistema debe permitir aplicar filtros por prioridad.
- El listado debe mostrar únicamente las tareas que cumplan el filtro seleccionado.

---

## Historia 9
**Como** usuario,  
**quiero** editar una tarea,  
**para** corregir o actualizar su información.

### Criterios de aceptación
- El sistema debe permitir modificar el nombre de una tarea existente.
- El sistema debe permitir modificar su prioridad, si aplica.
- Los cambios deben guardarse en el archivo JSON.

---

## Historia 10
**Como** usuario,  
**quiero** visualizar mis tareas en formato tipo Kanban en consola,  
**para** entender mejor su estado actual.

### Criterios de aceptación
- El sistema debe agrupar tareas por estado.
- Las tareas deben mostrarse organizadas visualmente en la terminal.
- La visualización debe diferenciar entre pendientes y completadas.
