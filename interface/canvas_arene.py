from tkinter import Canvas, ALL, LAST
from texture_loader import GameTextureLoader


class CanvasArene(Canvas):
    def __init__(self, master, arene, width, height):
        """
        Constructeur de la classe CanvasArene. Attribue les dimensions en pixels
        en fonction des dimensions de l'arène, dessine l'arène dans l'interface
        et associe le clic de souris à la méthode selectionner_case.

        Args:
            master (Tk): Le widget TKinter dans lequel le canvas s'intègre.
            arene (Arene): L'arène des GlaDéateurs à afficher.
        """
        self.arene = arene
        self.width = width
        self.height = height
        super().__init__(master, width=self.width,
                         height=self.height,
                         borderwidth=0, highlightthickness=0)

        self.textures = GameTextureLoader(self.width, self.height)
        self.des = self.arene.des

    def afficher_de(self):
        for coordonnes, de in self.des.items():
            if de is not None:
                (x, y) = coordonnes
                valeur_de = de.affichage_de(self.arene.mode_affichage)
                self.create_image(x, y, image=getattr(self.textures, valeur_de), anchor="center")

    def affichage_arene(self, lancer=None):
        self.create_image(0, 0, image=self.textures.arene_bg, anchor="nw")
        if lancer is None:
            trajectoire = []
        elif type(lancer) is list:
            trajectoire = lancer
        else:
            trajectoire = lancer.trajectoire

        for (x, y) in self.des.keys():
            if (x, y) in trajectoire:
                self.create_image(x, y, image=self.textures.arene_tile_dark, anchor="center")
            else:
                self.create_image(x, y, image=self.textures.arene_tile, anchor="center")
        self.afficher_de()
        self.pack(fill="both", expand=True)
