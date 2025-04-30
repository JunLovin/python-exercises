# Implementa una función que reciba dos listas y devuelva una lista con los elementos comunes entre ambas.

def devolver_listas_comunes(primer_lista, segunda_lista):
    lista_final = []
    for elemento in primer_lista:
        for segundo_elemento in segunda_lista:
            if elemento == segundo_elemento:
                lista_final.append(elemento)

    return lista_final

lista_uno = [2, 4, "texto", "bacano", 9, 12]
lista_dos  = [2, 4, "notexto", "no bacano", "10", 12]

print(devolver_listas_comunes(lista_uno, lista_dos))