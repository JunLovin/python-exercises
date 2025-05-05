# Implementa una función que genere los primeros n números de la secuencia de Fibonacci.

def fibonacci(n):
    # Verifico si n es menor o igual a 0, en cuyo caso devuelvo una lista vacía.
    if n <= 0:
        return []
    # Verifico si n es igual a 1, en cuyo caso devuelvo una lista con el número 0.
    elif n == 1:
        return [0]

    # Inicializo una lista con los primeros dos números de la secuencia de Fibonacci.
    fib = [0, 1]
    # Genero los siguientes números de la secuencia de Fibonacci y los agrego a la lista.
    while len(fib) < n:
        # fib[-1]: El último número de la lista fib.
        # fib[-2]: El penúltimo número de la lista fib.
        # Agrego la suma de los dos últimos números de la lista fib
        fib.append(fib[-1] + fib[-2])

    return fib

n = int(input("Ingrese la cantidad de números de Fibonacci que desea generar: "))
fib_nums = fibonacci(n)
print(fib_nums)