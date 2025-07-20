def registrar_libro(campos):
    titulo = campos["titulo"].get()
    autor = campos["autor"].get()
    anio = campos["anio"].get()
    genero = campos["genero"].get()
    categorias = [cat for cat, var in campos["categorias"].items() if var.get()]
    disponibilidad = campos["disponibilidad"].get()
    copias = campos["copias"].get()
    resumen = campos["resumen"].get("1.0", "end").strip()
    idioma = campos["idioma"].get()

    print("=== Detalles del Libro ===")
    print(f"Título: {titulo}")
    print(f"Autor: {autor}")
    print(f"Año: {anio}")
    print(f"Género: {genero}")
    print(f"Categorías: {', '.join(categorias)}")
    print(f"Disponibilidad: {disponibilidad}")
    print(f"Número de copias: {copias}")
    print(f"Resumen: {resumen}")
    print(f"Idioma: {idioma}")
    print("==========================")


def limpiar_campos(campos):
    campos["titulo"].delete(0, "end")
    campos["autor"].delete(0, "end")
    campos["anio"].delete(0, "end")
    campos["genero"].set(None)
    for var in campos["categorias"].values():
        var.set(False)
    campos["disponibilidad"].set(None)
    campos["copias"].delete(0, "end")
    campos["resumen"].delete("1.0", "end")
    campos["idioma"].set("Seleccione idioma")
