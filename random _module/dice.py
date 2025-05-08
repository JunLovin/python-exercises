# Simulación de dados
import random

# - Función que simula tirar un dado n número de veces
def tirar_dado(veces):
    # ? Si las veces son menor o igual a 0, devuelvo un mensaje de error
    if veces <= 0:
        return 'No se puede tirar el dado 0 o menos veces'

    # ? Creo un diccionario con los números del 1 al 6 y los inicializo en 0
    numeros = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
    }

    # ? Recorro un rango de 0 hasta las veces
    for i in range(veces):
        # ? Genero un número random aleatorio entre 1 y el numero mayor del diccionario números
        n = random.randint(1, max(numeros))
        # ? Sumo 1 al número que salió
        numeros[n]+=1

    # ? Devuelvo el diccionario con los números y la cantidad de veces que salió cada número
    return numeros

print(tirar_dado(3))