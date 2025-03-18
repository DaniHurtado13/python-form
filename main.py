from flask import Flask, request, jsonify, send_from_directory
from flask_pymongo import PyMongo
from bson import ObjectId
from flask_cors import CORS  


app = Flask(__name__)
CORS(app)
#CORS(app, resources={r"/*": {"origins": "*"}})


app.config["MONGO_URI"] = "mongodb://localhost:27017/Juegos"
mongo = PyMongo(app)
db = mongo.db.juegosDB

@app.route('/')
def index():
    return send_from_directory('.', 'form.html')

# 📌 Crear un nuevo juego
@app.route('/Juegos', methods=['POST'])  
def add_games():
    data = request.json
    if not data or not all(k in data for k in ['nombre', 'genero', 'año_lanzamiento', 'copias_vendidas']):
        return jsonify({"error": "Faltan datos"}), 400

    juego = {
        "nombre": data["nombre"],
        "genero": data["genero"],
        "año_lanzamiento": int(data["año_lanzamiento"]),
        "copias_vendidas": int(data["copias_vendidas"])
    }    

    inserted_id = db.insert_one(juego).inserted_id
    return jsonify({"message": "Juego agregado", "id": str(inserted_id)})

# 📌 Obtener todos los juegos
@app.route('/Juegos', methods=['GET'])
def get_games():
    juegos = []
    for juego in db.find():
        juego['_id'] = str(juego['_id'])
        juegos.append(juego)
    return jsonify(juegos)  # ⬅️ Antes devolvías solo 'juego', ahora es toda la lista

# 📌 Actualizar un juego
@app.route('/Juegos/<id>', methods=['PUT'])
def update_games(id):
    data = request.json
    if not data: 
        return jsonify({"error": "Datos no encontrados"}), 400
    
    update_data = {}
    if "nombre" in data:
        update_data["nombre"] = data["nombre"]
    if "genero" in data:
        update_data["genero"] = data["genero"]
    if "año_lanzamiento" in data:
        update_data["año_lanzamiento"] = int(data["año_lanzamiento"])
    if "copias_vendidas" in data:  # ⬅️ Ahora permite actualizar copias vendidas
        update_data["copias_vendidas"] = int(data["copias_vendidas"])

    update = db.update_one({"_id": ObjectId(id)}, {"$set": update_data})    

    if update.modified_count > 0:
        return jsonify({"message": "Juego actualizado"})
    return jsonify({"error": "No se encontró el juego"}), 400

# 📌 Eliminar un juego
@app.route('/Juegos/<id>', methods=['DELETE'])
def delete_juego(id):
    deleted = db.delete_one({"_id": ObjectId(id)})
    
    if deleted.deleted_count > 0:
        return jsonify({"message": "Juego eliminado"})
    return jsonify({"error": "Juego no encontrado"}), 404

# 📌 Ejecutar API
if __name__ == '__main__':
    app.run(debug=True)
