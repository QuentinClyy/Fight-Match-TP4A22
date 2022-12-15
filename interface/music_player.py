import pygame


class MusicPlayer:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()

    def play_music(self):
        a = pygame.mixer.music
        a.load("./interface/Sounds/startMusic.wav")
        a.queue("./interface/Sounds/MusiqueLoop.wav", loops=-1)
        a.set_volume(0.5)
        a.play()
