import re

def evaluar_fortaleza(contraseña):
    """Evalúa la fortaleza de una contraseña y devuelve su nivel de seguridad."""
    puntuacion = 0
    if len(contraseña) >= 12:
        puntuacion += 1
    if any(c.isdigit() for c in contraseña):
        puntuacion += 1
    if any(c.islower() for c in contraseña) and any(c.isupper() for c in contraseña):
        puntuacion += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", contraseña):
        puntuacion += 1

    niveles = ["Débil", "Moderada", "Fuerte", "Muy Fuerte"]
    return niveles[puntuacion] if puntuacion > 0 else "Muy Débil"
