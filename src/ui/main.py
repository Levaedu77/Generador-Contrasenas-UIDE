import src.logic.generator as generator
import src.logic.evaluator as evaluator
import src.storage.database as database

def mostrar_menu():
    """ Muestra las opciones del menú """
    print("\n🔑 Generador de Contraseñas Seguras 🔒")
    print("1️⃣ Generar una nueva contraseña")
    print("2️⃣ Ver y copiar contraseñas guardadas")
    print("3️⃣ Salir del programa")

def main():
    """ Función principal del programa """
    database.vaciar_archivo()  # Vaciar el archivo de contraseñas al iniciar el programa

    while True:
        mostrar_menu()
        opcion = input("\n👉 Opción: ").strip()

        if opcion == "1":
            try:
                longitud = int(input("Ingrese la longitud de la contraseña (mínimo 8): "))
                if longitud < 8:
                    print("⚠️ La contraseña debe tener al menos 8 caracteres.")
                    continue

                incluir_mayus = input("¿Incluir mayúsculas? (s/n): ").strip().lower() == "s"
                incluir_numeros = input("¿Incluir números? (s/n): ").strip().lower() == "s"
                incluir_simbolos = input("¿Incluir símbolos? (s/n): ").strip().lower() == "s"

                contraseña = generator.generar_contraseña(longitud, incluir_mayus, incluir_numeros, incluir_simbolos)
                fortaleza = evaluator.evaluar_fortaleza(contraseña)

                print(f"\n✅ Contraseña generada: {contraseña}")
                print(f"🔵 Fortaleza de la contraseña: {fortaleza}")

                if input("¿Desea guardar la contraseña? (s/n): ").strip().lower() == "s":
                    database.guardar_contraseña(contraseña)
                    print("💾 Contraseña guardada exitosamente.")
            
            except ValueError:
                print("❌ Error: Debe ingresar un número válido para la longitud.")

        elif opcion == "2":
            contraseñas_guardadas = database.obtener_contraseñas()
            if not contraseñas_guardadas:
                print("⚠️ No hay contraseñas almacenadas.")
                continue

            print("\n📜 Lista de Contraseñas Guardadas:")
            for i, pwd in enumerate(contraseñas_guardadas, 1):
                print(f"{i}. {pwd}")

            try:
                seleccion = int(input("\nIngrese el número de la contraseña que desea copiar: ")) - 1
                if 0 <= seleccion < len(contraseñas_guardadas):
                    import pyperclip
                    pyperclip.copy(contraseñas_guardadas[seleccion])
                    print("📋 Contraseña copiada al portapapeles.")
                else:
                    print("❌ Número inválido.")

            except ValueError:
                print("❌ Entrada no válida.")

        elif opcion == "3":
            print("👋 Saliendo del programa...")
            break

        else:
            print("❌ Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
