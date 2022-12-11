from tkinter import *
from index import *
from musicPlayer import *

root = Tk()
# root.geometry("1600x900")
root.attributes('-fullscreen', True)
root.update()
width = root.winfo_width()
height = root.winfo_height()

main_menu = MainMenu(root, width, height)
main_menu.main_menu_init()

musicplayer = MusicPlayer()
musicplayer.play_music()

root.mainloop()
