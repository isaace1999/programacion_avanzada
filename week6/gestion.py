import json
import os


def leer_archivo(nombre_archivo):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r") as archivo:
            return json.load(archivo)
    else:
        return []


def escribir_archivo(nombre_archivo, datos):
    with open(nombre_archivo, "w") as archivo:
        json.dump(datos, archivo, indent=4)


def agregar_libro(libros, archivo_libros):
    titulo = input("Título del libro: ")
    genero = input("Género: ")
    año = input("Año de publicación: ")
    autor = input("Nombre del autor: ")
    libros.append({"titulo": titulo, "genero": genero, "año": año, "autor": autor})
    escribir_archivo(archivo_libros, libros)
    print("Libro agregado con éxito.\n")


def agregar_autor(autores, archivo_autores):
    nombre = input("Nombre del autor: ")
    nacionalidad = input("Nacionalidad: ")
    autores.append({"nombre": nombre, "nacionalidad": nacionalidad})
    escribir_archivo(archivo_autores, autores)
    print("Autor agregado con éxito.\n")


def mostrar_informacion(libros, autores):
    print("\n--- LIBROS ---")
    print(json.dumps(libros, indent=4, ensure_ascii=False))
    print("\n--- AUTORES ---")
    print(json.dumps(autores, indent=4, ensure_ascii=False))
