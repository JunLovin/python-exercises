# Escribe una función que tome una cadena de texto como entrada y devuelva una un diccionario con la frecuencia de cada carácter en la cadena.

def string_to_dict(string):
    new_dict = {}
    for letra in string:
        # Forma para verificar si un valor existe EN UN DICCIONARIO
        if letra in new_dict:
            new_dict[letra] += 1
        else:
            new_dict[letra] = 1
    return new_dict

# También se puede conÑ

def string_to_dict_with_dict_methods(texto):
    nuevo_diccionario = {}
    for letra in texto:
        # nuevo_diccionario.get intenta obtener el valor asociado a letra. Si letra ya está en el diccionario, devuelve su valor actual; si no está, devuelve 0 (nuestro valor por defecto para empezar con el conteo). Luego simplemente sumamos uno para que el valor por defecto sea 1
        # La syntaxis es: diccionario.get(clave, valor_por_defecto)
        # Si la clave existe devuelve el valor, sino crea la clave y le asigna el valor por defecto que pongamos
        nuevo_diccionario[letra] = nuevo_diccionario.get(letra, 0) + 1
    return nuevo_diccionario

print(string_to_dict("hello"))

print(string_to_dict_with_dict_methods("vayaina"))