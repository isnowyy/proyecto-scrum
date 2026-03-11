# Product Backlog – TaskFlow CLI

## 1. Nombre del proyecto
TaskFlow CLI

## 2. Problema del proyecto
Muchas personas necesitan organizar sus actividades diarias, pero no siempre cuentan con una herramienta rápida, simple y accesible para hacerlo desde la terminal. En muchos casos, las tareas se anotan en distintos lugares o se olvidan, lo que dificulta el seguimiento de pendientes.

Por esta razón, se propone desarrollar una aplicación de consola que permita gestionar tareas de forma sencilla, almacenando la información localmente para que el usuario pueda consultarla y actualizarla en cualquier momento.

## 3. Objetivo del sistema
Desarrollar una aplicación de línea de comandos llamada TaskFlow CLI que permita a los usuarios gestionar tareas de forma simple y persistente, mediante funciones de creación, consulta, actualización y eliminación de tareas almacenadas en un archivo JSON.

## 4. Objetivo del producto
Permitir a los usuarios registrar, consultar, completar y eliminar tareas desde la terminal, conservando la información entre ejecuciones del programa.

## 5. Product Backlog priorizado

| ID  | Ítem del Product Backlog | Descripción | Prioridad |
|-----|---------------------------|-------------|-----------|
| PB1 | Crear tareas | El sistema debe permitir registrar nuevas tareas desde la terminal. | Alta |
| PB2 | Listar tareas | El sistema debe mostrar todas las tareas registradas. | Alta |
| PB3 | Guardar tareas en JSON | Las tareas deben almacenarse en un archivo JSON para conservar la información. | Alta |
| PB4 | Cargar tareas al iniciar | Al iniciar el programa, el sistema debe leer las tareas guardadas previamente. | Alta |
| PB5 | Marcar tareas como completadas | El usuario debe poder cambiar el estado de una tarea a completada. | Alta |
| PB6 | Eliminar tareas | El usuario debe poder borrar tareas que ya no necesite. | Alta |
| PB7 | Asignar prioridad a tareas | El usuario podrá establecer prioridad baja, media o alta a una tarea. | Media |
| PB8 | Filtrar tareas | El sistema podrá mostrar tareas según estado o prioridad. | Media |
| PB9 | Editar tareas | El usuario podrá modificar el nombre o prioridad de una tarea existente. | Media |
| PB10 | Vista tipo Kanban en consola | El sistema podrá mostrar tareas agrupadas por estado. | Baja |

## 6. Observaciones
Los ítems PB1 a PB6 corresponden al MVP mínimo requerido para el proyecto. Los demás ítems se consideran funcionalidades opcionales para futuras iteraciones o sprints adicionales.