import random

class ColorManager:
    """
    Administrador de colores para las cajas del juego.
    
    Atributos:
        base_colors (list): Lista de colores base para las cajas.
        colors (list): Lista de colores aleatorios para las cajas.
        
    Métodos:
        generate_random_colors(): Genera una lista aleatoria de colores para las cajas.
    """
    
    def __init__(self, base_colors, num_colors=100):
        """
        Inicializa el administrador de colores.
        
        Parámetros:
            base_colors (list): Colores base para generar colores aleatorios.
            num_colors (int): Número de colores aleatorios a generar.
        """
        self.base_colors = base_colors
        
        # Ajustar num_colors si es mayor que la cantidad de colores base
        if num_colors > len(self.base_colors):
            print(f"Ajustando el número de colores a {len(self.base_colors)} ya que es mayor que la cantidad de colores base.")
            num_colors = len(self.base_colors)
        
        self.colors = self.generate_random_colors(num_colors)

    def generate_random_colors(self, num_colors):
        """
        Genera una lista de colores aleatorios para las cajas.
        
        Parámetros:
            num_colors (int): Número total de colores a generar.
        
        Retorna:
            list: Lista de colores aleatorios.
        """
        try:
            # Si el número de colores a generar es mayor que la población base de colores
            return random.sample(self.base_colors * (num_colors // len(self.base_colors)), num_colors)
        except Exception as e:
            print(f"Error generando colores aleatorios: {e}")
            return self.base_colors  # Devuelve colores base en caso de error
