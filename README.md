# YUHU BACKEND

## Objetivos del Proyecto

El objetivo de YUHU Backend es construir una API funcional para la gestión de tareas, que permita a los usuarios realizar las siguientes acciones:

- **Crear** una nueva tarea con título, email y descripción.
- **Leer** la lista de tareas existentes.
- **Actualizar** una tarea (modificar título y/o descripción).
- **Eliminar** una tarea existente.

### Funcionalidades Adicionales

- **Fechas de Vencimiento**: Asignar una fecha de vencimiento opcional para cada tarea.
- **Paginación**: Implementar paginación en la lista de tareas para facilitar la navegación cuando hay muchas tareas.
- **Documentación API**: Documentar el uso de la API utilizando Postman, Swagger/OpenAPI o en formato Markdown.
- **Servicios AWS**: Utilizar servicios de la capa gratuita de AWS.

## Arquitectura y Tecnologías

### Backend
- **Tecnologías**: Django, Django REST Framework (DRF), Celery
- **Infraestructura**: AWS EC2, Nginx, Gunicorn

### Frontend
- **Tecnologías**: Vue, Quasar
- **Infraestructura**: AWS EC2

## Endpoints y URLs


- **URL Frontend**: [http://3.16.13.233/task](http://3.16.13.233/task)


- **URL Backend**: [http://18.223.180.179/](http://18.223.180.179/)
- **Documentación API**:
  - [Swagger UI](http://18.223.180.179/swagger/)
  - [ReDoc UI](http://18.223.180.179/redoc/)
  - [Descargar esquema JSON (swagger.json)](http://18.223.180.179/swagger.json)

## Idioma de la Aplicación

- **English**

© Jesús Eduardo Robles Duana 