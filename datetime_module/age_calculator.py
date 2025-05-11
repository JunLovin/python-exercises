# Calculadora de edad

from datetime import datetime

# ? Creo una función que tome como argumento una fecha de nacimiento en el formato: YYYY-MM-DD
def agee_calculator(fecha_nacimiento):
    # ? Guardo en una variable la resta de la fecha actual y la fecha del usuario
    result_date = datetime.now() - datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
    # ? Retorno la edad del usuario en años
    return f'Tu edad es de: {result_date.days // 365} años'

print(age_calculator('2007-02-17'))
