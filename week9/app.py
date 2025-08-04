import tkinter as tk
from tkinter import messagebox
import db_config

def agregar_paciente():
    con = db_config.conectar()
    cursor = con.cursor()
    try:
        sql = "INSERT INTO Pacientes (Nombre, Edad, Genero, HistorialMedico, Contacto) VALUES (%s, %s, %s, %s, %s)"
        datos = (nombre_var.get(), int(edad_var.get()), genero_var.get(), historial_var.get(), contacto_var.get())
        cursor.execute(sql, datos)
        con.commit()
        messagebox.showinfo("Éxito", "Paciente agregado exitosamente")
        mostrar_pacientes()
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        con.close()

def mostrar_pacientes():
    con = db_config.conectar()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Pacientes")
    registros = cursor.fetchall()
    listbox.delete(0, tk.END)
    for reg in registros:
        listbox.insert(tk.END, f"{reg[0]} - {reg[1]} - {reg[2]} años - {reg[3]} - {reg[5]}")
    con.close()

# GUI
root = tk.Tk()
root.title("Clínica SaludTotal - Gestión de Pacientes")

nombre_var = tk.StringVar()
edad_var = tk.StringVar()
genero_var = tk.StringVar()
historial_var = tk.StringVar()
contacto_var = tk.StringVar()

tk.Label(root, text="Nombre").pack()
tk.Entry(root, textvariable=nombre_var).pack()
tk.Label(root, text="Edad").pack()
tk.Entry(root, textvariable=edad_var).pack()
tk.Label(root, text="Género").pack()
tk.Entry(root, textvariable=genero_var).pack()
tk.Label(root, text="Historial Médico").pack()
tk.Entry(root, textvariable=historial_var).pack()
tk.Label(root, text="Contacto").pack()
tk.Entry(root, textvariable=contacto_var).pack()

tk.Button(root, text="Agregar Paciente", command=agregar_paciente).pack()
tk.Button(root, text="Mostrar Pacientes", command=mostrar_pacientes).pack()

listbox = tk.Listbox(root, width=100)
listbox.pack()

root.mainloop()
