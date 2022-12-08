from direct.showbase.ShowBase import ShowBase


class MusicPlayer(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.music_mgr = self.musicManager
        self.music_mgr.setConcurrentSoundLimit(2)
        self.play_music()

    def play_music(self):
        start_music = self.loader.loadMusic("./Sounds/startMusic.wav")
        start_music.setVolume(0.5)
        music_loop = self.loader.loadMusic("./Sounds/MusiqueLoop.wav")
        music_loop.setVolume(0.5)
        start_music.play()
        music_loop.setLoop(True)
        music_loop.play()


if __name__ == "__main__":
    music = MusicPlayer()
    music.run()
