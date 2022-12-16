from tkinter import Canvas, ALL, LAST
from interface.texture_loader import GameTextureLoader
import itertools


class CanvasArene(Canvas):
    def __init__(self, master, arene):
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
        super().__init__(master)
        self.arene = arene
        self.textures = GameTextureLoader(self.master.width, self.master.height)

        self.suite_clic = None
        self.coordonnees_cliquables = lambda coordonnees: False
        self.bind("<Button-1>", self.selectionner_case)

        self.affichage_arene(lambda: None)

    def placement_arene(self):
        """

        Returns:
            tuple:

        """
        width_addition = 0
        height_addition = 0
        if self.arene.dimension == 5:
            width_addition = 775
            height_addition = 300
        elif self.arene.dimension == 7:
            width_addition = 675
            height_addition = 250
        elif self.arene.dimension == 9:
            width_addition = 610
            height_addition = 200

        return width_addition, height_addition

    def coordonnees_en_pixel(self, x, y):
        """
        Cette méthode des coordonnées de l'arène en position en pixels

        Args:
            x (int): La coordonnée en x
            y (int): La coordonnée en y

        Returns:
            tuple: La position en pixels.
        """
        (width_addition, height_addition) = self.placement_arene()

        x_return = width_addition + 90 * x
        y_return = height_addition + 90 * y

        return x_return, y_return

    def pixel_en_coordonnees(self, x_pixel, y_pixel):
        """
        Cette méthode convertit la position d'un clic en coordonnées de l'arène.

        Args:
            x_pixel: La position du clic, en x (de haut en bas)
            y_pixel: La position du clic, en y (de gauche à droite)

        Returns:
            tuple: Les coordonnées de la case cliquée.
        """
        (width_addition, height_addition) = self.placement_arene()

        x_return =  (x_pixel - width_addition) // 90
        y_return =  (y_pixel - height_addition) // 90

        return x_return, y_return

    def selectionner_case(self, event):
        """
        Cette méthode prend en argument un clic de souris sur le canvas, et actionne
        la fonction définie comme devant faire suite au clic (self.suite_clic), dont
        l'argument est en coordonnées plutôt qu'en pixels.

        Args:
            event (tkinter.Event): L'événement correspondant au clic

        """
        x, y = event.y, event.x  # nos coordonnées sont transposées par rapport aux pixels
        coordonnees = self.pixel_en_coordonnees(x, y)
        if self.suite_clic is not None and self.coordonnees_cliquables(coordonnees):
            self.suite_clic(coordonnees)

    def dessiner_un_de(self, valeur_de, gauche, haut, droite, bas):
        """
        Cette methode dessine un seul de en utilisant l'interface Tkinter en fonction de sa valeur
        et des coordonnees limites en pixel de la case sur laquelle il se trouve.

        Args:
            valeur_de (str): la valeur du de en string
            gauche (int): limite de la gauche de la case du de en pixel
            haut (int): limite du haut de la case du de en pixel
            droite (int): limite de la droite de la case du de en pixel
            bas (int): limite du bas de la case du de en pixel
        """
        self.create_rectangle(gauche, haut, droite, bas, fill='white',
                              outline='black', width=3)

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
        """
        Dessine tous les des selon leur mode d'affichage (1 = un de "tkinter", 2 = un galdeateur en pixel art)
        """
        for coordonnes, de in self.arene.des.items():
            if de is not None:
                x, y = coordonnes
                x_pixel, y_pixel = self.coordonnees_en_pixel(x, y)
                valeur_de = de.affichage_string(self.arene.mode_affichage)
                if valeur_de in ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]:
                    gauche = x_pixel + self.master.width // 85
                    haut = y_pixel + self.master.height // 47
                    droite = x_pixel - self.master.width // 85
                    bas = y_pixel - self.master.height // 47
                    self.dessiner_un_de(valeur_de, gauche, haut, droite, bas)
                else:
                    self.create_image(x_pixel, y_pixel, image=getattr(self.textures, valeur_de), anchor="center")

    def permettre_clics(self, case_cliquable, suite_clic):
        """
        Cette méthode associe une fonction à exécuter à ce qui doit arriver suite
        à un clic, pour les cases où le clic est permis.

        Args:
            case_cliquable (fonction): Fonction qui détermine si des coordonnées sont cliquables
            suite_clic (fonction): Fonction à exécuter suite au clic d'une cases
        """
        self.coordonnees_cliquables = case_cliquable
        self.suite_clic = suite_clic
        self.affichage_arene(lambda: None)

    def affichage_arene(self, suite):
        self.create_image(0, 0, image=self.textures.arene_bg, anchor="nw")

        for x, y in itertools.product(range(self.arene.dimension), range(self.arene.dimension)):
            (x_pixel, y_pixel) = self.coordonnees_en_pixel(x, y)
            self.create_image(x_pixel, y_pixel, image=self.textures.arene_tile, anchor="center")
        self.dessiner_tous_les_des()
        self.pack(fill="both", expand=True)

        suite()

    def affichage_lancer(self, lancer, temps_attente, suite):
        self.suite_clic = None
        self.coordonnees_cliquables = lambda _: False
        traj = lancer.trajectoire
        for i in range(len(traj) - 1):
            x1, y1 = traj[i]
            x2, y2 = traj[i + 1]
            self.create_line(*self.coordonnees_en_pixel(y1, x1),
                             *self.coordonnees_en_pixel(y2, x2),
                             arrow=LAST)

        self.after(temps_attente, suite)
