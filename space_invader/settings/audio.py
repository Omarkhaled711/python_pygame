from pygame import mixer

'''
This module is for audio related settings.
if you have a long audio file, use the Music class,
otherwise if you want to add a short sound effect that's
associated with an event on the screen, use the Sound class
'''


class Audio():
    '''
    Base class for handling audio in the game.
    Provides common attributes and methods for managing sound and music.
    '''

    def __init__(self, loop_state=0):
        self.loop_state = loop_state


class Music(Audio):
    '''
    Class for handling background music.
    Inherits from Audio and provides methods to play music.
    '''

    def __init__(self, sound_file, loop_state=0):
        super().__init__(loop_state)
        self.sound = mixer.music.load(sound_file)
        if loop_state == 1:
            mixer.music.play(-1)
        else:
            mixer.music.play()


class Sound(Audio):
    '''
    Class for handling sound effects.
    Inherits from Audio and provides methods to play
    sound effects.
    '''

    def __init__(self, sound_file, loop_state=0):
        super().__init__(loop_state)
        self.sound = mixer.Sound(sound_file)
        if loop_state == 1:
            self.sound.play(-1)
        else:
            self.sound.play()
