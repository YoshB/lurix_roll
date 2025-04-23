import random
import tkinter as tk
from PIL import Image, ImageTk
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

monsters_filename =f"DB/{os.getenv('MONSTERS_FILENAME', 'monsters.csv')}"
monsters_df = pd.read_csv(monsters_filename)
#monsters_df = monsters_df.fillna("None")
monsters_df['Nombre'] = [str(m).strip() for m in monsters_df["Nombre"]]

# Zonas disponibles
zonas = ['Bosque',
         'Pradera',	
         'Desierto',
         'Pantano',	'Montaña',
         'Nevado', 
         'Rios y lagos', 
         'Mares']

        
def abrir_exploracion():
    # Crear ventana de exploración
    exploracion = tk.Toplevel()
    exploracion.title("Exploración")
    exploracion.geometry("500x700")

    # Título
    titulo = tk.Label(exploracion, text="Elige una zona para explorar", font=("Helvetica", 14))
    titulo.pack(pady=10)

    # Menú desplegable
    zona_seleccionada = tk.StringVar(value=zonas[0])

    menu_zonas = tk.OptionMenu(exploracion, zona_seleccionada, *zonas)
    menu_zonas.config(width=30)
    menu_zonas.pack(pady=3)

    # Frame para mostrar el monstruo
    frame_monstruo = tk.Frame(exploracion)
    frame_monstruo.pack(pady=10)

    def explorar_zona():
        # Limpiar contenido anterior
        for widget in frame_monstruo.winfo_children():
            widget.destroy()

        # Elegir monstruo al azar
        nombre_monstruo, stats = random_monster(zona=zona_seleccionada.get())
        # Ruta a la imagen
        imagen_path = f"img/monstruos/{nombre_monstruo}.png"

        # Cuadro para imagen del monstruo
        try:
            if os.path.exists(imagen_path):
                imagen = Image.open(imagen_path)
                imagen = imagen.resize((200, 200))
                imagen_tk = ImageTk.PhotoImage(imagen)
            else:
                raise FileNotFoundError(f"Imagen no encontrada: {imagen_path}")
        except Exception as e:
            # Si no se encuentra la imagen o hay error, se crea una imagen negra
            print(repr(e))
            imagen = Image.new("RGB", (200, 200), "black")
            imagen_tk = ImageTk.PhotoImage(imagen)

        # Mostrar imagen
        label_imagen = tk.Label(frame_monstruo, image=imagen_tk)
        label_imagen.image = imagen_tk  # Se guarda una referencia para evitar que se borre
        label_imagen.pack()

        # Nombre
        nombre_label = tk.Label(frame_monstruo, text=nombre_monstruo, font=("Helvetica", 14, "bold"))
        nombre_label.pack(pady=2)

        # Stats
        for stat, valor in stats.items():
            stat_label = tk.Label(frame_monstruo, 
                                  text=f"{stat.capitalize()}: {valor}", 
                                  wraplength=200, 
                                  justify="left")

            stat_label.pack()

    # Botón explorar
    btn_explorar = tk.Button(exploracion, text="Explorar", command=explorar_zona)
    btn_explorar.pack(pady=10)


def explorar_bestiario():
        # Crear ventana de exploración
    exploracion = tk.Toplevel()
    exploracion.title("Bestiario")
    exploracion.geometry("500x700")

    # Título
    titulo = tk.Label(exploracion, text="Elige un Monstruo", font=("Helvetica", 14))
    titulo.pack(pady=10)

    # Menú desplegable
    monstruo_seleccionado = tk.StringVar(value=monsters_df['Nombre'].tolist()[0])

    menu_monstruos = tk.OptionMenu(exploracion, monstruo_seleccionado, *monsters_df['Nombre'].tolist())
    menu_monstruos.config(width=30)
    menu_monstruos.pack(pady=3)

    # Frame para mostrar el monstruo
    frame_monstruo = tk.Frame(exploracion)
    frame_monstruo.pack(pady=10)

    def explorar_zona():
        # Limpiar contenido anterior
        for widget in frame_monstruo.winfo_children():
            widget.destroy()

        nombre_monstruo = monstruo_seleccionado.get()
        # Elegir monstruo al azar
        monster_stats = get_monster(nombre_monstruo)
        # Ruta a la imagen
        imagen_path = f"img/{nombre_monstruo}.png"

        # Cuadro para imagen del monstruo
        try:
            if os.path.exists(imagen_path):
                imagen = Image.open(imagen_path)
                imagen = imagen.resize((200, 200))
                imagen_tk = ImageTk.PhotoImage(imagen)
            else:
                raise FileNotFoundError(f"Imagen no encontrada: {imagen_path}")
        except Exception as e:
            # Si no se encuentra la imagen o hay error, se crea una imagen negra
            print(repr(e))
            imagen = Image.new("RGB", (200, 200), "black")
            imagen_tk = ImageTk.PhotoImage(imagen)

        # Mostrar imagen
        label_imagen = tk.Label(frame_monstruo, image=imagen_tk)
        label_imagen.image = imagen_tk  # Se guarda una referencia para evitar que se borre
        label_imagen.pack()

        # Nombre
        nombre_label = tk.Label(frame_monstruo, text=nombre_monstruo, font=("Helvetica", 14, "bold"))
        nombre_label.pack(pady=2)

        # Stats
        for stat, valor in monster_stats.items():
            stat_label = tk.Label(frame_monstruo, 
                                  text=f"{stat.capitalize()}: {valor}", 
                                  wraplength=200, 
                                  justify="left")

            stat_label.pack()
    # Botón explorar
    btn_explorar = tk.Button(exploracion, text="Explorar", command=explorar_zona)
    btn_explorar.pack(pady=10)



def random_monster(zona:str="pradera", sample:int=1) -> list:
    """
        Devuelve una lista de artículos aleatorios de la tienda.
        
        Args:
            sample (int): Número de artículos a seleccionar.
            
        Returns:
            list: Lista de artículos seleccionados.
    """
    monster_list = monsters_df.get('Nombre').tolist()
    monsters_prob = monsters_df.get(zona).tolist()
    monster_name = random.choices(list(monster_list), weights=monsters_prob, k=sample)[0]
    print(monster_name)
    stats = monsters_df.loc[monsters_df['Nombre'] == monster_name].iloc[0, 1:12].to_dict()
    return (monster_name, stats)

def get_monster(nombre:str) -> dict:
    """
        Devuelve un monstruo específico por su nombre.
        
        Args:
            nombre (str): Nombre del monstruo.
            
        Returns:  
            dict: Datos del monstruo.
    """
    monster = monsters_df.loc[monsters_df['Nombre'] == nombre].iloc[0, 1:12].to_dict()
    return monster

