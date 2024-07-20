from . import character
from pygame import KEYDOWN, K_SPACE
from math import sqrt, pow
import settings.audio as audio


class Bullet(character.Character):
    '''
    Bullet class. Inherits from Character.
    Responsible for rendering the bullet, controlling its movement,
    and checking for collisions.
    '''

    def __init__(self, x, y, image_path, sound_file=None) -> None:
        self.bullet_state = 0  # Bullet state: 0 = not fired, 1 = fired
        self.y_change = 20
        self.y_start = y  # Starting y position
        self.collide_dist = 30  # Collision detection distance
        super().__init__(x, y, image_path, sound_file)

    def move(self, event):
        # Handle key press for firing the bullet
        if event.type == KEYDOWN and event.key == K_SPACE:
            if self.bullet_state == 0:
                self.bullet_state = 1
                self.y = self.y_start
                if self.sound_file:
                    audio.Sound(sound_file=self.sound_file)

    def draw(self, window):
        if self.bullet_state == 1:
            self.y -= self.y_change  # Move bullet upwards
            if self.y < 0:
                self.bullet_state = 0  # Reset bullet state if it goes off screen
            window.screen.blit(self.img, (self.x, self.y))  # Draw bullet

    def did_Collide(self, enemy_x, enemy_y):
        # Check for collision with enemy
        distance = sqrt(pow((self.x - enemy_x), 2) +
                        pow((self.y - enemy_y), 2))
        if distance < self.collide_dist:
            self.y = self.y_start
            self.bullet_state = 0
            return True
        return False

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if self.bullet_state == 0:
            self.__x = val
