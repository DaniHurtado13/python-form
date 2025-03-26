from flask import Flask, render_template, request, redirect, url_for
import os 
import pyodbc
from dotenv import load_dotenv
from database import get_db_connection

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')
env_path = os.path.join(template_dir, 'src', '.env')


app = Flask(__name__, template_folder=template_dir)
load_dotenv(env_path)

def get_db_connection():
    try:
        conn = pyodbc.connect(
            f"DRIVER={os.getenv('DB_DRIVER')};"
            f"SERVER={os.getenv('DB_SERVER')};"
            f"DATABASE={os.getenv('DB_DATABASE')};"
            f"UID={os.getenv('DB_USER')};"
            f"PWD={os.getenv('DB_PASSWORD')}"
        )
        return conn
    except pyodbc.Error as e:
        print(f"❌ Error de conexión: {e}")
        return None  # Devuelve None en caso de error


@app.route('/')
def index():
    return render_template('home.html')



# Ruta principal
@app.route('/index.html')
def home():
    conn = get_db_connection()
    if conn is None:
        return "Error de conexión a la base de datos", 500
    try:
        # Obtener conexión a la base de datos
        cursor = conn.cursor()
        
        # Ejecutar consulta
        cursor.execute('SELECT * FROM carro')
        column_names = [column[0] for column in cursor.description]
        data = [dict(zip(column_names, row)) for row in cursor.fetchall()]
        return render_template('index.html', data=data)
    except pyodbc.Error as e:
        return f"Error en consulta: {str(e)}", 500
    finally:
        if 'cursor' in locals():
            cursor.close()
        if conn:
            conn.close()

@app.route('/car', methods=['POST'])
def addCar():
    modelo = request.form['modelo']
    color = request.form['color']
    año = request.form['año']
    marca = request.form['marca']

    if modelo and color and año and marca:
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO carro (modelo, color, año, marca) VALUES (?, ?, ?, ?)"
        data = (modelo, color, año, marca)
        cursor.execute(sql, data)
        conn.commit()
    return redirect(url_for('home'))


@app.route('/delete/<string:id>')
def delete(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM carro WHERE id = ?"
    data = (id)
    cursor.execute(sql, data)
    conn.commit()
    return redirect(url_for('home'))


@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    modelo = request.form['modelo']
    color = request.form['color']
    año = request.form['año']
    marca = request.form['marca']

    if modelo and color and año and marca:
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "UPDATE carro SET modelo = ?, color = ?, año = ?, marca = ? WHERE id = ?"
        data = (modelo, color, año, marca, id)
        cursor.execute(sql, data)
        conn.commit()
        return redirect(url_for('home'))
    else: 
        return "Todos los campos son obligatorios", 400



if __name__ == '__main__':
    app.run(debug=True, port=4000)