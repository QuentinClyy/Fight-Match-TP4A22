import tkinter as tk
from Helper import *


class Program(tk.Tk):
    def __init__(self):
        super().__init__()
        self.main_canvas = None
        self.all_canvas = dict()
        self.switch_canvas()

    def switch_canvas(self, canvas_class):
        if self.main_canvas:
            self.main_canvas.pack_forger()

        canvas = self.all_canvas.get(canvas_class, False)

        if not canvas:
            canvas = canvas_class(self)
            self.all_canvas[canvas_class] = canvas

        canvas.pack(pady=60)
        self.main_canvas = canvas


class BaseMenu(tk.Frame):

    def __init__(self, master, width, height):
        super().__init__(master)
        self.master = master
        self.width = width
        self.height = height
        self.textures = MenuTextureLoader(self.width, self.height)

        # creating canvases
        self.main_canvas = tk.Canvas(self.master, width=self.width, height=self.height)
        self.size_arena_canvas = tk.Canvas(self.master, width=self.width, height=self.height)
        self.nb_players_canvas = tk.Canvas(self.master, width=self.width, height=self.height)
        self.nb_dice_canvas = tk.Canvas(self.master, width=self.width, height=self.height)

    def bg_init(self, canvas):
        canvas.create_image(0, 0, image=self.textures.menu_bg, anchor="nw")
        canvas.create_image(0, 0, image=self.textures.menu_left_char, anchor="nw")
        canvas.create_image(0, 0, image=self.textures.menu_right_char, anchor="nw")
        canvas.create_image(0, 0, image=self.textures.menu_title, anchor="nw")


class MainMenu(tk.Canvas):

    def __init__(self, master, width, height):
        super().__init__(master)
        self.master = master
        self.width = width
        self.height = height
        self.textures = MenuTextureLoader(self.width, self.height)
        self.main_canvas = tk.Canvas(self.master, width=self.width, height=self.height)
        # creating buttons
        self.launch_button = create_menu_button(self.master, "Play", self.width, self.height)
        # self.launch_button.config(command=self.play_command)

        self.options_button = create_menu_button(self.master, "Options", self.width, self.height)

        self.quit_button = create_menu_button(self.master, "Quit", self.width, self.height)
        # self.quit_button.config(command=self.master.quit)

    def main_menu_init(self):

        self.main_canvas.create_window((self.width/2),
                                       (self.height - self.height / 1.75),
                                       anchor="center",
                                       window=self.launch_button)
        self.main_canvas.create_window((self.width/2),
                                       (self.height - (self.height / 2.8)),
                                       anchor="center",
                                       window=self.options_button)
        self.main_canvas.create_window((self.width/2),
                                       (self.height - (self.height / 7)),
                                       anchor="center",
                                       window=self.quit_button)
        self.main_canvas.pack(fill="both", expand=True)

    def play_command(self):
        self.main_canvas.delete("all")
        self.main_canvas.destroy()
        arena_sm = ArenaSizeMenu(self.master, self.width, self.height)
        arena_sm.arena_size_menu_init()


class ArenaSizeMenu(BaseMenu):

    def __init__(self, master, width, height):
        BaseMenu.__init__(self, master, width, height)

    def arena_size_menu_init(self):
        self.size_arena_canvas.create_image(0, 0, image=self.textures.menu_bg, anchor="nw")
        self.size_arena_canvas.create_image(0, 0, image=self.textures.menu_left_char, anchor="nw")
        self.size_arena_canvas.create_image(0, 0, image=self.textures.menu_right_char, anchor="nw")
        self.size_arena_canvas.create_image(0, 0, image=self.textures.menu_title, anchor="nw")
        self.size_arena_canvas.pack(fill="both", expand=True)
