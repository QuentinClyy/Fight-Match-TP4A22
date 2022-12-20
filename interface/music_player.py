import pygame


class MusicPlayer:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.player = pygame.mixer.music
        self.player.load("./interface/Sounds/startMusic.wav")
        self.player.queue("./interface/Sounds/MusiqueLoop.wav", loops=-1)
        self.player.set_volume(0.5)
        self.player.play()


