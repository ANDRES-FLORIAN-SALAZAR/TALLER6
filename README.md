# Taller DB

## Descripción

Taller DB es un proyecto de aplicación web desarrollado con Django, un framework de Python. Este proyecto permite a los usuarios registrarse, iniciar sesión y actualizar sus datos de manera segura.

## Instalación

Sigue estos pasos para instalar el proyecto:

1. Clona el repositorio:

    ```bash
    git clone https://github.com/ANDRES-FLORIAN-SALAZAR/TALLER6.git
    ```

2. Crea un entorno virtual:

    ```bash
    python -m venv venv
    ```

3. Activa el entorno virtual:

    - En Linux/MacOS:

        ```bash
        source venv/bin/activate
        ```

    - En Windows:

        ```bash
        venv\Scripts\activate
        ```

4. Instala las dependencias necesarias:

    ```bash
    pip install -r requirements.txt
    ```

5. Configura la base de datos ejecutando las migraciones:

    ```bash
    python manage.py migrate
    ```

## Ejecución

Para ejecutar el proyecto, realiza los siguientes pasos:

1. Activa el entorno virtual:

    - En Linux/MacOS:

        ```bash
        source venv/bin/activate
        ```

    - En Windows:

        ```bash
        venv\Scripts\activate
        ```

2. Inicia el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

3. Abre un navegador y accede a `http://127.0.0.1:8000/`.

## Características

* Registro de usuarios con validación de datos.
* Inicio de sesión seguro.
* Actualización de datos de usuario.
* Autenticación y autorización utilizando el sistema integrado de Django.
* Gestión de sesiones para proteger la información del usuario.

## Notas adicionales

Asegúrate de tener Python 3.8 o superior instalado en tu sistema. Además, verifica que `pip` esté actualizado antes de instalar las dependencias:

```bash
pip install --upgrade pip
```
