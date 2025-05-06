# Encuentra el número que falta, tomando en cuenta que solo falta 1.

# Escribe una función que tome una lista de números enteros y devuelva el número que falta en la secuencia.
def encontrar_numero(lista_de_numeros):
    # Verifico si la lista está vacía
    if len(lista_de_numeros) == 0:
        return "Por favor, ingresa una lista con números"
    # Inicializo una variable en donde guardaré el número faltante.
    n_faltante = 0
    # Recorro la lista de números
    # min(lista_de_numeros): Devuelve el número más pequeño de la lista
    # max(lista_de_numeros): Devuelve el número más grande de la lista
    for i in range(min(lista_de_numeros), max(lista_de_numeros)):
        # Si el número no está en la lista, lo devuelvo
        if i not in lista_de_numeros:
            return i
    return None

print(encontrar_numero([1, 2, 3, 5, 6, 7, 8, 9, 10]))