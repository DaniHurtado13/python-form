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

2. Configurar entorno virtual
```
- python -m venv venv
- venv\Scripts\activate
```

3. Instalar dependencias
```
pip install -r requirements.txt
```

4. Configurar base de datos
   ° Crear archivo .env en /src con:
```
DB_SERVER="tpc:tu-servidor.database.windows.net"
DB_DATABASE="nombre-db"
DB_USER="tu-usuario"
DB_PASSWORD="tu-contraseña"
DB_DRIVER="ODBC Driver 17 for SQL Server"
DB_PORT="1433" // Opcional
```
  ° Configurar firewall en Azure Portal para permitir tu IP

5. Ejecutar aplicación en la terminal
```
python src/app.py
```
_Finaliza con un ejemplo de cómo obtener datos del sistema o como usarlos para una pequeña demo_

## Ejecutando las pruebas ⚙️

_Explica como ejecutar las pruebas automatizadas para este sistema_

### Analice las pruebas end-to-end 🔩

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

### Y las pruebas de estilo de codificación ⌨️

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

## Despliegue 📦

_Agrega notas adicionales sobre como hacer deploy_

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [Maven](https://maven.apache.org/) - Manejador de dependencias
* [ROME](https://rometools.github.io/rome/) - Usado para generar RSS

## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/tu/proyecto/wiki)

## Versionado 📌

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/tu/proyecto/tags).

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Andrés Villanueva** - *Trabajo Inicial* - [villanuevand](https://github.com/villanuevand)
* **Fulanito Detal** - *Documentación* - [fulanitodetal](#fulanito-de-tal)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/your/project/contributors) quíenes han participado en este proyecto. 

## Licencia 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo. 
* Da las gracias públicamente 🤓.
* Dona con cripto a esta dirección: `0xf253fc233333078436d111175e5a76a649890000`
* etc.



---
⌨️ con ❤️ por [Villanuevand](https://github.com/Villanuevand) 😊

https://gist.github.com/Villanuevand/6386899f70346d4580c723232524d35a#file-readme-espanol-md
