from flask import Flask, request
from flask_cors import CORS
# Se importa el archivo users.py
import users
import csv
import os

# Se crea una instancia de Flask
app = Flask(__name__)
# Se habilitan los CORS para que cualquier servidor se conecte
CORS(app)

# Se ejecuta cuando un cliente llama a /usuarios con POST
@app.route('/usuarios', methods=["POST"])
def api_agregar_users():
    body = request.json
    username = body["username"]
    email = body["email"]
    return users.add_user(username, email)

# Se ejecuta cuando un cliente llama a /usuarios con GET
@app.route('/usuarios', methods=["GET"])
def api_get_users():
    return users.get_users()

# Se ejecuta cuando un cliente llama a /usuarios/<username> con GET
# Recibe en la ruta un username dinamico
@app.route('/usuarios/<username>', methods=["GET"])
def api_get_user(username):
    return users.get_user(username)

# Se ejecuta cuando un cliente llama a /usuarios/<username> con DELETE
# Recibe en la ruta un username dinamico
@app.route('/usuarios/<username>', methods=["DELETE"])
def api_delete_user(username):
    return users.delete_user(username)

# Se ejecuta cuando un cliente llama a /usuarios/<username> con PUT
# Recibe en la ruta un username dinamico
@app.route('/usuarios/<username>', methods=["PUT"])
def api_update_user(username):
    body = request.json
    # Recibe en el body el nuevo email
    new_email = body["email"]
    return users.update_user(username, new_email)

app.config['UPLOAD_FOLDER'] = 'C:\\Users\\dalex\\github\\UHospitalBackend'

# Ruta inicial de la API, saluda al mundo
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Ruta inicial de la API, saluda al mundo
@app.route('/', methods=["POST"])
def cargar():
    file = request.files["entrada_csv"]
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], "entrada.csv"))
    read_csv("entrada.csv")   
    return 'Hello, World!'


def read_csv(path):
    with open(path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row["username"])
            print(row["email"])
            users.add_user(row["username"], row["email"])