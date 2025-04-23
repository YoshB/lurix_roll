
from monster_controller import Monster

class Zona():
    """
    Clase que representa una zona en el juego.
    
    Atributos:
        nombre (str): Nombre de la zona.
        monstruo (str): Tipo de monstruo en la zona.
        dificultad (int): Dificultad de la zona.
        recompensa (int): Recompensa por explorar la zona.
    """
    def __init__(self, nombre:str):
        self.nombre = nombre
        self.monstruo_prob = {} # Probabilidad de aparición del monstruo

    def agregar_monstruo(self, monstruo:Monster, probabilidad:int):
        """
        Agrega un monstruo a la zona con su probabilidad de aparición.
        
        Args:
            monstruo (Monstruo): El monstruo a agregar.
            probabilidad (int): La probabilidad de aparición del monstruo.
        """
        self.monstruo_prob[monstruo.nombre] = probabilidad

    def explorar(self, zona:str) -> Monster:
        """
        Simula la exploración de una zona y devuelve un monstruo indicando el resultado.
        
        Args:
            zona (str): La zona que se está explorando.
            
        Returns:
            str: Mensaje indicando el resultado de la exploración.
        """
        m = ''
        while m == '':

            self.monstruo_pro.key 

        zonas_validas = ["bosque", "pradera", "montaña", "nevado", "mar", "rio", "desierto"]
        if zona not in zonas_validas:
            return "Zona no válida. Debes explorar en el bosque, cueva o montaña."


        return f"Explorando la zona: {zona}..."

    def __repr__(self):
        return f"Zona(nombre={self.nombre}, monstruo={self.monstruo}, dificultad={self.dificultad}, recompensa={self.recompensa})"