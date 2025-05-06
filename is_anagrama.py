# Verifica si una cadena es anagrama de otra.

# Defino una función llamada es_anagrama que recibe dos argumentos: palabra1 y palabra2.
def es_anagrama(palabra1, palabra2):
    palabra1_lower = palabra1.lower().strip()
    palabra2_lower = palabra2.lower().strip()
    # Inicializo dos diccionarios, cada uno palabra su respectiva palabra
    diccionario1 = {}
    diccionario2 = {}

    # Recorro cada letra de la palabra1 y si está en el diccionario aumento su valor, sino la inicializo en 1
    for i in palabra1_lower:
        if i in diccionario1:
            diccionario1[i] += 1
        else:
            diccionario1[i] = 1
    
    # Recorro cada letra de la palabra2 y si está en el diccionario aumento su valor, sino la inicializo en 1
    for i in palabra2_lower:
        if i in diccionario2:
            diccionario2[i] += 1
        else:
            diccionario2[i] = 1

    # Comparo los dos diccionarios y si son iguales retorno True, sino False
    if diccionario1 == diccionario2:
        return True
    else:
        return False

print(es_anagrama("amor", "roma"))