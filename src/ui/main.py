import time
import pyperclip
from src.logic.generator import generar_contraseña
from src.logic.evaluator import evaluar_fortaleza
from src.storage.database import guardar_contraseña, mostrar_contraseñas, generar_otp, validar_otp

def menu():
    while True:
        print("\n🔐 Generador de Contraseñas Seguras 🔐")
        print("1️⃣ Generar una nueva contraseña")
        print("2️⃣ Ver y copiar contraseñas guardadas (Requiere OTP)")
        print("3️⃣ Salir del programa")
        
        opcion = input("👉 Opción: ")

        if opcion == "1":
            longitud = int(input("Ingrese la longitud de la contraseña (mínimo 8): "))
            incluir_mayus = input("¿Incluir mayúsculas? (s/n): ").strip().lower() == "s"
            incluir_numeros = input("¿Incluir números? (s/n): ").strip().lower() == "s"
            incluir_simbolos = input("¿Incluir símbolos? (s/n): ").strip().lower() == "s"

            try:
                contraseña = generar_contraseña(longitud, incluir_mayus, incluir_numeros, incluir_simbolos)
                print(f"\n✅ Contraseña generada: {contraseña}")
                print(f"🟢 Fortaleza de la contraseña: {evaluar_fortaleza(contraseña)}")

                # Copiar al portapapeles automáticamente
                pyperclip.copy(contraseña)
                print("📋 Contraseña copiada al portapapeles automáticamente.")

                if input("\n¿Desea guardar esta contraseña? (s/n): ").strip().lower() == "s":
                    guardar_contraseña(contraseña)
            except ValueError as e:
                print(f"⚠️ {e}")

        elif opcion == "2":
            otp = generar_otp()
            print(f"\n🔑 Tu código OTP es: {otp} (válido por 3 minutos)")

            codigo_ingresado = input("🔑 Ingresa el código OTP: ")
            valido, mensaje = validar_otp(codigo_ingresado)

            if valido:
                mostrar_contraseñas()
            else:
                print(mensaje)

        elif opcion == "3":
            print("👋 Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("❌ Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()
