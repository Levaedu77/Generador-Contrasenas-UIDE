import json
import random
import time
import os
import pyperclip  # 🔄 Permite copiar contraseñas al portapapeles

ARCHIVO_CONTRASEÑAS = "contraseñas.json"

def guardar_contraseña(contraseña):
    """Guarda una nueva contraseña en el archivo JSON."""
    contraseñas = cargar_contraseñas()
    contraseñas.append(contraseña)
    with open(ARCHIVO_CONTRASEÑAS, "w") as file:
        json.dump(contraseñas, file, indent=4)
    print("💾 Contraseña guardada exitosamente.")

def cargar_contraseñas():
    """Carga las contraseñas almacenadas desde un archivo JSON."""
    if not os.path.exists(ARCHIVO_CONTRASEÑAS):
        return []
    with open(ARCHIVO_CONTRASEÑAS, "r") as file:
        return json.load(file)

# --- Seguridad OTP ---
otp_code = None
otp_expiration = None

def generar_otp():
    """Genera un código OTP de 6 dígitos con una validez de 3 minutos."""
    global otp_code, otp_expiration
    otp_code = random.randint(100000, 999999)
    otp_expiration = time.time() + 180  # Expira en 3 minutos
    return otp_code

def validar_otp(codigo_ingresado):
    """Verifica si el OTP ingresado es correcto y aún está vigente."""
    global otp_code, otp_expiration
    if time.time() > otp_expiration:
        return False, "❌ Código OTP expirado. Solicita uno nuevo."
    if int(codigo_ingresado) == otp_code:
        return True, "✅ Código correcto. Acceso permitido."
    return False, "❌ Código incorrecto."

def mostrar_contraseñas():
    """Muestra todas las contraseñas almacenadas y permite copiarlas al portapapeles."""
    contraseñas = cargar_contraseñas()
    if not contraseñas:
        print("⚠️ No hay contraseñas almacenadas.")
    else:
        print("\n📂 Contraseñas Guardadas:")
        for idx, contraseña in enumerate(contraseñas, 1):
            print(f"{idx}. {contraseña}")

        # Agregar opción para copiar una contraseña
        while True:
            opcion = input("\nIngrese el número de la contraseña que desea copiar (o 'x' para salir): ").strip()
            if opcion.lower() == 'x':
                break
            elif opcion.isdigit() and 1 <= int(opcion) <= len(contraseñas):
                pyperclip.copy(contraseñas[int(opcion) - 1])
                print("📋 Contraseña copiada al portapapeles.")
            else:
                print("❌ Opción inválida. Inténtelo de nuevo.")
