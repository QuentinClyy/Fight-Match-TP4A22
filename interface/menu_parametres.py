from interface.menu import Menu


class MainMenu(Menu):

    def __init__(self, master, width, height):
        super().__init__(master, width, height)

        # creating buttons
        self.launch_button = self.create_menu_button("Play", self.width, self.height,
                                                     self.textures,
                                                     lambda: master.switch_canvas(ArenaSizeMenu))

        self.options_button = self.create_menu_button("Options", self.width, self.height,
                                                      self.textures, lambda: None)

        self.quit_button = self.create_menu_button("Quit", self.width, self.height,
                                                   self.textures, master.quit)

        self.bg_init()
        self.launch_window = self.create_window((self.width / 2),
                                                            (self.height - self.height / 1.75),
                                                            anchor="center",
                                                            window=self.launch_button)
        self.options_window = self.create_window((self.width / 2),
                                                             (self.height - (self.height / 2.8)),
                                                             anchor="center",
                                                             window=self.options_button)
        self.quit_window = self.create_window((self.width / 2),
                                                          (self.height - (self.height / 7)),
                                                          anchor="center",
                                                          window=self.quit_button)
        self.pack(fill="both", expand=True)

    # def play_command(self):


class ArenaSizeMenu(Menu):

    def __init__(self, master, width, height):
        super().__init__(master, width, height)

        self.small_arena_button = self.create_menu_button("Small", self.width, self.height,
                                                          self.textures, self.size_arena_command(5))

        self.mid_arena_button = self.create_menu_button("Medium", self.width, self.height,
                                                        self.textures, self.size_arena_command(7))

        self.big_arena_button = self.create_menu_button("Large", self.width, self.height,
                                                        self.textures, self.size_arena_command(9))

        self.back_button = self.create_back_button("Back", self.textures)
        self.back_button.config(command=lambda: master.switch_canvas(MainMenu))

        self.bg_init()

        self.small_window = self.create_window((self.width/2),
                                                           (self.height - self.height / 1.75),
                                                           anchor="center",
                                                           window=self.small_arena_button)
        self.mid_window = self.create_window((self.width/2),
                                                         (self.height - self.height / 2.8),
                                                         anchor="center",
                                                         window=self.mid_arena_button)
        self.big_window = self.create_window((self.width/2),
                                                         (self.height - self.height / 7),
                                                         anchor="center",
                                                         window=self.big_arena_button)
        self.quit_window = self.create_window(self.width-(self.width/38.4),
                                                          self.height - (self.height / 21.6),
                                                          anchor="se",
                                                          window=self.back_button)
        self.pack(fill="both", expand=True)

    def size_arena_command(self, valeur):
        pass
        self.arene_size = valeur
        # self.master.switch_canvas()

