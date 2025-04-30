# Define una función que calcule el factorial de un número entero positivo.

def factorial(numero):
    # Verifico si el número es negativo
    if numero < 0:
        return "El número debe ser positivo"
    # Si el número es 0, retorno 1
    elif numero == 0:
        return 1

    resultado = 1
    # Recorro desde 1 hasta el número ingresado y multiplico el resultado por el número actual
    for i in range(1, numero + 1):
        print(resultado)
        resultado *= i
    return resultado

print(factorial(5))
