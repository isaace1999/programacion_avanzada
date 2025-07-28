import tkinter as tk
from tkinter import messagebox
import db_config

def agregar_videojuego():
    con = db_config.conectar()
    cursor = con.cursor()
    try:
        sql = "INSERT INTO Videojuegos (ID, Titulo, Genero, Clasificacion, Plataforma) VALUES (%s, %s, %s, %s, %s)"
        datos = (id_var.get(), titulo_var.get(), genero_var.get(), clasificacion_var.get(), plataforma_var.get())
        cursor.execute(sql, datos)
        con.commit()
        messagebox.showinfo("Éxito", "Videojuego agregado")
        mostrar_videojuegos()
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        con.close()

def mostrar_videojuegos():
    con = db_config.conectar()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Videojuegos")
    registros = cursor.fetchall()
    listbox.delete(0, tk.END)
    for reg in registros:
        listbox.insert(tk.END, f"{reg[0]} - {reg[1]} - {reg[2]} - {reg[3]} - {reg[4]}")
    con.close()

# GUI
root = tk.Tk()
root.title("Gestor de Videojuegos")

id_var = tk.StringVar()
titulo_var = tk.StringVar()
genero_var = tk.StringVar()
clasificacion_var = tk.StringVar()
plataforma_var = tk.StringVar()

tk.Label(root, text="ID").pack()
tk.Entry(root, textvariable=id_var).pack()
tk.Label(root, text="Título").pack()
tk.Entry(root, textvariable=titulo_var).pack()
tk.Label(root, text="Género").pack()
tk.Entry(root, textvariable=genero_var).pack()
tk.Label(root, text="Clasificación").pack()
tk.Entry(root, textvariable=clasificacion_var).pack()
tk.Label(root, text="Plataforma").pack()
tk.Entry(root, textvariable=plataforma_var).pack()

tk.Button(root, text="Agregar", command=agregar_videojuego).pack()
tk.Button(root, text="Mostrar", command=mostrar_videojuegos).pack()

listbox = tk.Listbox(root, width=100)
listbox.pack()

root.mainloop()
