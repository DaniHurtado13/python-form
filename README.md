# 🚗 Sistema CRUD de Vehículos con Flask y Azure SQL
Aplicación web para gestionar un inventario de automóviles con operaciones CRUD completas, desarrollada con:

Backend: Python + Flask

Base de datos: Azure SQL (conexión segura mediante ODBC)

Frontend: HTML/CSS + Bootstrap básico

Seguridad: Credenciales protegidas con .env

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

### Pre-requisitos 📋

Que cosas necesitas para instalar el software

```
Python 3.11 en adelante
Git
Azure SQL
ODBC Driver 17 > Es necesario para la conexión a base de datos
```

### Instalación 🔧

1. Clonar repositorio
```
git clone https://github.com/DaniHurtado13/python-form.git
cd python-form
git checkout SQLCrud
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

4. Configurar base de datos <br>
   - Crear archivo .env en /src con:
```
DB_SERVER="tpc:tu-servidor.database.windows.net"
DB_DATABASE="nombre-db"
DB_USER="tu-usuario"
DB_PASSWORD="tu-contraseña"
DB_DRIVER="ODBC Driver 17 for SQL Server"
DB_PORT="1433" // Opcional
```
  - Configurar firewall en Azure Portal para permitir tu IP



5. Ejecutar aplicación en la terminal
```
python src/app.py
```


## ⚙️ Estructura del Proyecto

```
/src
├── app.py                # Lógica principal
├── database.py           # Conexión a Azure SQL
├── requirements.txt      # Dependencias
/templates
└── index.html            # Vista principal
```


### 🛠️ Funcionalidades Clave

_✔ CRUD completo de vehículos <br>
✔ Validación de año (4 dígitos) <br>
✔ Mensajes flash de confirmación/error <br>
✔ Conexión segura a Azure SQL_ 

<br>

### 🚨 Solución de Problemas Comunes
_Error de conexión a Azure SQL_
```
pyodbc.OperationalError: ('08001', '[08001] [Microsoft][ODBC Driver 17...')
```

Solución:
   1. Verificar que el firewall de Azure permita tu IP actual
   2. Confirmar que el string de conexión incluya tcp:

```
DB_SERVER="tcp:tu-servidor.database.windows.net"
```

## Construido con 🛠️

* [Flask](https://flask.palletsprojects.com/en/stable/) - Framework web
* [PyODBC](https://github.com/mkleehammer/pyodbc) - Conexión a Azure SQL
* [BootStrap](https://getbootstrap.com/) -  Estilos básicos

