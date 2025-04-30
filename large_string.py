# Crea una función que tome una lista de palabras y devuelva la palabra más larga

def palabra_mas_larga(lista):
    # Verifico si la lista está vacía
    if not lista:
        return "La lista está vacía"
    
    # Inicializo la variable palabra_larga con la primera palabra de la lista
    palabra_larga = lista[0]

    # Recorro la lista de palabras y comparo la longitud de cada palabra con la longitud de la palabra inicializada
    for palabra in lista:
        if len(palabra) > len(palabra_larga):
            palabra_larga = palabra

    return palabra_larga

print(palabra_mas_larga(["hola", "adios", "que", "tal", "estas"]))