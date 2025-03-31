# 🎮 CRUD de Videojuegos con Flask + MongoDB
API RESTful para gestionar un catálogo de videojuegos con operaciones CRUD completas, conectada a MongoDB y consumida desde un frontend HTML/JavaScript.

🌟 Características
 - Operaciones CRUD completas (Create, Read, Update, Delete)
 - Validación de datos en backend
 - API RESTful con respuestas JSON estandarizadas
 - Frontend independiente que consume la API
 - CORS habilitado para desarrollo frontend
   
## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

### Pre-requisitos 📋

Que cosas necesitas para instalar el software

```
Python 3.11 en adelante
Git
mongodb
```

### Instalación 🔧

1. Clonar repositorio
```
git clone https://github.com/DaniHurtado13/python-form.git
cd python-form
```
<br>

2. Configurar entorno virtual
```
- python -m venv venv
- venv\Scripts\activate
```

<br>

3. Instalar dependencias
```
pip install -r requirements.txt
```

<br>

4. Ejecutar aplicación en la terminal
```
Run python file, esquina superior derecha
Ejecutamos sobre el archivo main.py
```


## 📚 Documentación de la API

```
Endpoints
Método	   Ruta	        Descripción	 Ejemplo de Body
----------------------------------------------------
POST	   /Juegos	Crear nuevo juego JSON ↓
----------------------------------------------------
GET	    /Juegos	Obtener los juegos	-
----------------------------------------------------
PUT     /Juegos/<id>	Actualizar juego  JSON (parcial)
----------------------------------------------------
DELETE	 /Juegos/<id>	Eliminar juego	-

```

_Ejemplo de JSON (POST/PUT)
```
{
    "nombre": "The Legend of Zelda",
    "genero": "Aventura",
    "año_lanzamiento": 2017,
    "copias_vendidas": 20000000
}
```

### 📦 Estructura del Proyecto
```
.
├── app.py                # API Flask
├── form.html             # Frontend principal
├── requirements.txt      # Dependencias Python
└── README.md             # Este archivo
```

<br>

## Construido con 🛠️

* [Flask](https://flask.palletsprojects.com/en/stable/) - Framework web
* [MongoDB](https://www.mongodb.com/) - Conexión a Azure SQL
* [BootStrap](https://getbootstrap.com/) -  Estilos básicos

