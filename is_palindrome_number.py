def isPalindrome(x):
    # Convertir a string
    n_str = str(x)
    # Inicializo una lista
    n_list = []

    # Recorro la longitud del string y agrego cada caracter a la lista
    for i in range(0, len(n_str)):
        n_list.append(n_str[i])

    # Invierto la lista y la convierto a string
    n_list.reverse()
    n_reverse = ''.join(n_list)

    # Comparo si el string original es igual al string invertido
    if n_str == n_reverse:
        print("Palindromo")
        return True
    else:
        print("No es palindromo")
        return False

isPalindrome(385)