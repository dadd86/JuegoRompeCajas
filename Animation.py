import pygame
import random
from Player import Player
from Scene import Scene
from ColorManager import ColorManager # Asegúrate de importar ColorManager

def initialize_game():
    """
    Inicializa todos los componentes del juego: la ventana, el jugador y la escena.
    Establece las dimensiones de la pantalla, el jugador en el centro y las cajas con colores aleatorios.
    
    Retorna:
        - screen (Surface): Superficie de Pygame donde se dibujarán los elementos.
        - player (Player): Instancia del jugador.
        - scene (Scene): Instancia de la escena con las cajas generadas.
        - current_color (tuple): El primer color que se usará para las cajas.
        - WIDTH (int): Ancho de la pantalla.
        - HEIGHT (int): Alto de la pantalla.
    """
    # Dimensiones de la ventana
    WIDTH, HEIGHT = 400, 600

    # Inicializar Pygame y la pantalla
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Rompe las cajas')

    # Crear ColorManager
    base_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (0, 255, 255)]
    color_manager = ColorManager(base_colors, num_colors=100)  # Asegurarse de generar colores adecuados

    # Inicializar el jugador en el centro de la pantalla y la escena con las cajas
    player = Player(WIDTH // 2, HEIGHT // 2)
    scene = Scene(WIDTH, HEIGHT, color_manager)

    # Establecer el primer color de las cajas (aleatorio)
    current_color = scene.colors[0]  # Aseguramos que colors se haya generado correctamente

    return screen, player, scene, current_color, WIDTH, HEIGHT

def handle_events():
    """
    Maneja los eventos del juego, como el cierre de la ventana.
    
    Retorna:
        - True si el juego debe continuar.
        - False si el juego debe cerrarse.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def update_display(screen, player, scene):
    """
    Actualiza la pantalla del juego: dibuja las cajas y el jugador, y actualiza la ventana.
    
    Parámetros:
        screen (Surface): Superficie de Pygame donde se dibujan los elementos.
        player (Player): El jugador que se dibuja en la pantalla.
        scene (Scene): La escena con las cajas a dibujar.
    """
    # Limpiar la pantalla con un fondo blanco
    screen.fill((255, 255, 255))

    # Dibujar las cajas y el jugador en la pantalla
    scene.draw(screen)
    player.draw(screen)

    # Actualizar la ventana
    pygame.display.flip()
