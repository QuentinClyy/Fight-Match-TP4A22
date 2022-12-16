from interface.fenetre_principale import FenetrePrincipale
from interface.music_player import MusicPlayer

root = FenetrePrincipale()

music_player = MusicPlayer()
music_player.play_music()

root.mainloop()
