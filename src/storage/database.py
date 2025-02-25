import os

FILE_PATH = "contraseñas.txt"

def vaciar_archivo():
    """ Vacía el archivo de contraseñas al inicio del programa. """
    with open(FILE_PATH, "w") as file:
        file.write("")  # Sobrescribe el archivo con un contenido vacío

def guardar_contraseña(contraseña):
    """ Guarda una contraseña en el archivo """
    with open(FILE_PATH, "a") as file:
        file.write(contraseña + "\n")

def obtener_contraseñas():
    """ Obtiene la lista de contraseñas guardadas """
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as file:
        return [line.strip() for line in file.readlines()]
