# Caesar Cypher

# ? Creo un array que contendrá todas las letras del abecedario
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# ? Creo una función que reciba un mensaje y devuelva el mensaje cifrado con el cifrado de César
def cypher(mensaje):
    mensaje_cifrado = ''

    for letra in mensaje:
        if letra in letras:
            i = letras.index(letra)
            mensaje_cifrado+=letras[i+10]

    return mensaje_cifrado

print(cypher('hola'))

#? Creo una función que reciba un mensaje y devuelva el mensaje descifrado con el cifrado de César
def uncypher(mensaje):
    mensaje_descifrado = ''

    for letra in mensaje:
        if letra in letras:
            i = letras.index(letra)
            mensaje_descifrado+=letras[i-16]

    return mensaje_descifrado

print(uncypher('xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'))