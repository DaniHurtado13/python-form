from flask import Flask, request, jsonify, send_from_directory
from flask_pymongo import PyMongo
from bson import ObjectId
from flask_cors import CORS  
from datetime import datetime
import pyodbc



app = Flask(__name__)
CORS(app)


DB_CONFIG = {
    "DRIVER": "{SQL Server}",
    "SERVER": "DESKTOP-SI63H0G",
    "DATABASE": "Games",
    "Trusted_Connection": "yes"
}

def get_connection():
    return pyodbc.connect(**DB_CONFIG)

@app.route('/')
def index():
    return send_from_directory('.', 'form.html')

# 📌 Crear un nuevo juego
@app.route('/Juegos', methods=['POST'])  
def add_games():
    data = request.json
    if not data or not all(k in data for k in ['nombre', 'genero', 'plataforma', 'precio', 'fecha_lanzamiento']):
        return jsonify({"error": "Faltan datos"}), 400

    try:
        fecha_lanzamiento = data["fecha_lanzamiento"]

        connection = get_connection()
        cursor = connection.cursor()

        sql = "INSERT INTO Juegos (nombre, genero, plataforma, precio, fecha_lanzamiento) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(sql, (data["nombre"], data["genero"], data["plataforma"], int(data["precio"]), fecha_lanzamiento))
        connection.commit()

        return jsonify({"message": "Juego agregado"})
    
    except ValueError:
        return jsonify({"error": "Formato de fecha inválido. Usa YYYY-MM-DD"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()

# 📌 Obtener todos los juegos
@app.route('/Juegos', methods=['GET'])
def get_games():
    try: 
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT id, nombre, genero, plataforma, precio, fecha_lanzamiento FROM Juegos")

        juegos_list = []
        for row in cursor.fetchall():
            juegos_list.append({
                "id": row.id,
                "nombre": row.nombre,
                "genero": row.genero,
                "plataforma": row.plataforma,
                "precio": row.precio,
                "fecha_lanzamiento": row.fecha_lanzamiento if isinstance(row.fecha_lanzamiento, str) else row.fecha_lanzamiento.strftime("%Y-%m-%d")
            })

        return jsonify(juegos_list) 

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# 📌 Actualizar un juego
@app.route('/Juegos/<id>', methods=['PUT'])
def update_games(id):
    data = request.json
    if not data: 
        return jsonify({"error": "Datos no encontrados"}), 400
    
    try: 
        connection = get_connection()
        cursor = connection.cursor()

        update_data = []
        sql_parts = []

        if "nombre" in data:
            sql_parts.append("nombre = ?")
            update_data.append(data["nombre"])
        if "genero" in data:
            sql_parts.append("genero = ?")
            update_data.append(data["genero"])
        if "plataforma" in data:
            sql_parts.append("plataforma = ?")
            update_data.append(data["plataforma"])
        if "precio" in data:
            sql_parts.append("precio = ?")
            update_data.append(int(data["precio"]))
        if "fecha_lanzamiento" in data:
            sql_parts.append("fecha_lanzamiento = ?")
            update_data.append(datetime.strptime(data["fecha_lanzamiento"], "%Y-%m-%d").date())

        if not update_data:
            return jsonify({"error": "No hay datos para actualizar"}), 400

        update_data.append(id)  # Agregar ID al final
        sql_query = f"UPDATE Juegos SET {', '.join(sql_parts)} WHERE id = ?"
        
        cursor.execute(sql_query, update_data)
        connection.commit()

        return jsonify({"message": "Juego actualizado correctamente"})
    
    except ValueError:
        return jsonify({"error": "Formato de fecha inválido. Usa YYYY-MM-DD"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()

# 📌 Eliminar un juego
@app.route('/Juegos/<id>', methods=['DELETE'])
def delete_juego(id):
    try: 
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("DELETE FROM Juegos WHERE id =?", (id,))
        connection.commit()

        if cursor.rowcount > 0:
            return jsonify({"message": "Juego eliminado correctamente"})
        return jsonify({"error": "juego no encontrado"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()

# 📌 Ejecutar API
if __name__ == '__main__':
    app.run(debug=True)
