import sys
from tkinter import Tk, messagebox
from interface.main_menu import MainMenu
from interface.menu_parametres import MenuParametres
from interface.canvas_arene import CanvasArene
from jeu.gladeateur import Gladeateur
from interface.joueur_ordinateur import JoueurOrdinateur
from interface.gestionnaire_io_interface import GestionnaireIOInterface
from interface.frames_fenetre_principale import FrameDescription, FrameJoueurActif, FrameTableauJoueurs, \
    FrameTempsAttente


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

    def choix_des_parametres(self, canvas_class):
        self.switch_menu_canvas(canvas_class)

    def demarrer(self):
        """
        Lance une partie.
        """
        self.switch_menu_canvas("CanvasArene")

        self.frame_description = FrameDescription(self)
        self.canvas.create_window(self.width // 5, self.height // 5,
                                        anchor="se", window=self.frame_description)

        self.frame_joueur = FrameJoueurActif(self)
        self.canvas.create_window(self.width // 5, self.height // 5,
                                        anchor="se", window=self.frame_joueur)

        self.joueur_index = 0
        self.joueur_actuel = self.joueurs[self.joueur_index]

        self.gestionnaire_io = GestionnaireIOInterface(self, self.canvas, self.frame_description)

        self.frame_tableau_joueurs = FrameTableauJoueurs(self)
        self.frame_temps_attente = FrameTempsAttente(self)
        self.canvas.create_window(self.width // 5, self.height // 5,
                                  anchor="se", window=self.frame_tableau_joueurs)
        self.canvas.create_window(self.width // 5, self.height // 5,
                                  anchor="se", window=self.frame_temps_attente)

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

        self.canvas.dessiner_canvas(lambda: None)
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
        self.canvas.permettre_clics(lambda _: None, None)
        self.frame_joueur.populer(joueur)