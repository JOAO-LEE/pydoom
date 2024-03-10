import pygame as pg

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sounds/'
        # pg.mixer.Sound.set_volume(5.5)
        self.shotgun = pg.mixer.Sound(self.path + 'shotgun.mp3')
