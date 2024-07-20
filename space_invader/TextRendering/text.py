import pygame


class Text():
    '''
    Class for rendering text on the screen.
    Provides methods to display text with specified font, size, and color.
    '''

    def __init__(self, text, size, x, y, font="freesansbold.ttf", red=255, green=255, blue=255):
        self.text = text
        self.font = pygame.font.Font(font, size)
        self.size = size
        self.x = x
        self.y = y

        # Default text color (white)
        self.red = red
        self.green = green
        self.blue = blue

    def show_text(self, screen, value=None):
        if value is not None:
            text = self.font.render(f"{self.text}: {value}",
                                    True, (self.red, self.green, self.blue))
        else:
            text = self.font.render(
                self.text, True, (self.red, self.green, self.blue))
        screen.blit(text, (self.x, self.y))
