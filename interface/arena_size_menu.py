import interface.menu as menu
import interface.main_menu as mm
import tkinter as tk


class ArenaSizeMenu(menu.Menu):

    def __init__(self, master, width, height):
        super().__init__(master, width, height)
        self.size_arena_canvas = tk.Canvas(self.master, width=self.width, height=self.height)

        self.small_arena_button = self.create_menu_button("Small", self.width, self.height, self.textures)
        self.mid_arena_button = self.create_menu_button("Medium", self.width, self.height, self.textures)
        self.big_arena_button = self.create_menu_button("Large", self.width, self.height, self.textures)
        self.back_button = self.create_back_button("Back", self.textures)
        self.back_button.config(command=self.back_command)

    def arena_size_menu_init(self):
        self.bg_init(self.size_arena_canvas)
        self.size_arena_canvas.create_window((self.width/2),
                                             (self.height - self.height/1.75),
                                             anchor="center",
                                             window=self.small_arena_button)
        self.size_arena_canvas.create_window((self.width/2),
                                             (self.height - self.height/2.8),
                                             anchor="center",
                                             window=self.mid_arena_button)
        self.size_arena_canvas.create_window((self.width/2),
                                             (self.height - self.height/7),
                                             anchor="center",
                                             window=self.big_arena_button)
        self.size_arena_canvas.create_window(self.width-(self.width/38.4),
                                             self.height-(self.height/21.6),
                                             anchor="se",
                                             window=self.back_button)

        self.size_arena_canvas.pack(fill="both", expand=True)

    def back_command(self):
        self.size_arena_canvas.destroy()
        mainmenu = mm.MainMenu(self.master, self.width, self.height)
        mainmenu.main_menu_init()
