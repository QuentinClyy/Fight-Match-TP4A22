from interface.switch import Switch
from interface.music_player import MusicPlayer



root = Switch()

music_player = MusicPlayer()
music_player.play_music()

root.mainloop()
