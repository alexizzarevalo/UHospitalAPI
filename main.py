users = []

def add_user(user):
    print("Voy a agregar un usuario")
    users.append(user)

def get_user():
    print("Obteniendo usuario")

add_user(1)
add_user(2)
add_user(3)
print(users)