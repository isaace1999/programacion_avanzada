from tkinter import Tk
from gui.widgets import crear_interfaz

if __name__ == "__main__":
    ventana = Tk()
    ventana.title("Biblioteca SaberX")
    crear_interfaz(ventana)
    ventana.mainloop()
