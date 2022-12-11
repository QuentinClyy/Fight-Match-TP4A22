from helper import *


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


class MainMenu(BaseMenu):

    def __init__(self, master, width, height):
        super().__init__(master, width, height)
        self.master = master
        self.width = width
        self.height = height
        # creating buttons
        self.launch_button = create_menu_button(self.master, "Play", self.width, self.height, self.textures)
        self.launch_button.config(command=self.play_command)

        self.options_button = create_menu_button(self.master, "Options", self.width, self.height, self.textures)

        self.quit_button = create_menu_button(self.master, "Quit", self.width, self.height, self.textures)
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
        arena_sm = ArenaSizeMenu(self.master, self.width, self.height)
        arena_sm.arena_size_menu_init()


class ArenaSizeMenu(BaseMenu):

    def __init__(self, master, width, height):
        BaseMenu.__init__(self, master, width, height)
        self.small_arena_button = create_menu_button(self.master, "Small", self.width, self.height, self.textures)
        self.mid_arena_button = create_menu_button(self.master, "Medium", self.width, self.height, self.textures)
        self.big_arena_button = create_menu_button(self.master, "Large", self.width, self.height, self.textures)

    def arena_size_menu_init(self):
        self.bg_init(self.size_arena_canvas)
        self.size_arena_canvas.create_window((self.width/2),
                                             (self.height - self.height / 1.75),
                                             anchor="center",
                                             window=self.small_arena_button)
        self.size_arena_canvas.create_window((self.width/2),
                                             (self.height - self.height / 2.8),
                                             anchor="center",
                                             window=self.mid_arena_button)
        self.size_arena_canvas.create_window((self.width/2),
                                             (self.height - self.height / 7),
                                             anchor="center",
                                             window=self.big_arena_button)

        self.size_arena_canvas.pack(fill="both", expand=True)
