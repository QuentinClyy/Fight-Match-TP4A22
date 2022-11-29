from tkinter import *
from mainmenu import MainMenu

root = Tk()
root.title('FightMatch')
root.attributes('-fullscreen', True)
# root.iconbitmap()
root.update()
width = root.winfo_width()
height = root.winfo_height()

main_menu = MainMenu(root, width, height)
main_menu.create_background()
main_menu.load_characters()
main_menu.load_title()

root.mainloop()
