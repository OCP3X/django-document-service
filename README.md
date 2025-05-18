Django Document Service
Un microservicio de gestión de documentos construido con Django y Django REST Framework (DRF). Este servicio permite subir, listar, consultar metadatos, descargar y eliminar archivos.
Características

Subir documentos (archivos) con metadatos automáticos
Listar todos los documentos disponibles
Obtener metadatos detallados de un documento específico
Descargar documentos
Eliminar documentos
API RESTful completa
Panel de administración para gestión manual de documentos
Despliegue con Docker y Kubernetes

Tecnologías utilizadas

Python 3.11
Django 4.x
Django REST Framework
PostgreSQL
Docker
Kubernetes

Estructura del proyecto
django-document-service/
├── docservice/               # Directorio principal del proyecto
│   ├── documents/            # Aplicación de documentos
│   │   ├── migrations/       # Migraciones de la base de datos
│   │   ├── admin.py          # Configuración del panel de administración
│   │   ├── apps.py           # Configuración de la aplicación
│   │   ├── models.py         # Definición del modelo Document
│   │   ├── serializers.py    # Serializadores para la API REST
│   │   ├── urls.py           # Definición de URLs para la API
│   │   └── views.py          # Vistas para manejar las solicitudes HTTP
│   ├── settings.py           # Configuración del proyecto Django
│   ├── urls.py               # Configuración de URLs principal
│   └── wsgi.py               # Punto de entrada WSGI
├── k8s/                      # Manifiestos de Kubernetes
│   ├── deployment.yaml       # Configuración de despliegue
│   ├── ingress.yaml          # Configuración de ingress
│   ├── pvc.yaml              # Configuración de volumen persistente
│   ├── secret.yaml           # Configuración de secretos
│   └── service.yaml          # Configuración de servicio
├── media/                    # Directorio para almacenar los archivos subidos
├── .dockerignore             # Archivos excluidos del contexto de Docker
├── .gitignore                # Archivos excluidos del control de versiones
├── docker-compose.yml        # Configuración para Docker Compose
├── Dockerfile                # Definición de la imagen Docker
├── manage.py                 # Utilidad de línea de comandos de Django
├── README.md                 # Este archivo
└── requirements.txt          # Dependencias del proyecto
Requisitos previos

Python 3.11
PostgreSQL
Docker (opcional para desarrollo local, requerido para despliegue)
Kubernetes (opcional, solo para despliegue)

Configuración del entorno de desarrollo
1. Clonar el repositorio
bashgit clone https://github.com/tu-usuario/django-document-service.git
cd django-document-service
2. Crear un entorno virtual
bashpython -m venv .venv
# En Windows
.\.venv\Scripts\activate
# En MacOS/Linux
source .venv/bin/activate
3. Instalar dependencias
bashpip install -r requirements.txt
4. Configurar la base de datos PostgreSQL
Crea una base de datos PostgreSQL:
bash# Usando psql
createdb document_service
Actualiza las credenciales en docservice/settings.py o configura variables de entorno:
pythonDATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'document_service',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
5. Aplicar migraciones
bashpython manage.py makemigrations
python manage.py migrate
6. Crear superusuario
bashpython manage.py createsuperuser
7. Ejecutar el servidor de desarrollo
bashpython manage.py runserver
La aplicación estará disponible en http://localhost:8000/
Uso de la API
Endpoints disponibles

GET /documents/: Listar todos los documentos
POST /documents/: Subir un nuevo documento
GET /documents/{id}/: Obtener metadatos de un documento específico
GET /documents/{id}/download/: Descargar un documento específico
DELETE /documents/{id}/: Eliminar un documento específico

Ejemplos de uso
Subir un documento
bashcurl -X POST -F "file=@/ruta/al/archivo.pdf" http://localhost:8000/documents/
Listar documentos
bashcurl http://localhost:8000/documents/
Obtener metadatos de un documento
bashcurl http://localhost:8000/documents/1/
Descargar un documento
bashcurl -O http://localhost:8000/documents/1/download/
Eliminar un documento
bashcurl -X DELETE http://localhost:8000/documents/1/
Despliegue con Docker
Usando Docker Compose
bashdocker-compose build
docker-compose up
La aplicación estará disponible en http://localhost:8000/
Despliegue en Kubernetes
1. Construir y subir la imagen Docker
bashdocker build -t tu-registro/document-service:latest .
docker push tu-registro/document-service:latest
2. Actualizar la imagen en deployment.yaml
Edita kubernetes/deployment.yaml y actualiza la imagen:
yamlimage: tu-registro/document-service:latest
3. Aplicar los manifiestos de Kubernetes
bashkubectl apply -f kubernetes/pvc.yaml
kubectl apply -f kubernetes/secret.yaml
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
kubectl apply -f kubernetes/ingress.yaml
4. Verificar el despliegue
bashkubectl get pods
kubectl get services
kubectl get ingress
Desarrollo
Ramas principales

main: Rama principal estable
feat/microservice: Rama de desarrollo principal
feat/scaffolding: Rama para la estructura inicial del proyecto (fusionada a main)

Contribuir al proyecto

Crea una nueva rama desde main
Realiza tus cambios
Crea un pull request a main