# - Crear una función que reciba una lista de números y devuelva una lista conteniendo solo los números pares.

# Sin lists comprehension

def devolver_pares(lista):
    lista_final = []

    for numero in lista:
        if ((numero % 2) == 0):
            lista_final.append(numero)
            
    return lista_final

lista = [2, 4, 6, 7, 8, 120, 3, 9, 13]

print(devolver_pares(lista))

# Con lists comprehension

def devolver_pares_lists_comprehension(lista): return [numero for numero in lista if (numero % 2) == 0]

print(devolver_pares_lists_comprehension(lista))