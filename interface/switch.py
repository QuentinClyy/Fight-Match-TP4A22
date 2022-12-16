from tkinter import Tk
from interface.menu_parametres import MainMenu


class Switch(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1600x900")
        # self.attributes('-fullscreen', True)
        self.update()

        self.width = self.winfo_width()
        self.height = self.winfo_height()
        self.canvas = None
        self.switch_menu_canvas(MainMenu)

    def switch_menu_canvas(self, canvas_class):
        new_canvas = canvas_class(self, self.width, self.height)
        print(canvas_class)
        if self.canvas is not None:
            self.canvas.destroy()
        self.canvas = new_canvas
        self.canvas.pack(fill="both", expand=True)




    # def back_command(self):