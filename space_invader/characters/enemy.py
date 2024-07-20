from pygame import KEYDOWN, KEYUP, K_LEFT, K_RIGHT
from . import character


class Enemy(character.Character):
    '''
    Enemy character class. Inherits from Character.
    Responsible for rendering the enemy and controlling its movement.
    '''

    def __init__(self, x, y, image_path, speed=5) -> None:
        self.x_change = speed  # Horizontal speed
        self.y_change = 40  # Vertical drop after hitting a boundary
        super().__init__(x, y, image_path)

    def draw(self, window):
        self.x += self.x_change
        super().boundry(window)  # Ensure enemy stays within bounds
        if self.x >= (window.width - self.character_width) or self.x <= 0:
            self.x_change = -self.x_change
            self.y += self.y_change
        window.screen.blit(self.img, (self.x, self.y))
