from flask import Response
import json

# Lista que guarda usuarios
users = []

# Agrega un usuario a la lista
def add_user(username, email):
    users.append({
        "username": username,
        "email": email
    })
    # Se retornan el status 201 que significa Created
    return Response(status=201)

# Retorna la lista completa de usuarios
def get_users():
    return Response(json.dumps(users), mimetype='application/json')

# Busca el usuario con el username indicado y lo devuelve
def get_user(username):
    for user in users:
        if user["username"] == username:
            return Response(json.dumps(user), mimetype='application/json')
    # Retorna status 404 que significa NotFound
    return Response(status=404)

# Busca el usuario con el username indicado y lo elimina
def delete_user(username):
    for user in users:
        if user["username"] == username:
            users.remove(user)
            # Retorna el status 204 que significa NoContent
            return Response(status=204)
    # Retorna status 404 que significa NotFound
    return Response(status=404)

# Busca el usuario con el username indicado y actualiza el email
def update_user(username, new_email):
    for user in users:
        if user["username"] == username:
            user["email"] = new_email
            # Retorna el status 200 que significa OK
            return Response(status=200)
    # Retorna status 404 que significa NotFound
    return Response(status=404)