import tkinter as tk
import random
from PIL import Image, ImageTk

import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

objects_filename =f"DB/{os.getenv('OBJECTS_FILENAME', 'objetos.csv')}"
objects_df = pd.read_csv(objects_filename)
#objects_df = objects_df.fillna("None")
objects_df['Nombre'] = [str(obj).strip() for obj in objects_df["Nombre"]]

def abrir_tienda():
    # Crear una nueva ventana
    tienda = tk.Toplevel()
    tienda.title("Tienda")
    tienda.geometry("700x530")

    # Etiqueta de título en la ventana de la tienda
    titulo = tk.Label(tienda, text="Bienvenido a la Tienda", font=("Helvetica", 16))
    titulo.pack(pady=10)

    # Frame para los artículos
    frame_articulos = tk.Frame(tienda)
    frame_articulos.pack(pady=10)

    def mostrar_articulos():
        # Limpiar artículos anteriores
        for widget in frame_articulos.winfo_children():
            widget.destroy()

        # Elegir 6 artículos al azar
        seleccionados = random_items(sample=6)
        print(seleccionados)

        for idx, nombre in enumerate(seleccionados):
            fila = idx // 3
            columna = idx % 3

            # Marco individual para cada artículo
            item_frame = tk.Frame(frame_articulos, bd=1, relief="solid", padx=5, pady=5)
            item_frame.grid(row=fila, column=columna, padx=5, pady=7)

            # Ruta a la imagen
            imagen_path = f"img/objetos/{nombre}.png"

            try:
                if os.path.exists(imagen_path):
                    imagen = Image.open(imagen_path)
                    imagen = imagen.resize((150, 150))
                    imagen_tk = ImageTk.PhotoImage(imagen)
                else:
                    raise FileNotFoundError
            except:
                imagen = Image.new("RGB", (150, 150), "gray")
                imagen_tk = ImageTk.PhotoImage(imagen)

            # Mostrar imagen con evento clic
            img_label = tk.Label(item_frame, image=imagen_tk, cursor="hand2")
            img_label.image = imagen_tk  # Guardar referencia
            img_label.pack()

            # Asociar evento clic
            img_label.bind("<Button-1>", lambda e, nombre=nombre: mostrar_detalle(nombre))

            # Nombre del artículo
            label = tk.Label(item_frame, text=nombre)
            label.pack()
            
    # Botón para volver a visitar
    btn_volver = tk.Button(tienda, text="Volver a visitar", command=mostrar_articulos)
    btn_volver.pack(pady=10)

    # Mostrar los primeros artículos al abrir
    mostrar_articulos()


def mostrar_detalle(nombre):
    detalle = tk.Toplevel()
    detalle.title(nombre)
    detalle.geometry("350x550")

    # Intentar cargar imagen
    imagen_path = f"imagenes/{nombre}.jpg"
    try:
        if os.path.exists(imagen_path):
            img = Image.open(imagen_path).resize((200, 200))
        else:
            raise FileNotFoundError
    except:
        img = Image.new("RGB", (200, 200), "black")

    imagen_tk = ImageTk.PhotoImage(img)
    img_label = tk.Label(detalle, image=imagen_tk)
    img_label.image = imagen_tk  # Guardar referencia
    img_label.pack(pady=10)

    info_item = get_item(nombre)
    # Mostrar información del objeto
    for stat, valor in info_item.items():
        stat_label = tk.Label(detalle, 
                                text=f"{stat.capitalize()}: {valor}", 
                                wraplength=200, 
                                justify="left")

        stat_label.pack()


def random_items(sample:int=6) -> list:
    """
        Devuelve una lista de artículos aleatorios de la tienda.
        
        Args:
            sample (int): Número de artículos a seleccionar.
            
        Returns:
            list: Lista de artículos seleccionados.
    """
    return random.sample(objects_df["Nombre"].tolist(), sample)

def get_item(nombre:str) -> dict:

    """
        Devuelve un objeto de la tienda.
        
        Returns:
            dict: Objeto seleccionado.
    """
    obj_info = objects_df.loc[objects_df['Nombre'] == nombre].iloc[0].dropna().to_dict()
    return obj_info
