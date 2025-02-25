import string

def evaluar_fortaleza(contraseña):
    """Evalúa la seguridad de una contraseña en base a su complejidad."""
    
    puntuacion = 0
    if any(c.islower() for c in contraseña):
        puntuacion += 1
    if any(c.isupper() for c in contraseña):
        puntuacion += 1
    if any(c.isdigit() for c in contraseña):
        puntuacion += 1
    if any(c in string.punctuation for c in contraseña):
        puntuacion += 1

    if len(contraseña) >= 12 and puntuacion >= 3:
        return "Fuerte 🔒"
    elif len(contraseña) >= 8 and puntuacion >= 2:
        return "Moderada ⚠️"
    else:
        return "Débil ❌"
