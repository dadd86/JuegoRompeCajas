import pygame
import random


class Player:
    """
    Clase que representa al jugador como un círculo que se mueve en la pantalla.
    La clase maneja tanto la representación visual del jugador como su movimiento en el juego.
    
    Atributos:
        pos (list): Lista que contiene la posición [x, y] del jugador en la pantalla.
        radius (int): Radio del círculo que representa al jugador. Valor por defecto es 15.
        speed (int): Velocidad de movimiento del jugador. Valor por defecto es 5.

    Métodos:
        draw(screen): Dibuja al jugador en la pantalla.
        move(keys, width, height): Mueve al jugador según las teclas presionadas,
                                   asegurando que se mantenga dentro de los límites de la pantalla.
    """

    def __init__(self, x, y, radius=15, speed=5):
        """
        Inicializa un nuevo jugador en la posición [x, y] con un radio y velocidad determinados.

        Parámetros:
            x (int): Posición horizontal inicial del jugador.
            y (int): Posición vertical inicial del jugador.
            radius (int, opcional): Radio del círculo que representa al jugador. Valor por defecto es 15.
            speed (int, opcional): Velocidad de movimiento del jugador. Valor por defecto es 5.
        
        Levanta:
            ValueError: Si los valores de x, y, radio o velocidad son negativos.
        """
        if x < 0 or y < 0 or radius <= 0 or speed <= 0:
            raise ValueError("Los valores de x, y, radio y velocidad deben ser positivos.")

        self.pos = [x, y]
        self.radius = radius
        self.speed = speed

    def draw(self, screen):
        """
        Dibuja al jugador como un círculo negro en la pantalla.

        Parámetros:
            screen (Surface): Superficie de Pygame donde se dibuja el jugador.

        Levanta:
            TypeError: Si el parámetro screen no es una superficie válida.
        """
        if not isinstance(screen, pygame.Surface):
            raise TypeError("El parámetro 'screen' debe ser una superficie de Pygame.")
        
        pygame.draw.circle(screen, (0, 0, 0), self.pos, self.radius)

    def move(self, keys, width, height):
        """
        Mueve al jugador en la pantalla según las teclas presionadas.

        Asegura que el jugador no se salga de los límites de la pantalla.

        Parámetros:
            keys (dict): Diccionario con el estado actual de las teclas presionadas.
            width (int): Ancho de la pantalla, utilizado para los límites de movimiento.
            height (int): Altura de la pantalla, utilizado para los límites de movimiento.
        
        Levanta:
            ValueError: Si las dimensiones de la pantalla son negativas o cero.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Las dimensiones de la pantalla deben ser mayores que cero.")

        # Validación de movimiento para no salir de los límites
        if keys[pygame.K_LEFT] and self.pos[0] - self.radius > 0:
            self.pos[0] -= self.speed
        if keys[pygame.K_RIGHT] and self.pos[0] + self.radius < width:
            self.pos[0] += self.speed
        if keys[pygame.K_UP] and self.pos[1] - self.radius > 0:
            self.pos[1] -= self.speed
        if keys[pygame.K_DOWN] and self.pos[1] + self.radius < height:
            self.pos[1] += self.speed