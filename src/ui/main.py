from src.logic.generator import generar_contraseña
from src.logic.evaluator import evaluar_fortaleza
from src.storage.database import guardar_contraseña, mostrar_contraseñas_guardadas

def main():
    print("🔐 Generador Seguro de Contraseñas 🔐")
    longitud = int(input("Ingrese la longitud de la contraseña (mínimo 8 caracteres): "))
    incluir_mayus = input("¿Incluir mayúsculas? (s/n): ").strip().lower() == 's'
    incluir_numeros = input("¿Incluir números? (s/n): ").strip().lower() == 's'
    incluir_simbolos = input("¿Incluir símbolos? (s/n): ").strip().lower() == 's'

    if longitud < 8:
        print("⚠️ La longitud mínima permitida es de 8 caracteres.")
        return

    # Generar la contraseña
    contraseña = generar_contraseña(longitud, incluir_mayus, incluir_numeros, incluir_simbolos)
    print(f"\n🔑 Contraseña generada: {contraseña}")

    # Evaluar fortaleza
    fortaleza = evaluar_fortaleza(contraseña)
    print(f"✅ Fortaleza de la contraseña: {fortaleza}")

    # Guardar contraseña
    if input("¿Desea guardar la contraseña? (s/n): ").strip().lower() == 's':
        guardar_contraseña(contraseña)
        print("✅ Contraseña guardada exitosamente.")

    # Mostrar contraseñas almacenadas
    if input("¿Desea ver las contraseñas guardadas? (s/n): ").strip().lower() == 's':
        contraseñas_guardadas = mostrar_contraseñas_guardadas()
        if contraseñas_guardadas:
            print("\n📜 Contraseñas almacenadas:")
            for index, pwd in enumerate(contraseñas_guardadas, 1):
                print(f"{index}. {pwd.strip()}")
        else:
            print("⚠️ No hay contraseñas almacenadas.")

if __name__ == "__main__":
    main()
