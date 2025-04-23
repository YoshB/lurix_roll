import tkinter as tk
from controllers.tienda_controller import abrir_tienda
from controllers.monster_controller import abrir_exploracion
from controllers.monster_controller import explorar_bestiario


def comprar():
    abrir_tienda()

def explorar():
    abrir_exploracion()

def bestiario():
    explorar_bestiario()

# Crear la ventana principal
root = tk.Tk()
root.title("Lurix roll")
root.geometry("300x250")  # Tamaño de la ventana

# Título
titulo = tk.Label(root, text="Lurix roll", font=("Helvetica", 16))
titulo.pack(pady=20)

# Botones principales
boton_frame = tk.Frame(root)
boton_frame.pack(pady=10)

btn_comprar = tk.Button(boton_frame, text="Comprar", command=comprar, width=15)
btn_comprar.grid(row=0, column=0, padx=10)

# Botón "explorar"
btn_explorar = tk.Button(root, text="Explorar", command=explorar, width=15)
btn_explorar.pack(pady=5)

# Botón "bestiario"
btn_explorar = tk.Button(root, text="Bestiario", command=bestiario, width=15)
btn_explorar.pack(pady=5)


# Ejecutar app
root.mainloop()
