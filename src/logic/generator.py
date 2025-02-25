import random
import string

def generar_contraseña(longitud=12, incluir_mayusculas=True, incluir_numeros=True, incluir_simbolos=True):
    """Genera una contraseña segura basada en los parámetros indicados."""
    
    caracteres = string.ascii_lowercase
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    return ''.join(random.choice(caracteres) for _ in range(longitud))
