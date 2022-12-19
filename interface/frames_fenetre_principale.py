"""
Module contenant des frames utilitaires présents dans la fenêtre principale.
"""

from tkinter import Frame, Label, Button, Scale, VERTICAL, IntVar

from interface.joueur_ordinateur import JoueurOrdinateur


class FrameDescription(Frame):
    def __init__(self, master):
        """
        Constructeur de la classe FrameDescription. Affiche un descriptif
        de ce qui se passe dans le jeu.

        Args:
            master (Tk): La fenêtre dans laquelle ce frame s'insert.
        """
        super().__init__(master)
        self.label_description = Label(self, text="")
        self.label_description.grid(row=0, column=0)

    def populer(self, texte, temps_attente, suite):
        """
        Cette méthode affiche les informations sur le jeu.

        Args:
            texte (str): Le message à afficher
            temps_attente (int): Temps en millisecondes avant d'exécuter la suite
            suite (fonction): La fonction à exécuter après
        """
        self.label_description['text'] = texte
        self.after(temps_attente, suite)

    def vider(self):
        """
        Cette méthode enlève l'affichage.
        """
        self.label_description['text'] = ""


class FrameJoueurActif(Frame):
    def __init__(self, master):
        """
        Constructeur de la classe FrameJoueurActif. Affiche les informations relatives au
        joueur dont c'est le tour.

        Args:
            master (Tk): La fenêtre dans laquelle ce frame s'insert.
        """
        super().__init__(master)

        self.label_nom_joueur = Label(self, text="")
        self.label_nombre_des = Label(self, text="")

        self.label_nom_joueur.grid(row=0, column=0)
        self.label_nombre_des.grid(row=1, column=0)

        self.clic_bouton = lambda: None
        self.bouton_terminer_tour = Button(self, text="Terminer le tour", command=self.appui_bouton)
        self.bouton_terminer_tour.grid(row=1, column=1)
        self.bouton_terminer_tour["state"] = "disabled"

        self.couleurs = [
            'blue', 'green', 'red', 'orange', 'purple'
        ]

    def populer(self, joueur):
        """
        Ajoute les informations d'un joueur dans le frame.

        Args:
            joueur (Joueur): le joueur dont c'est le tour
        """
        self.label_nom_joueur["text"] = f"Joueur # {joueur.numero_joueur}"
        self.label_nombre_des["text"] = f"{len(joueur.des)} dés"
        self.label_nom_joueur["fg"] = self.couleurs[joueur.numero_joueur - 1]
        self.label_nombre_des["fg"] = self.couleurs[joueur.numero_joueur - 1]

    def activer_bouton(self, fonction):
        """
        Permet de cliquer sur le bouton fin du tour, et associe la fonction au clic.

        Args:
            fonction (fonction): La fonction à exécuter suite au clic de bouton
        """
        self.bouton_terminer_tour["state"] = "normal"
        self.clic_bouton = fonction

    def appui_bouton(self):
        """
        Effectue la fonction à exécuter suite au clic de bouton, et grise le bouton.
        """
        self.bouton_terminer_tour["state"] = "disabled"
        self.clic_bouton()


class FrameTableauJoueurs(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.joueurs = self.master.joueurs
        self.couleurs = self.master.frame_joueur.couleurs
        self.liste_label = []
        i = 0
        for joueur in self.joueurs:
            nombre_des = len(joueur.des)
            label_joueur = Label(self, text=f"Joueur {joueur.numero_joueur}: {nombre_des}")
            label_joueur["fg"] = self.couleurs[joueur.numero_joueur - 1]
            label_joueur.grid(row=i, column=0)
            i += 1
            self.liste_label.append(label_joueur)

    def mise_a_jour(self):
        i = 0
        for joueur in self.joueurs:
            nombre_des = len(joueur.des)
            if nombre_des == 0:
                nombre_des = "éliminé"
            label = self.liste_label[i]
            label.config(text=f"Joueur {joueur.numero_joueur}: {nombre_des}")
            i += 1


class FrameTempsAttente(Frame):
    def __init__(self, master):
        super().__init__(master)
        #### DÉBUT DÉFI TEMPS ATTENTE ####
        self.scale = Scale(self, from_=50, to=500,
                           label="Vitesse Joueur CPU",
                           orient="horizontal", width=20,
                           relief="ridge", length=110)
        self.scale.grid()
        #### FIN DÉFI TEMPS ATTENTE ####
