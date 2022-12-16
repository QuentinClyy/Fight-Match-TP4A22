from tkinter import Button, messagebox
from interface.menu import Menu
from interface.joueur_humain import JoueurHumain
from interface.joueur_ordinateur import JoueurOrdinateur
from jeu.de import De


class MainMenu(Menu):

    def __init__(self, master):
        super().__init__(master)

        self.launch_button = self.create_menu_button("Play", lambda: master.switch_menu_canvas(ArenaSizeMenu))

        self.options_button = self.create_menu_button("Options", lambda: None)

        self.quit_button = self.create_menu_button("Quit",master.quit)
        self.remplissage_auto_button = Button(self,
                                              width=int(self.master.width // 60),
                                              height=int(self.master.height // 300),
                                              text="Default Settings", command=self.master.remplissage_auto)

        self.bg_init()
        self.create_window((self.master.width // 2),
                           (self.master.height - self.master.height // 1.75),
                           anchor="center",
                           window=self.launch_button)
        self.create_window((self.master.width / 2),
                           (self.master.height - self.master.height // 2.8),
                           anchor="center",
                           window=self.options_button)
        self.create_window((self.master.width / 2),
                           (self.master.height - self.master.height // 7),
                           anchor="center",
                           window=self.quit_button)
        self.create_window((self.master.width - self.master.width // 38.4),
                           (self.master.height - self.master.height // 21.6),
                           anchor="se",
                           window=self.remplissage_auto_button)
        self.pack(fill="both", expand=True)


class ArenaSizeMenu(Menu):

    def __init__(self, master):
        super().__init__(master)

        self.small_arena_button = self.create_menu_button("Small", lambda: self.size_arena_command(5))

        self.mid_arena_button = self.create_menu_button("Medium", lambda: self.size_arena_command(7))

        self.big_arena_button = self.create_menu_button("Large", lambda: self.size_arena_command(9))

        self.back_button = self.create_back_button("Back", self.textures)
        self.back_button.config(command=lambda: master.switch_menu_canvas(MainMenu))

        self.bg_init()

        self.create_window((self.master.width // 2),
                           (self.master.height - self.master.height // 1.75),
                           anchor="center",
                           window=self.small_arena_button)
        self.create_window((self.master.width // 2),
                           (self.master.height - self.master.height // 2.8),
                           anchor="center",
                           window=self.mid_arena_button)
        self.create_window((self.master.width // 2),
                           (self.master.height - self.master.height // 7),
                           anchor="center",
                           window=self.big_arena_button)
        self.create_window((self.master.width - self.master.width // 38.4),
                           (self.master.height - self.master.height // 21.6),
                           anchor="se",
                           window=self.back_button)
        self.pack(fill="both", expand=True)

    def size_arena_command(self, valeur):
        self.master.arene_size = valeur
        self.master.switch_menu_canvas(NombreDesMenu)


class NombreDesMenu(Menu):
    def __init__(self, master):
        super().__init__(master)

        self.few_des_button = self.create_menu_button("5 Gladiators", lambda: self.nombre_des_command(5))

        self.some_des_button = self.create_menu_button("10 Gladiators", lambda: self.nombre_des_command(10))

        self.lot_des_button = self.create_menu_button("15 Gladiators", lambda: self.nombre_des_command(15))

        self.back_button = self.create_back_button("Back", self.textures)
        self.back_button.config(command=lambda: master.switch_menu_canvas(ArenaSizeMenu))

        self.bg_init()

        self.create_window((self.master.width // 2),
                           (self.master.height - self.master.height // 1.75),
                           anchor="center",
                           window=self.few_des_button)
        self.create_window((self.master.width // 2),
                           (self.master.height - self.master.height // 2.8),
                           anchor="center",
                           window=self.some_des_button)
        self.create_window((self.master.width // 2),
                           (self.master.height - self.master.height // 7),
                           anchor="center",
                           window=self.lot_des_button)
        self.create_window((self.master.width - self.master.width // 38.4),
                           (self.master.height - self.master.height // 21.6),
                           anchor="se",
                           window=self.back_button)
        self.pack(fill="both", expand=True)

    def nombre_des_command(self, valeur):
        self.master.nombre_des = valeur
        self.master.switch_menu_canvas(NombreJoueursMenu)


class NombreJoueursMenu(Menu):
    def __init__(self, master):
        super().__init__(master)

        self.bg_init()
        for i in range(4):
            bouton_joueur = self.create_player_button("Inactif", lambda c=i: self.changer_type_joueur(c))
            self.create_window((self.master.width - self.master.width // 2.6) - (i % 2)*(self.master.width // 4),
                               (self.master.height - self.master.height // 3) - (i // 2)*(self.master.height // 4),
                               anchor="center",
                               window=bouton_joueur)
            self.master.boutons_joueur.append(bouton_joueur)

        self.start_button = self.create_menu_button("Start !", lambda: None)
        self.create_window((self.master.width // 2),
                           (self.master.height - self.master.height // 8),
                           anchor="center",
                           window=self.start_button)

        self.back_button = self.create_back_button("Back", self.textures)
        self.back_button.config(command=lambda: master.switch_menu_canvas(NombreDesMenu))
        self.create_window((self.master.width - self.master.width // 38.4),
                           (self.master.height - self.master.height // 21.6),
                           anchor="se",
                           window=self.back_button)

        self.pack(fill="both", expand=True)



    def obtenir_joueurs(self, arene, nb_des_par_joueur, fenetre_jeu):
        """
        Cette méthode crée les joueurs en fonction du contenu des boutons.

        Returns:
            list: La liste des joueurs
        """
        joueurs = []
        n_des_joueurs = 30
        n_joueurs = sum(map(lambda bouton: int(bouton['text'] != 'Inactif'), self.master.boutons_joueur))

        for i, bouton_joueur in enumerate(self.master.boutons_joueur):
            des = [De() for _ in range(nb_des_par_joueur)]
            if bouton_joueur['text'] == "Humain":
                joueurs.append(JoueurHumain(i + 1, des, arene, fenetre_jeu))
            elif bouton_joueur['text'] == "Ordinateur":
                joueurs.append(JoueurOrdinateur(i + 1, des, arene))
        if len(joueurs) < 2:
            raise ValueError("Trop peu de joueurs!")
        return joueurs

    def changer_type_joueur(self, i):
        """
        Cette fonction permet de modifier le contenu du bouton dont
        le numéro est en paramètres.

        Args:
            i (int): Le numéro du bouton à modifier
        """
        if self.master.boutons_joueur[i]['text'] == "Inactif":
            self.master.boutons_joueur[i]['text'] = "Humain"
        elif self.master.boutons_joueur[i]['text'] == "Humain":
            self.master.boutons_joueur[i]['text'] = "Ordinateur"
        else:
            self.master.boutons_joueur[i]['text'] = "Inactif"





