import random
import string

def generar_contraseña(longitud=12, incluir_mayus=True, incluir_numeros=True, incluir_simbolos=True):
    """Genera una contraseña segura con los parámetros especificados."""
    
    if longitud < 8:
        raise ValueError("La contraseña debe tener al menos 8 caracteres.")

    caracteres = string.ascii_lowercase
    if incluir_mayus:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña
