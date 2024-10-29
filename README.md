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

- **URL Backend**: [http://18.116.26.70:8000/](http://18.116.26.70:8000/)
- **Documentación API**:
  - [Swagger UI](http://18.116.26.70:8000/swagger/)
  - [ReDoc UI](http://18.116.26.70:8000/redoc/)
  - [Descargar esquema JSON (swagger.json)](http://18.116.26.70:8000/swagger.json)

## Configuración y Ejecución

Para desplegar YUHU Backend, asegúrate de que tu entorno tiene configuradas las siguientes dependencias y configuraciones:

1. **AWS EC2**: Instancias para alojar el backend y el frontend.
2. **Nginx**: Configurado como proxy reverso para gestionar solicitudes al servidor Gunicorn.
3. **Gunicorn**: Servidor WSGI para ejecutar la aplicación Django.
4. **Celery**: Configurado para manejo de tareas en segundo plano.

## Idioma de la Aplicación

- **English**