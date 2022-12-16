import sys
from tkinter import Tk
from interface.main_menu import MainMenu
from interface.menu_parametres import MenuParametres
from interface.canvas_arene import CanvasArene


class FenetrePrincipale(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1600x900")
        self.attributes('-fullscreen', True)
        self.update()

        self.arene = None
        self.joueurs = None

        self.width = self.winfo_width()
        self.height = self.winfo_height()
        self.canvas = None
        self.switch_menu_canvas("MainMenu")

    def switch_menu_canvas(self, canvas_class):
        if canvas_class == "CanvasArene":
            new_canvas = getattr(sys.modules[__name__], canvas_class)(self, self.arene)
        else:
            new_canvas = getattr(sys.modules[__name__], canvas_class)(self)
        if self.canvas is not None:
            self.canvas.destroy()
        self.canvas = new_canvas
        self.canvas.pack(fill="both", expand=True)
