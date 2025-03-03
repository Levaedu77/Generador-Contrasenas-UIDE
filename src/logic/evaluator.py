import string

def evaluar_fortaleza(contraseña):
    """Evalúa la fortaleza de una contraseña en base a su composición."""
    
    longitud = len(contraseña)
    tiene_mayus = any(c.isupper() for c in contraseña)
    tiene_numeros = any(c.isdigit() for c in contraseña)
    tiene_simbolos = any(c in string.punctuation for c in contraseña)

    puntuacion = longitud + (tiene_mayus * 2) + (tiene_numeros * 2) + (tiene_simbolos * 3)

    if puntuacion >= 14:
        return "Fuerte 💪"
    elif 10 <= puntuacion < 14:
        return "Moderada ⚠️"
    else:
        return "Débil ❌"
