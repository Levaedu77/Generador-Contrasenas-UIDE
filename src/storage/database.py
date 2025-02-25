import os

FILE_PATH = "src/storage/passwords.txt"

def guardar_contraseña(contraseña):
    """Guarda la contraseña generada en un archivo de texto."""
    with open(FILE_PATH, "a") as file:
        file.write(contraseña + "\n")

def mostrar_contraseñas_guardadas():
    """Muestra todas las contraseñas guardadas en el sistema."""
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            return file.readlines()
    return []
