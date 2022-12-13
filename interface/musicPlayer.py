import pygame
import tkinter as tk

class MusicPlayer:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()

    def play_music(self):
        a = pygame.mixer.music
        a.load("./Sounds/startMusic.wav")
        a.queue("./Sounds/MusiqueLoop.wav", loops=-1)
        a.set_volume(0.5)
        a.play()


if __name__ == "__main__":
    root = tk.Tk()
    music = MusicPlayer()
    music.play_music()
    root.mainloop()
