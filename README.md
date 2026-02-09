# Catálogo de Productos Django

Sistema de gestión de productos con autenticación, exportación PDF y diseño moderno.

## Instalación en Producción (Linux)

1.  **Clonar y configurar entorno**:

    ```bash
    git clone <tu-repo>
    cd Django-test
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2.  **Configurar Variables de Entorno**:
    Crea un archivo `.env` o exporta las variables:

    ```bash
    export DEBUG=False
    export SECRET_KEY='tu_clave_super_secreta'
    export ALLOWED_HOSTS='*'  # O tu dominio
    # Configuración de base de datos...
    ```

3.  **Preparar Archivos Estáticos**:
    Esto reunirá todos los CSS/imágenes en la carpeta `staticfiles`:

    ```bash
    python manage.py collectstatic
    ```

4.  **Ejecutar con Gunicorn**:
    Levantar el servidor en el puerto 8000:
    ```bash
    gunicorn simple_project.wsgi:application --bind 0.0.0.0:8000
    ```
    _Para dejarlo corriendo en background, se recomienda usar `supervisor` o `systemd`._

## Desarrollo Local (Windows)

1.  **Instalar dependencias**:

    ```bash
    pip install -r requirements.txt
    ```

2.  **Ejecutar servidor de prueba**:
    ```bash
    python manage.py runserver
    ```

## Comandos Útiles

- **Crear base de datos y tablas**:
  ```bash
  python manage.py migrate
  ```
- **Poblar datos de prueba**:
  ```bash
  python manage.py seed_products
  ```
- **Crear admin**:
  ```bash
  python manage.py createsuperuser
  ```
