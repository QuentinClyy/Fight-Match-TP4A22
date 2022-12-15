import tkinter as tk
from interface.main_menu import MainMenu
from interface.music_player import MusicPlayer

root = tk.Tk()
# root.geometry("1600x900")
root.attributes('-fullscreen', True)
root.update()
width = root.winfo_width()
height = root.winfo_height()

main_menu = MainMenu(root, width, height)
main_menu.main_menu_init()

music_player = MusicPlayer()
music_player.play_music()

root.mainloop()
