# Escribe un programa que determine si un número entero positivo dado es un número de Armstrong.

# LOS ENTEROS NO SON ITERABLES.

def verificar_si_es_armstrong(numero):
    # Si el número es menor o igual a 0, deuvelvo False
    if numero <= 0:
        return False
    
    # Convierto el número a string para sacar su length ya que no se puede sacar len() si es entero
    numero_str = str(numero)
    # Guardo el length del número
    length = len(numero_str)
    # Inicializo la suma
    suma = 0

    # Recorro un rango de 0 hasta el length del número
    for i in range(length):
        # Sumo la potencia del número elevado al length del número
        # Ej: suma = suma + 1^3 + 5^3 + 3^3
        # suma = suma + 1 + 125 + 27
        # suma = 153
        suma += int(numero_str[i]) ** length
    
    # Si la suma es igual al número, devuelvo True, sino False.
    if suma == numero:
        return True
    else:
        return False

numero = 153
print(verificar_si_es_armstrong(numero))
