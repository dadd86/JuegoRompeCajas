import pygame
import random

class Scene:
    """
    Representa una escena en el juego que contiene un conjunto de cajas con colores aleatorios.

    Atributos:
        width (int): Ancho de la ventana de la escena.
        height (int): Alto de la ventana de la escena.
        boxes (list): Lista de diccionarios que contienen las cajas y sus respectivos colores.
        color_manager (ColorManager): Administrador de colores para las cajas.

    Métodos:
        create_boxes(): Crea las cajas en la escena.
        draw(screen): Dibuja las cajas en la pantalla.
        break_box(player_pos): Rompe la caja que el jugador hace clic.
        check_change_color(current_color): Verifica si todas las cajas de un color han sido rotas.
    """
    
    def __init__(self, width, height, color_manager):
        """
        Inicializa la escena con un ancho y un alto determinados, y genera cajas aleatorias.

        Parámetros:
            width (int): Ancho de la ventana de la escena.
            height (int): Alto de la ventana de la escena.
            color_manager (ColorManager): Instancia de ColorManager para obtener los colores.
        """
        self.width = width
        self.height = height
        self.color_manager = color_manager
        self.boxes = []
        self.colors = self.color_manager.colors  # Aseguramos que 'colors' esté correctamente asignado
        self.create_boxes()

    def create_boxes(self):
        """
        Crea las cajas en la escena. Cada caja tiene una posición, un tamaño y un color aleatorio.
        Las cajas se distribuyen en una cuadrícula de 10x10.
        """
        try:
            self.boxes = []
            color_index = 0
            num_colors = len(self.colors)
            
            for row in range(10):
                for col in range(10):
                    # Usar el operador % para evitar desbordamiento de índices
                    color = self.colors[color_index % num_colors]
                    box = pygame.Rect(col * 45, row * 45, 40, 40)
                    self.boxes.append({'rect': box, 'color': color})
                    color_index += 1
        except Exception as e:
            print(f"Error creando las cajas: {e}")
            self.boxes = []  # En caso de error, limpiamos las cajas

    def draw(self, screen):
        """
        Dibuja todas las cajas en la pantalla.

        Parámetros:
            screen (Surface): Superficie de Pygame donde se dibujan las cajas.
        """
        try:
            for box in self.boxes:
                if box['color'] != (0, 0, 0):  # Solo dibujar cajas que no estén rotas
                    pygame.draw.rect(screen, box['color'], box['rect'])
        except Exception as e:
            print(f"Error al dibujar las cajas: {e}")

    def break_box(self, player_pos):
        """
        Rompe la caja en la posición donde el jugador hace clic.

        Parámetros:
            player_pos (tuple): Las coordenadas (x, y) donde el jugador hizo clic.
        """
        try:
            for box in self.boxes:
                if box['rect'].collidepoint(player_pos) and box['color'] != (0, 0, 0):
                    box['color'] = (0, 0, 0)  # Cambiar a negro para simular que está rota
        except Exception as e:
            print(f"Error al romper la caja: {e}")

    def check_change_color(self, current_color):
        """
        Verifica si todas las cajas de un color han sido rotas.

        Parámetros:
            current_color (tuple): El color actual que se está verificando.

        Retorna:
            bool: Devuelve True si todas las cajas del color actual están rotas, de lo contrario, False.
        """
        try:
            for box in self.boxes:
                if box['color'] == current_color:
                    return False
            return True
        except Exception as e:
            print(f"Error verificando el cambio de color: {e}")
            return False
