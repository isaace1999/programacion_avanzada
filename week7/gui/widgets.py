import tkinter as tk
from gui.logic import registrar_libro, limpiar_campos

# Variables globales que se usan entre funciones
campos = {}


def crear_interfaz(ventana):
    global campos

    # Frame: Detalles del libro
    frame_detalles = tk.LabelFrame(ventana, text="Detalles del Libro", padx=10, pady=10)
    frame_detalles.pack(padx=10, pady=5, fill="x")

    tk.Label(frame_detalles, text="Título:").grid(row=0, column=0, sticky="e")
    campos["titulo"] = tk.Entry(frame_detalles)
    campos["titulo"].grid(row=0, column=1, sticky="we")

    tk.Label(frame_detalles, text="Autor:").grid(row=1, column=0, sticky="e")
    campos["autor"] = tk.Entry(frame_detalles)
    campos["autor"].grid(row=1, column=1, sticky="we")

    tk.Label(frame_detalles, text="Año:").grid(row=2, column=0, sticky="e")
    campos["anio"] = tk.Entry(frame_detalles)
    campos["anio"].grid(row=2, column=1, sticky="we")

    # Género y Categoría
    frame_genero_cat = tk.LabelFrame(
        ventana, text="Género y Categoría", padx=10, pady=10
    )
    frame_genero_cat.pack(padx=10, pady=5, fill="x")

    campos["genero"] = tk.StringVar()
    tk.Label(frame_genero_cat, text="Género:").grid(row=0, column=0, sticky="w")
    tk.Radiobutton(
        frame_genero_cat, text="Ficción", variable=campos["genero"], value="Ficción"
    ).grid(row=0, column=1)
    tk.Radiobutton(
        frame_genero_cat,
        text="No Ficción",
        variable=campos["genero"],
        value="No Ficción",
    ).grid(row=0, column=2)

    tk.Label(frame_genero_cat, text="Categoría:").grid(row=1, column=0, sticky="w")
    categorias = ["Novela", "Ciencia", "Historia", "Fantasía", "Educativo"]
    campos["categorias"] = {cat: tk.BooleanVar() for cat in categorias}
    for i, cat in enumerate(categorias):
        tk.Checkbutton(
            frame_genero_cat, text=cat, variable=campos["categorias"][cat]
        ).grid(row=1, column=i + 1)

    # Estado de disponibilidad
    frame_estado = tk.LabelFrame(
        ventana, text="Estado de Disponibilidad", padx=10, pady=10
    )
    frame_estado.pack(padx=10, pady=5, fill="x")
    campos["disponibilidad"] = tk.StringVar()
    tk.Radiobutton(
        frame_estado,
        text="Disponible",
        variable=campos["disponibilidad"],
        value="Disponible",
    ).pack(side="left")
    tk.Radiobutton(
        frame_estado,
        text="Prestado",
        variable=campos["disponibilidad"],
        value="Prestado",
    ).pack(side="left")

    # Número de copias
    frame_copias = tk.LabelFrame(ventana, text="Número de Copias", padx=10, pady=10)
    frame_copias.pack(padx=10, pady=5, fill="x")
    tk.Label(frame_copias, text="Copias disponibles:").pack(side="left")
    campos["copias"] = tk.Entry(frame_copias)
    campos["copias"].pack(side="left")

    # Resumen
    frame_resumen = tk.LabelFrame(ventana, text="Resumen del Libro", padx=10, pady=10)
    frame_resumen.pack(padx=10, pady=5, fill="both", expand=True)
    campos["resumen"] = tk.Text(frame_resumen, height=5)
    campos["resumen"].pack(fill="both", expand=True)

    # Idioma
    frame_idioma = tk.LabelFrame(ventana, text="Idioma del Libro", padx=10, pady=10)
    frame_idioma.pack(padx=10, pady=5, fill="x")
    campos["idioma"] = tk.StringVar(value="Seleccione idioma")
    opciones = ["Español", "Inglés", "Francés", "Alemán"]
    tk.OptionMenu(frame_idioma, campos["idioma"], *opciones).pack()

    # Botones
    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=10)

    tk.Button(
        frame_botones, text="Registrar Libro", command=lambda: registrar_libro(campos)
    ).pack(side="left", padx=10)
    tk.Button(
        frame_botones, text="Limpiar", command=lambda: limpiar_campos(campos)
    ).pack(side="left", padx=10)
