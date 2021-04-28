from flask import Flask, request, send_file
from flask_cors import CORS
# Se importa el archivo users.py
import users
import csv
import os
from reports import user_report_live

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

# app.config['UPLOAD_FOLDER'] = 'C:\\Users\\dalex\\github\\UHospitalBackend'

# Ruta inicial de la API, saluda al mundo
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Ruta inicial de la API, saluda al mundo
@app.route('/', methods=["POST"])
def cargar():
    file = request.files["entrada_csv"]
    file.save("entrada.csv")
    read_csv("entrada.csv")   
    return 'Hello, World!'


def read_csv(path):
    with open(path, mode='r', encoding="utf-8-sig") as csv_file:
        csv_reader = csv.DictReader(csv_file, fieldnames=["username", "email"])
        for row in csv_reader:
            # print(row["contraseña"])
            users.add_user(row["username"], row["email"])

@app.route('/report_user', methods=["GET"])
def report_user():
    filename = "usuarios.pdf"
    all_users = users.get_all_users()
    user_report_live.create_user_report(filename, all_users)
    return send_file(filename)








# Enviar un reporte
@app.route('/report', methods=["GET"])
def send_report():
    return send_file("report.pdf", attachment_filename="user_report.pdf")

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(port=5000)