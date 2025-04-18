# Taller DB

## Descripción

Taller DB es un proyecto de aplicación web desarrollado con Django, un framework de Python. El proyecto permite a los usuarios registrarse, iniciar sesión y actualizar sus datos.

## Instalación

Para instalar el proyecto, sigue los siguientes pasos:

1. Clona el repositorio:

    ```bash
    git clone <https://github.com/JuanS3/taller-db.git>
    ```

2. Crea un entorno virtual:

   ```bash
    python -m venv venv
    ```

3. Activa el entorno virtual:

    ```bash
    source venv/bin/activate
    ```

4. Instala las dependencias:

   ```bash
    pip install -r requirements.txt
    ```

5. Configura la base de datos:

    ```bash
    python manage.py migrate
    ```

## Ejecución

Para ejecutar el proyecto, sigue los siguientes pasos:

1. Activa el entorno virtual:

    ```bash
    source venv/bin/activate
    ```

2. Inicia el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

3. Abre un navegador y accede a `http://127.0.0.1:8000/`

## Características

* Registro de usuarios
* Inicio de sesión
* Actualización de datos de usuario
* Autenticación y autorización con Django
