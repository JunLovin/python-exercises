# Escribe una función que determine si una cadena de texto dada es un palíndromo.

def es_palindromo(texto):
    # Reviso si el usuario insertó un string, de otra forma imprimo un error y retorno
    if not texto or not isinstance(texto, (str)):
        print("Por favor, ingresa un texto")
        return
    # Guardo el texto ingresado al usuario al revés en una variable
    # "".join Es para transformar a texto el resultado de reversed(texto), ya que, reversed(texto) no me devuelve un string, es como utilizar range(). Tengo que transformarlo primero, y como la función str() no funcionaba, utilicé "".join() para hacerla un texto.
    texto_alreves = "".join(reversed(texto))
    # Convierto ambos textos en minúscula para no perder ningún detalle en la comparación
    texto_minuscula = texto.lower()
    texto_alreves_minuscula = texto_alreves.lower()
    # Muestro en pantalla una comparativa para los usuarios y que puedan ver si es un palíndromo o no
    print(f"Texto normal: {texto}")
    print(f"Texto al revés: {texto_alreves}")

    # Si ambos textos condiciden retorno True y muestro un mensaje de éxito
    if texto_minuscula == texto_alreves_minuscula:
        print("El texto es palíndromo")
        return True
    # Si no son iguales retorno False y muestro un mensaje de error
    else:
        print("El texto no es palíndromo")
        return False

es_palindromo("14389")