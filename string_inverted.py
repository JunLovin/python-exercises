# Implementa una función para invertir una cadena de texto sin usar funciones built-in ni métodos como slicing.

# - Defino una función llamada invertir que recibe un argumento: texto.
def invertir(texto):
    if len(texto) == 0:
        return "Por favor, ingresa un texto válido."
    # ? Inicializo una variable llamada texto_invertido que va a contener el texto invertido
    texto_invertido = ""
    # ? Guardo la longitud del texto en una variable
    texto_len = len(texto)

    # ? Recorro el texto de atrás hacia adelante y voy guardando cada letra en texto_invertido
    for c in range(texto_len - 1, -1, -1):
        texto_invertido += texto[c]

    # ? Devuelvo el texto invertido
    return texto_invertido

print(invertir("prueba"))