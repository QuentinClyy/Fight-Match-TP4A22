import sys
from tkinter import Tk, messagebox, Button, font
from interface.main_menu import MainMenu
from interface.menu_parametres import MenuParametres
from interface.canvas_principal import CanvasPrincipal
from interface.menu_options import MenuOptions
from interface.music_player import MusicPlayer
from jeu.gladeateur import Gladeateur
from interface.joueur_ordinateur import JoueurOrdinateur
from interface.gestionnaire_io_interface import GestionnaireIOInterface
from interface.frames_fenetre_principale import FrameDescription, FrameJoueurActif, FrameTableauJoueurs, \
    FrameTempsAttente


class FenetrePrincipale(Tk):
    def __init__(self):
        super().__init__()
        self.attributes('-fullscreen', True)
        self.update()

        self.music_player = MusicPlayer()

        self.arene = None
        self.joueurs = None

        self.width = self.winfo_width()
        self.height = self.winfo_height()
        self.canvas = None
        self.switch_menu_canvas("MainMenu")

    def switch_menu_canvas(self, canvas_class):
        new_canvas = getattr(sys.modules[__name__], canvas_class)(self)
        if self.canvas is not None:
            self.canvas.destroy()
        self.canvas = new_canvas
        self.canvas.pack(fill="both", expand=True)

    def demarrer(self):
        """
        Lance une partie.
        """
        self.switch_menu_canvas("CanvasPrincipal")

        self.frame_description = FrameDescription(self)
        self.canvas.create_window(self.width // 2,
                                  self.height - self.height // 9,
                                  anchor="center", window=self.frame_description)

        self.frame_joueur = FrameJoueurActif(self)
        self.canvas.create_window(self.width // 2,
                                  self.height - self.height // 15,
                                  anchor="center", window=self.frame_joueur)

        self.joueur_index = 0
        self.joueur_actuel = self.joueurs[self.joueur_index]

        self.gestionnaire_io = GestionnaireIOInterface(self, self.canvas, self.frame_description)

        self.frame_tableau_joueurs = FrameTableauJoueurs(self)
        self.frame_temps_attente = FrameTempsAttente(self)
        self.canvas.create_window((self.width - self.width // 5),
                                  self.height // 2,
                                  anchor="center", window=self.frame_tableau_joueurs)
        self.canvas.create_window((self.width - self.width // 5),
                                  self.height // 2 + self.height // 8,
                                  anchor="center", window=self.frame_temps_attente)

        self.quit_button = Button(self,
                                  width=int(self.width // 7.2),
                                  height=int(self.height // 15),
                                  borderwidth=0,
                                  bg='#4d330f', activebackground='#4d330f',
                                  fg='#ad2513', activeforeground='#63170d',
                                  command=self.quit)
        self.quit_button.config(image=self.canvas.textures.button_panel, text="Quit", compound="center")
        button_font = font.Font(family='Roman', size=25)
        self.quit_button['font'] = button_font
        self.canvas.create_window((self.width - self.width // 10),
                                  (self.height - self.height // 20),
                                  anchor="center",
                                  window=self.quit_button)

        self.gladeateur = Gladeateur(self.joueurs, self.arene, self.gestionnaire_io)
        self.gladeateur.jouer_partie()

    def est_joueur_ordi(self):
        """
        Cette méthode indique s'il s'agit d'un joueur ordinateur

        Returns:
            bool: True s'il s'agit d'un ordinateur, False si joueur humain
        """
        return isinstance(self.joueur_actuel, JoueurOrdinateur)

    def redessiner(self, temps_attente, suite):
        """
        Cette méthode active le redessinage de l'arène, et déclenche
        la suite.

        Args:
            temps_attente (int): Temps en millisecondes avant d'exécuter la suite
            suite (fonction): La fonction à exécuter suite au redessinage
        """

        self.canvas.canvas_arene.dessiner_canvas(lambda: None)
        self.frame_description.vider()

        if not self.est_joueur_ordi():
            temps_attente = 0
        self.after(temps_attente, suite)

    def afficher_joueur(self, joueur, temps_attente, suite):
        """
        Cette méthode affiche le joueur en cours

        Args:
            joueur (Joueur): Le joueur à afficher
            temps_attente (int): Temps en millisecondes avant d'exécuter la suite
            suite (fonction): La fonction à exécuter suite à l'affichage du joueur
        """
        self.frame_tableau_joueurs.mise_a_jour()
        self.frame_joueur.populer(joueur)
        self.redessiner(temps_attente, suite)

    def afficher_gagnant(self, joueur):
        """
        Affiche le gagnant de la partie.
        """
        messagebox.showinfo("Fin de la partie", f"Victoire du {str(joueur)}")
        self.canvas.canvas_arene.permettre_clics(lambda _: None, None)
        self.frame_tableau_joueurs.mise_a_jour()
        self.quit_button.config(command=lambda: self.switch_menu_canvas("MainMenu"))
        self.frame_joueur.populer(joueur)
