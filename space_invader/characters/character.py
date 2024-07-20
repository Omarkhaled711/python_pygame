from pygame import image


class Character():
    '''
    Base class for all characters in the game.
    Provides common attributes and methods for characters.
    '''

    def __init__(self, x, y, image_path, sound_file=None) -> None:
        self.img = image.load(image_path)
        self.x = x
        self.y = y
        self.character_width = 64
        self.sound_file = sound_file

    def boundry(self, window):
        ''' Ensure the character stays within window bounds '''
        if self.x >= (window.width - self.character_width):
            self.x = window.width - self.character_width
        elif self.x <= 0:
            self.x = 0

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        self.__y = val
