contraseñas_guardadas = []

def guardar_contraseña(contraseña):
    """Guarda la contraseña en una lista."""
    contraseñas_guardadas.append(contraseña)

def mostrar_contraseñas_guardadas():
    """Devuelve la lista de contraseñas almacenadas."""
    return contraseñas_guardadas
