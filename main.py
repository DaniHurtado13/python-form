from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson import ObjectId
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

app.config["MONGO_URI"] = "mongodb://localhost:27017/users"
mongo = PyMongo(app)
db = mongo.db.users

@app.route('/users', methods=['POST'])  
def add_user():
    data = request.json
    if not data or not all (k in data for k in ['nombre', 'edad', 'correo']):
        return jsonify({"error": "Faltan datos"}), 400

    user = {
        "nombre": data["nombre"],
        "edad": int(data["edad"]),
        "correo": data["correo"]
    }    

    inserted_id = db.insert_one(user).inserted_id
    return jsonify({"message": "Usuario agregado", "id": str(inserted_id)})



@app.route('/users', methods=['GET'])
def get_users():
    users = []
    for user in db.find():
        user['_id'] = str(user['_id'])
        users.append(user)
    return jsonify(users)    


@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.json
    if not data: 
        return jsonify({"error": "Datos no encontrados"}), 400
    
    update_data = {}
    if "nombre" in data:
        update_data["nombre"] = data["nombre"]
    if "edad" in data:
        update_data["edad"] = int(data["edad"])
    if "correo" in data:
        update_data["correo"] = data["correo"]

    update = db.update_one({"_id": ObjectId(id)}, {"$set": update_data})    

    if update.modified_count > 0:
        return jsonify({"message": "Usuario Actualizado"})
    return jsonify({"error": "No se encontro"}), 400


@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    deleted = db.delete_one({"_id": ObjectId(id)})
    
    if deleted.deleted_count > 0:
        return jsonify({"message": "Usuario eliminado"})
    return jsonify({"error": "Usuario no encontrado"}), 404


if __name__ == '__main__':
    app.run(debug=True)
