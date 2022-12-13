import interface.menu as menu
import interface.arena_size_menu as asm
import tkinter as tk


class MainMenu(menu.Menu):

    def __init__(self, master, width, height):
        super().__init__(master, width, height)
        self.master = master
        self.width = width
        self.height = height
        self.main_canvas = tk.Canvas(self.master, width=self.width, height=self.height)
        # creating buttons
        self.launch_button = self.create_menu_button("Play", self.width, self.height, self.textures)
        self.launch_button.config(command=self.play_command)

        self.options_button = self.create_menu_button("Options", self.width, self.height, self.textures)

        self.quit_button = self.create_menu_button("Quit", self.width, self.height, self.textures)
        self.quit_button.config(command=self.master.quit)

    def main_menu_init(self):
        self.bg_init(self.main_canvas)
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
        self.main_canvas.destroy()
        arena_sm = asm.ArenaSizeMenu(self.master, self.width, self.height)
        arena_sm.arena_size_menu_init()

