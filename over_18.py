# Escribe una función que reciba una lista de diccionarios, donde cada diccionario representa a una persona con las claves "nombre" y "edad". La función debe devolver la lista de nombres de las personas mayores de 18 años.

def over_18(personas):
    # Utilizo la función filter junto con una función lambda para filtrar las personas mayores de 18 años y devolver una lista con las personas que cumplan la condición
    return list(filter(lambda persona: persona["edad"] > 18, personas))

personas = [{ "nombre": "Juan", "edad": 20 }, { "nombre": "María", "edad": 17 }, { "nombre": "Pedro", "edad": 19 }]

print(over_18(personas))