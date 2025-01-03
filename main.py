import pygame
import random
from Player import Player
from Animation import initialize_game
from Animation import update_display
from Animation import handle_events
from Scene import Scene
from ColorManager import ColorManager

def main():
    """
    Función principal que maneja el ciclo del juego, inicializa Pygame y ejecuta el juego.
    """
    # Inicializar componentes del juego
    screen, player, scene, current_color, WIDTH, HEIGHT = initialize_game()

    # Juego principal
    running = True
    while running:
        # Actualizar la pantalla
        update_display(screen, player, scene)

        # Comprobar si se debe cambiar el color
        if scene.check_change_color(current_color):
            # Cambiar al siguiente color
            next_color_index = (scene.colors.index(current_color) + 1) % len(scene.colors)
            current_color = scene.colors[next_color_index]
            # Reempezar el juego
            scene.create_boxes()

        # Detectar eventos
        running = handle_events()

        # Controlar el movimiento del jugador
        keys = pygame.key.get_pressed()
        player.move(keys, WIDTH, HEIGHT)

        # Romper cajas con el jugador
        scene.break_box(player.pos)

        pygame.time.delay(50)

    pygame.quit()


if __name__ == "__main__":
    main()
