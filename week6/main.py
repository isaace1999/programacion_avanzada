from gestion import (
    leer_archivo,
    escribir_archivo,
    agregar_libro,
    agregar_autor,
    mostrar_informacion,
)


def main():
    archivo_libros = "libros.json"
    archivo_autores = "autores.json"

    libros = leer_archivo(archivo_libros)
    autores = leer_archivo(archivo_autores)

    while True:
        print("\nMENÚ PRINCIPAL")
        print("1. Agregar Libro")
        print("2. Agregar Autor")
        print("3. Mostrar Información")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_libro(libros, archivo_libros)
        elif opcion == "2":
            agregar_autor(autores, archivo_autores)
        elif opcion == "3":
            mostrar_informacion(libros, autores)
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
