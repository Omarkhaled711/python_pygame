from pygame import display, image


class Window():
    '''
    Class for managing the game window and its properties.
    Responsible for setting up the window, drawing the background,
    and handling display settings.
    '''

    def __init__(self, height, width, title, logo_path, background_path=None) -> None:
        self.height = height
        self.width = width
        self.title = title
        self.logo = image.load(logo_path)
        self.background = None
        if background_path is not None:
            self.background = image.load(background_path)
        display.set_caption(self.title)
        display.set_icon(self.logo)
        self.screen = display.set_mode((self.width, self.height))

    def draw_background(self):
        if self.background is not None:
            self.screen.blit(self.background, (0, 0))
