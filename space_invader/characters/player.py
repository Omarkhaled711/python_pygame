from pygame import KEYDOWN, KEYUP, K_LEFT, K_RIGHT
from . import character
from math import sqrt, pow


class Player(character.Character):
    '''
    Player character class. Inherits from Character.
    Responsible for rendering the player, controlling its movement,
    and checking for collisions.
    '''

    def __init__(self, x, y, image_path, speed=5) -> None:
        self.x_change = 0
        self.speed = speed
        self.collide_dist = 70  # Collision detection distance
        super().__init__(x, y, image_path)

    def draw(self, window):
        self.x += self.x_change
        super().boundry(window)  # Ensure player stays within bounds
        window.screen.blit(self.img, (self.x, self.y))

    def move(self, event):
        ''' Handle key presses for movement '''
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                self.x_change = -self.speed
            elif event.key == K_RIGHT:
                self.x_change = self.speed

        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                self.x_change = 0

    def did_Collide(self, enemy_x, enemy_y):
        ''' Check for collision with enemy '''
        distance = sqrt(pow((self.x - enemy_x), 2) +
                        pow((self.y - enemy_y), 2))
        return distance < self.collide_dist
