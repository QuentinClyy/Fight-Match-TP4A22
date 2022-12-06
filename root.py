from tkinter import *
from mainmenu import MainMenu

root = Tk()
root.title('FightMatch')
# root.geometry("1280x720")
# root.geometry("1600x900")
root.attributes('-fullscreen', True)
root.iconbitmap(r'./Images/icon.ico')
root.update()
width = root.winfo_width()
height = root.winfo_height()

main_menu = MainMenu(root, width, height)
main_menu.main_menu_init()

root.mainloop()
