def evaluar_fortaleza(contraseña):
    """ Evalúa la fortaleza de una contraseña basada en su longitud y variedad de caracteres """
    longitud = len(contraseña)
    tiene_mayus = any(c.isupper() for c in contraseña)
    tiene_numeros = any(c.isdigit() for c in contraseña)
    tiene_simbolos = any(c in "!@#$%^&*()_+{}[]:;<>,.?/" for c in contraseña)

    puntaje = 0
    if longitud >= 12:
        puntaje += 2
    elif longitud >= 8:
        puntaje += 1
    if tiene_mayus:
        puntaje += 1
    if tiene_numeros:
        puntaje += 1
    if tiene_simbolos:
        puntaje += 1

    if puntaje >= 4:
        return "Fuerte 💪"
    elif puntaje == 3:
        return "Moderada ⚠️"
    else:
        return "Débil ❌"
