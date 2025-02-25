import random
import string

def generar_contraseña(longitud=12, mayus=True, nums=True, simbolos=True):
    """Genera una contraseña segura con los parámetros definidos."""
    caracteres = string.ascii_lowercase
    if mayus:
        caracteres += string.ascii_uppercase
    if nums:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña
