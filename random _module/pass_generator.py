# Generador de contraseñas

import random
import string

# - Crear una función que genere una contraseña aleatoria con la longitud que le pasemos.
def generar_contrasena(longitud):
    # ? Si la longitud es menor a 1, devuelvo un mensaje de error
    if longitud < 1:
        return 'La longitud debe ser mayor a 0'

    # ? Creo una variable que va a contener la contraseña
    password = ''

    # ? Recorro un rango de 0 hasta la longitud de la contraseña
    for i in range(longitud):
        # ? Genero una caracter random de la lista de caracteres, números y símbolos
        password+=random.choice(string.ascii_letters + string.punctuation + string.digits)

    #? Devuelvo la contraseña
    return password


print(generar_contrasena(10))