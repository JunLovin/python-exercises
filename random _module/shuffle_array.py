# Función para barajar una lista

import random

# - Crear una función que reciba una lista de números y devuelva una lista barajada.
def shuffle(lista):
    # ? Si la lista está vacía o tiene un solo elemento, devuelvo la lista
    if not lista or len(lista) <= 1:
        return lista

    # ? Guardo la longitud de la lista y creo una lista vacía para guardar los números barajados
    lista_temporal = lista.copy()
    longitud = len(lista_temporal)
    lista_final = []

    # ? Recorro un rango de 0 hasta la longitud de la lista
    for i in range(longitud):
        # ? Genero un número random entre 0 y la longitud de la lista - 1
        numero_random = random.randint(0, longitud - 1)
        # ? Agrego el número random a la lista final y lo elimino de la lista original
        lista_final.append(lista_temporal[numero_random])
        # !: Es importante eliminar el número de la lista original para que no se repita y disminuir la longitud de la lista original para que no se repita el número random en el siguiente ciclo
        lista_temporal.pop(numero_random)
        # ? Resto 1 a la longitud de la lista
        longitud -= 1

    # ? Devuelvo la lista final
    return lista_final

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)
print(shuffle(lista))

