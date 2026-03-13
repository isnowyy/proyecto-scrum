# TaskFlow CLI

## Descripción del proyecto

TaskFlow CLI es una aplicación de línea de comandos desarrollada en Python que permite gestionar tareas personales desde la terminal de forma rápida y sencilla. El sistema fue diseñado para ayudar a los usuarios a organizar sus actividades diarias sin necesidad de utilizar aplicaciones gráficas complejas.

La aplicación permite registrar nuevas tareas, visualizar las tareas existentes, marcar tareas como completadas y eliminar tareas que ya no sean necesarias. Toda la información se almacena en un archivo JSON, lo que permite mantener los datos guardados de manera persistente incluso después de cerrar el programa.

Este proyecto fue desarrollado como parte de un ejercicio  enfocado en la aplicación del marco de trabajo SCRUM para planificar, organizar y documentar el desarrollo de un producto mínimo viable (MVP).


## Planteamiento del problema

En muchas ocasiones las personas necesitan organizar sus tareas diarias, pero no siempre cuentan con herramientas simples que puedan utilizar rápidamente desde la terminal. Muchas aplicaciones de gestión de tareas son demasiado complejas o requieren interfaces gráficas que consumen más recursos.

Además, cuando las tareas se anotan en diferentes lugares o se gestionan de forma desordenada, es más fácil olvidar actividades importantes o perder el control sobre lo que se debe realizar.

Por esta razón surge la necesidad de una herramienta sencilla que permita gestionar tareas de manera rápida, organizada y persistente desde la consola.


## Objetivo del sistema

El objetivo principal del sistema es desarrollar una aplicación de consola que permita a los usuarios gestionar sus tareas de forma simple y eficiente. A través de este sistema el usuario podrá crear nuevas tareas, visualizar las tareas registradas, marcar tareas como completadas y eliminar aquellas que ya no sean necesarias.

El sistema también busca mantener la información almacenada localmente mediante el uso de archivos JSON para asegurar la persistencia de los datos.


## Solución propuesta

La solución consiste en desarrollar TaskFlow CLI, una aplicación ejecutada desde la terminal que permite administrar tareas personales de manera rápida y eficiente.

El sistema permite crear tareas, listarlas, actualizar su estado a completado y eliminarlas cuando ya no sean necesarias. Toda la información se guarda en un archivo JSON, lo que permite que los datos permanezcan almacenados y puedan ser cargados nuevamente cuando el programa se ejecute.

De esta manera se ofrece una solución simple para la gestión básica de tareas utilizando únicamente la línea de comandos.



## Funcionalidades implementadas

El sistema incluye las siguientes funcionalidades principales:

- Crear nuevas tareas
- Listar todas las tareas registradas
- Marcar tareas como completadas
- Eliminar tareas existentes
- Guardar tareas en un archivo JSON
- Cargar las tareas almacenadas al iniciar el programa

Estas funcionalidades permiten construir un producto mínimo viable funcional que cumple con los requisitos definidos en las historias de usuario.



## Tecnologías utilizadas

Para el desarrollo del proyecto se utilizaron las siguientes tecnologías:

- Python como lenguaje de programación principal
- JSON para el almacenamiento de datos
- Git para el control de versiones
- GitHub para el repositorio del proyecto
- SCRUM como metodología ágil para la organización del trabajo



## Instalación y ejecución

Para ejecutar el proyecto es necesario tener Python instalado en el sistema.

1. Clonar el repositorio desde GitHub.
2. Abrir la terminal y ubicarse en la carpeta del proyecto.
3. Ejecutar el programa utilizando el siguiente comando:

python main.py

Una vez ejecutado el programa, el usuario podrá interactuar con el sistema desde la terminal para gestionar sus tareas.



## Comandos disponibles

El sistema permite realizar las siguientes acciones desde la consola:

- Crear una nueva tarea
- Visualizar la lista de tareas registradas
- Marcar una tarea como completada
- Eliminar una tarea existente

Estas acciones permiten al usuario mantener un control básico de sus actividades pendientes.



## Estructura del proyecto

El proyecto está organizado de la siguiente manera:

proyecto-scrum/

README.md  
main.py  
tasks.json  
product_backlog.md  
historias_usuario.md  

documentacion/

La carpeta de documentación contiene las evidencias del proceso SCRUM realizado durante el desarrollo del proyecto.


## Integrantes del equipo y roles SCRUM

Los integrantes de nuestro equipo y sus roles dentro del marco de trabajo SCRUM son los siguientes:

Nicolas Naranjo —  Product Owner 
Julian Agudelo — Scrum Master
Pedro Diaz — Developer 1
Juan Jose —  Developer 2
Julieth Rojas - Developer 3 

Cada integrante participó en la planificación, desarrollo y documentación del proyecto.


## Aplicación de SCRUM en el proyecto

Durante el desarrollo del proyecto se aplicó el marco de trabajo SCRUM para organizar el proceso de trabajo del equipo.

Inicialmente se definieron los roles SCRUM dentro del equipo. Posteriormente se identificó el problema a resolver y se construyó el Product Backlog con las historias de usuario necesarias para el desarrollo del sistema.

A partir del Product Backlog se planificó el sprint y se seleccionaron las historias que serían desarrolladas para construir el MVP del sistema. El trabajo fue organizado mediante un tablero Kanban utilizando una herramienta de gestión ágil, lo que permitió visualizar el estado de cada tarea.

Durante el proceso se realizaron ceremonias SCRUM como Sprint Planning, Daily Stand-up, Sprint Review y Sprint Retrospective, las cuales permitieron hacer seguimiento al avance del proyecto y mejorar continuamente el proceso de trabajo del equipo.


## Reflexión final

El desarrollo de este proyecto permitió aplicar de manera práctica los conceptos de metodologías ágiles y del marco de trabajo SCRUM en el desarrollo de software.

A través de la planificación mediante historias de usuario, la organización del trabajo mediante backlog y sprints, y la colaboración entre los integrantes del equipo, fue posible desarrollar un producto mínimo viable funcional.

Este proyecto también permitió comprender la importancia de la comunicación, la organización del trabajo y la mejora continua dentro de un equipo de desarrollo.