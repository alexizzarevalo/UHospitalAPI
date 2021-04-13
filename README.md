# Crear entorno de desarrollo

> Estos comandos fueron ejecutados en `Powershell` de Windows
 
Crear un entorno virtual

```ps
python3 -m venv venv
```

Activar el entorno virtual

```ps
.\venv\Scripts\activate
```

Instalar las dependencias

```ps
pip install -r requirements.txt
```

# Correr la API

Agregar una variable de entorno con el nombre del archivo inicial

```ps
$env:FLASK_APP = "main.py"
```

Correr el servidor de Flask

```ps
flask run
```

# Comandos de GIT

Inicializar un repositorio local
    
    git init

Verificar el estado de mis archivos

    git status

Agregar cambios al stage

    git add <nombre de los archivos a agregar>

Hacer un commit

    git commit -m "Aqui va el mensaje descriptivo"

Ver el historial de cambios o commits

    git log

Subir cambios a Github

    git push origin main

Cambios Locales   ->  Area de stage  -> Commit

# REST API
 
Utiliza JSON como estandar

## Protocolo HTTP

### Verbos o metodos HTTP

[Ver mas acerca de metodos de peticion](https://developer.mozilla.org/es/docs/Web/HTTP/Methods)

- GET: Obtener algo
- POST: Guardar algo
- PUT: Modificar algo
- DELETE: Eliminar algo

### Codigos de respuesta

[Ver mas acerca de codigos de respuesta](https://developer.mozilla.org/es/docs/Web/HTTP/Status)
- Respuestas informativas (100–199),
- Respuestas satisfactorias (200–299),
- Redirecciones (300–399),
- Errores de los clientes (400–499),
- Errores de los servidores (500–599).

Ejemplos:

- 200: OK
- 201: Created
- 204: No Content
- 400: Bad Request
- 404: Not Found
- 405: Method Not Allowed
- 409: Conflict
- 500: Internal Server Error
- 501: Not Implemented
