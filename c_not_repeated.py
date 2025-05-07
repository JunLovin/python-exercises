# Escribe una función que encuentre el primer carácter no repetido en una cadena.

# - Defino una función llamada no_repetido que recibe un argumento: texto.
def no_repetido(texto):
    # ? Reviso si el texto es válido, si no lo es devuelvo un mensaje de error.
    if len(texto) == 0:
        return "Por favor, ingresa un texto válido."
    # ? Inicializo una variable llamada letra_no_repetida que va a contener la letra no repetida.
    letra_no_repetida = ""
    # ? Convierto el texto a minúscula y elimino los espacios en blanco
    texto_lower = texto.lower().strip()
    # ? Inicializo un diccionario
    diccionario = {}

    #? Recorro el texto y voy guardando cada letra en el diccionario
    for c in texto_lower:
        # ? Si la letra no está en el diccionario la inicializo en 1, sino la aumento en 1
        if c not in diccionario:
            diccionario[c] = 1
        else:
            diccionario[c] += 1
    # ? Recorro el diccionario y si la letra está en el diccionario y su valor es 1, la guardo en letra_no_repetida
    for c in diccionario:
        if diccionario[c] == 1:
            letra_no_repetida = c
            # ? Devuelvo la letra no repetida
            return letra_no_repetida
            break
    # ? Si no hay letra no repetida devuelvo un string vacío
    return ""

print(no_repetido("aabbcddee"))