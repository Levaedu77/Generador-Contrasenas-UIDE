import random
import string

def generar_contraseña(longitud, incluir_mayus, incluir_numeros, incluir_simbolos):
    """ Genera una contraseña aleatoria con los criterios seleccionados """
    caracteres = string.ascii_lowercase
    if incluir_mayus:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    return ''.join(random.choice(caracteres) for _ in range(longitud))
