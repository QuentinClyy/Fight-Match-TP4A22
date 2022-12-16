from interface.menu import Menu


class MainMenu(Menu):

    def __init__(self, master, width, height):
        super().__init__(master, width, height)

        self.launch_button = self.create_menu_button("Play", self.width, self.height,
                                                     self.textures,
                                                     lambda: master.switch_menu_canvas(ArenaSizeMenu))

        self.options_button = self.create_menu_button("Options", self.width, self.height,
                                                      self.textures, lambda: None)

        self.quit_button = self.create_menu_button("Quit", self.width, self.height,
                                                   self.textures, master.quit)

        self.bg_init()
        self.create_window((self.width // 2),
                           (self.height - self.height // 1.75),
                           anchor="center",
                           window=self.launch_button)
        self.create_window((self.width / 2),
                           (self.height - self.height // 2.8),
                           anchor="center",
                           window=self.options_button)
        self.create_window((self.width / 2),
                           (self.height - self.height // 7),
                           anchor="center",
                           window=self.quit_button)
        self.pack(fill="both", expand=True)


class ArenaSizeMenu(Menu):

    def __init__(self, master, width, height):
        super().__init__(master, width, height)

        self.small_arena_button = self.create_menu_button("Small", self.width, self.height,
                                                          self.textures, lambda: self.size_arena_command(5))

        self.mid_arena_button = self.create_menu_button("Medium", self.width, self.height,
                                                        self.textures, lambda: self.size_arena_command(7))

        self.big_arena_button = self.create_menu_button("Large", self.width, self.height,
                                                        self.textures, lambda: self.size_arena_command(9))

        self.back_button = self.create_back_button("Back", self.textures)
        self.back_button.config(command=lambda: master.switch_menu_canvas(MainMenu))

        self.bg_init()

        self.create_window((self.width // 2),
                           (self.height - self.height // 1.75),
                           anchor="center",
                           window=self.small_arena_button)
        self.create_window((self.width // 2),
                           (self.height - self.height // 2.8),
                           anchor="center",
                           window=self.mid_arena_button)
        self.create_window((self.width // 2),
                           (self.height - self.height // 7),
                           anchor="center",
                           window=self.big_arena_button)
        self.create_window((self.width - self.width // 38.4),
                           (self.height - self.height // 21.6),
                           anchor="se",
                           window=self.back_button)
        self.pack(fill="both", expand=True)

    def size_arena_command(self, valeur):
        self.arene_size = valeur
        self.master.switch_menu_canvas(NombreJoueursMenu)


class NombreDeMenu(Menu):
    def __init__(self, master, width, height):
        super().__init__(master, width, height)


class NombreJoueursMenu(Menu):
    def __init__(self, master, width, height):
        super().__init__(master, width, height)

        self.bg_init()
        self.boutons_joueur = []
        for i in range(4):
            bouton_joueur = self.create_player_button("Inactif",
                                                      self.width - self.width // 2.7,
                                                      self.height,
                                                      self.textures, lambda c=i: self.changer_type_joueur(c))
            self.create_window((self.width - self.width // 2.6) - (i % 2)*(self.width // 4),
                               (self.height - self.height // 3) - (i // 2)*(self.height // 4),
                               anchor="center",
                               window=bouton_joueur)
            self.boutons_joueur.append(bouton_joueur)

        self.start_button = self.create_menu_button("Start !", self.width, self.height,
                                                    self.textures, lambda: None)
        self.create_window((self.width // 2),
                           (self.height - self.height // 9),
                           anchor="center",
                           window=self.start_button)

        self.back_button = self.create_back_button("Back", self.textures)
        self.back_button.config(command=lambda: master.switch_menu_canvas(ArenaSizeMenu))
        self.create_window((self.width - self.width // 38.4),
                           (self.height - self.height // 21.6),
                           anchor="se",
                           window=self.back_button)

        self.pack(fill="both", expand=True)

    def changer_type_joueur(self, i):
        """
        Cette fonction permet de modifier le contenu du bouton dont
        le numéro est en paramètres.

        Args:
            i (int): Le numéro du bouton à modifier
        """
        if self.boutons_joueur[i]['text'] == "Inactif":
            self.boutons_joueur[i]['text'] = "Humain"
        elif self.boutons_joueur[i]['text'] == "Humain":
            self.boutons_joueur[i]['text'] = "Ordinateur"
        else:
            self.boutons_joueur[i]['text'] = "Inactif"





