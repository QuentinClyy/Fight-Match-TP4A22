from tkinter import Canvas, ALL, LAST
from interface.texture_loader import GameTextureLoader


class CanvasArene(Canvas):
    def __init__(self, master, arene, width, height):
        """
        Constructeur de la classe CanvasArene. Attribue les dimensions en pixels
        en fonction des dimensions de l'arène, dessine l'arène dans l'interface
        et associe le clic de souris à la méthode selectionner_case.

        Args:
            master (Tk): Le widget TKinter dans lequel le canvas s'intègre.
            arene (Arene): L'arène des GlaDéateurs à afficher.
            width (int): Largeur du canvas
            height (int): Hauteur du canvas
        """
        self.arene = arene
        self.width = width
        self.height = height
        super().__init__(master, width=self.width,
                         height=self.height,
                         borderwidth=0, highlightthickness=0)

        self.textures = GameTextureLoader(self.width, self.height)
        self.des = self.arene.des

    def dessiner_un_de(self, valeur_de):
        exterieur = (droite - gauche) // 10
        interieur = (droite - gauche - 4 * exterieur) // 3
        if valeur_de in ["⚀", "⚂", "⚄"]:
            self.create_oval(gauche + 2 * exterieur + interieur, haut + 2 * exterieur + interieur,
                             gauche + 2 * exterieur + 2 * interieur, haut + 2 * exterieur + 2 * interieur,
                             fill='black')
        if valeur_de in ["⚁", "⚂", "⚃", "⚄", "⚅"]:
            self.create_oval(gauche + exterieur, haut + exterieur,
                             gauche + exterieur + interieur, haut + exterieur + interieur, fill='black')
            self.create_oval(droite - exterieur, bas - exterieur,
                             droite - exterieur - interieur, bas - exterieur - interieur, fill='black')
        if valeur_de in ["⚃", "⚄", "⚅"]:
            self.create_oval(droite - exterieur, haut + exterieur,
                             droite - exterieur - interieur, haut + exterieur + interieur, fill='black')
            self.create_oval(gauche + exterieur, bas - exterieur,
                             gauche + exterieur + interieur, bas - exterieur - interieur, fill='black')
        if valeur_de == "⚅":
            self.create_oval(droite - exterieur, haut + 2 * exterieur + interieur,
                             droite - exterieur - interieur, haut + 2 * exterieur + 2 * interieur, fill='black')
            self.create_oval(gauche + exterieur, haut + 2 * exterieur + interieur,
                             gauche + exterieur + interieur, haut + 2 * exterieur + 2 * interieur, fill='black')

    def dessiner_tous_les_des(self):
        # valeur_de, x, y = 0, 0, 0
        for coordonnes, de in self.des.items():
            if de is not None:
                x, y = coordonnes
                valeur_de = de.affichage_string(self.arene.mode_affichage)
                print(valeur_de)
                if valeur_de in ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]:
                    pass
                else:
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
        self.dessiner_tous_les_des()
        self.pack(fill="both", expand=True)


