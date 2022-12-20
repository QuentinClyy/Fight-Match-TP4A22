"""
Module contenant la classe FenetreIntroduction et ses classes
utilitaires FrameArene et FrameJoueurs.
"""

from tkinter import IntVar, Button, Label, Entry, Frame, messagebox, RIDGE, \
    Checkbutton, END
from interface.menu import Menu
from jeu.arene import Arene
from jeu.de import De
from interface.joueur_ordinateur import JoueurOrdinateur
from interface.joueur_humain import JoueurHumain


class FrameArene(Frame):
    def __init__(self, master):
        """
        Constructeur de la classe FrameArene. Cette classe gère le menu
        de création de l'arène.

        Args:
            master (Frame): Le widget TKinter dans lequel la frame s'intègre.
        """
        super().__init__(master, borderwidth=1, relief=RIDGE, background='#d8c0a5')

        self.frame_dimension_carre = Frame(self)
        self.label_dimension_carre = Label(self.frame_dimension_carre, text="Size of one side: ",
                                           background='#d8c0a5')
        self.entry_dimension_carre = Entry(self.frame_dimension_carre, width=5,
                                           background='#d8c0a5')
        self.label_dimension_carre.grid(row=0, column=0)
        self.entry_dimension_carre.grid(row=0, column=1)
        self.frame_dimension_carre.grid(row=5, column=0, padx=5, pady=2)

        self.frame_nombre_des = Frame(self)
        self.label_nombre_des = Label(self.frame_nombre_des, text="Number of warriors per player: ",
                                      background='#d8c0a5')
        self.entry_nombre_des = Entry(self.frame_nombre_des, width=5,
                                      background='#d8c0a5')
        self.label_nombre_des.grid(row=0, column=0)
        self.entry_nombre_des.grid(row=0, column=1)
        self.frame_nombre_des.grid(row=6, column=0, padx=5, pady=2)

        self.mode_var = IntVar(value=0)
        self.mode_checkbutton = Checkbutton(self, text="Display warriors as dice", variable=self.mode_var,
                                            background='#d8c0a5', activebackground='#d8c0a5')
        self.mode_checkbutton.grid(row=4, column=0, padx=5, pady=2)

    def obtenir_arene(self):
        """
        Cette méthode crée une arène en fonction des paramètres déterminés dans le frame.

        Returns:
            Arene: L'arène créée.
        """
        try:
            dimension = int(self.entry_dimension_carre.get())
            if dimension < 3:
                raise ValueError
        except ValueError:
            raise ValueError("The size has to be greater or equal to 3 !")
        return Arene(dimension, De(), self.mode_var.get() + 1)

    def obtenir_nombre_des(self):
        """
        Cette fonction lit le nombre de dés inscrit dans l'entry correspondant
        Lance un exception si ce qui est inscrit n'est pas un entier valide.

        Returns:
            int: Le nombre de dés.
        """
        try:
            nb_des = int(self.entry_nombre_des.get())
            if nb_des < 1 or nb_des > 15:
                raise ValueError
            return nb_des
        except ValueError:
            raise ValueError("The quantity of warriors has to be between 1 and 15 !")


class FrameJoueurs(Frame):
    def __init__(self, master):
        """
        Constructeur de la classe FrameJoueurs. Cette classe gère le menu
        du choix des joueurs.

        Args:
            master (Frame): Le widget TKinter dans lequel la frame s'intègre.
        """
        super().__init__(master, borderwidth=1, relief=RIDGE, background='#d8c0a5')
        label_joueurs = Label(self, text="Select the players you want !",
                              background='#d8c0a5')
        label_joueurs.grid(row=0, column=0, padx=10, pady=10)
        self.boutons_joueur = []
        frame_boutons = Frame(self, background='#d8c0a5')
        frame_boutons.grid(row=5, column=0)
        for i in range(5):
            bouton_joueur = Button(frame_boutons, text="Inactive", width=8, font='sans 12',
                                   command=lambda c=i: self.changer_type_joueur(c),
                                   background='#d8c0a5', activebackground='#d8c0a5')
            bouton_joueur.grid(row=i // 2, column=i % 2, padx=5, pady=5)
            self.boutons_joueur.append(bouton_joueur)

    def obtenir_joueurs(self, arene, nb_des_par_joueur, fenetre_jeu):
        """
        Cette méthode crée les joueurs en fonction du contenu des boutons.

        Returns:
            list: La liste des joueurs
        """
        joueurs = []
        n_des_joueurs = 30
        n_joueurs = sum(map(lambda bouton: int(bouton['text'] != 'Inactive'), self.boutons_joueur))

        for i, bouton_joueur in enumerate(self.boutons_joueur):
            des = [De() for _ in range(nb_des_par_joueur)]
            if bouton_joueur['text'] == "Player":
                joueurs.append(JoueurHumain(i + 1, des, arene, fenetre_jeu))
            elif bouton_joueur['text'] == "Bot":
                joueurs.append(JoueurOrdinateur(i + 1, des, arene))
        if len(joueurs) < 2:
            raise ValueError("Not enough players !")
        return joueurs

    def changer_type_joueur(self, i):
        """
        Cette fonction permet de modifier le contenu du bouton dont
        le numéro est en paramètres.

        Args:
            i (int): Le numéro du bouton à modifier
        """
        if self.boutons_joueur[i]['text'] == "Inactive":
            self.boutons_joueur[i]['text'] = "Player"
        elif self.boutons_joueur[i]['text'] == "Player":
            self.boutons_joueur[i]['text'] = "Bot"
        else:
            self.boutons_joueur[i]['text'] = "Inactive"


class FrameRegles(Frame):
    def __init__(self, master):
        super().__init__(master, borderwidth=1, relief=RIDGE)
        self.texte = []
        self.obtenier_regles()
        self.label_regles = Label(self, background='#d8c0a5',
                                  highlightthickness=2, highlightbackground='#664524')
        for ligne in self.texte:
            current_text = self.label_regles.cget("text")
            new_text = current_text + "\n" + ligne
            self.label_regles.config(text=new_text)
        self.label_regles.grid()

    def obtenier_regles(self):
        with open("regles.txt", "r") as regles:
            for ligne in regles:
                self.texte.append(ligne)


class MenuParametres(Menu):
    def __init__(self, master):
        """
        Constructeur de la classe MenuParametres. Cette classe permet
        de choisir les paramètres de la partie et de démarrer la partie.
        """
        super().__init__(master)
        self.master = master

        self.frame_frame = Frame(self, background='#d8c0a5')
        self.frame_arene = FrameArene(self.frame_frame)
        self.frame_arene.grid(row=0, column=0, padx=10, pady=10)
        self.frame_joueurs = FrameJoueurs(self.frame_frame)
        self.frame_joueurs.grid(row=0, column=1, padx=10, pady=10)

        self.button_frame = Frame(self, background='#d8c0a5')
        self.bouton_remplissage_auto = Button(self.button_frame, text="Default settings",
                                              command=self.remplissage_auto,
                                              background='#d8c0a5', activebackground='#d8c0a5')
        self.bouton_remplissage_auto.grid(row=2, column=0)

        self.frame_regles = FrameRegles(self)
        self.create_window(0 + self.master.width // 6,
                           self.master.height // 1.7,
                           anchor="center",
                           window=self.frame_regles)

        self.back_button = self.create_back_button("Back", self.textures)
        self.back_button.config(command=lambda: self.master.switch_menu_canvas("MainMenu"))
        self.bouton_commencer = self.create_menu_button("Start !", self.commencer)

        self.bg_init()

        self.create_image(self.master.width // 2,
                          self.master.height // 2,
                          image=self.textures.menu_panel,
                          anchor="center")

        self.create_window(self.master.width // 2,
                           self.master.height // 2 + self.master.height // 10,
                           anchor="center",
                           window=self.button_frame)
        self.create_window(self.master.width // 2,
                           self.master.height // 2,
                           anchor="center",
                           window=self.frame_frame)
        self.create_window((self.master.width - self.master.width // 38.4),
                           (self.master.height - self.master.height // 21.6),
                           anchor="se",
                           window=self.back_button)
        self.create_window((self.master.width / 2),
                           (self.master.height - self.master.height // 7),
                           anchor="center",
                           window=self.bouton_commencer)

    def commencer(self):
        """
        Cette méthode crée la fenêtre principale en fonction des paramètres dans les frames.
        """
        try:
            self.master.arene = self.frame_arene.obtenir_arene()
            self.master.joueurs = self.frame_joueurs.obtenir_joueurs(self.master.arene,
                                                                     self.frame_arene.obtenir_nombre_des(),
                                                                     self.master)
            self.destroy()
            self.master.demarrer()
        except ValueError as e:
            messagebox.showerror("Erreur", str(e))

    def obtenir_donnees(self):
        """
        Retourne l'arène et les joueurs.

        Returns:
            Arene: L'arène créée
            list: La liste de joueurs créés
        """
        return self.master.arene, self.master.joueurs

    def remplissage_auto(self):
        try:
            self.obtenir_infos_remplissage()
        except NotImplementedError:
            messagebox.showerror("Erreur", "Le défi Fichier de configuration n'a pas été réalisé encore")
        except FileNotFoundError:
            messagebox.showerror("Erreur", "Aucun fichier de configuration trouvé")
        except KeyError:
            messagebox.showerror("Erreur", "Il manque un des champs obligatoires")
        except ValueError:
            messagebox.showerror("Erreur", "Un des champs n'a pas le bon format \
                                \n\nAssurez-vous d'avoir entre 2 et 5 joueurs")

    def obtenir_infos_remplissage(self):
        with open("./interface/config.txt", "r") as fichier_config:
            for ligne in fichier_config:
                cle, valeur = ligne.rstrip().split(":")
                self.ecrire_selon_cle(cle, valeur)

    def ecrire_selon_cle(self, cle, valeur):
        if cle == 'dimension':
            self.frame_arene.entry_dimension_carre.delete(0, END)
            self.frame_arene.entry_dimension_carre.insert(0, valeur)
        elif cle == 'n_des':
            self.frame_arene.entry_nombre_des.delete(0, END)
            self.frame_arene.entry_nombre_des.insert(0, valeur)
        elif cle == 'joueurs':
            if len(valeur.split(",")) < 2 \
                    or len(valeur.split(",")) > 5:
                raise ValueError
            i = 0
            for joueur in valeur.split(","):
                bouton_joueur = self.frame_joueurs.boutons_joueur[i]
                i += 1
                bouton_joueur.config(text=joueur)
        elif cle == 'dessiner':
            if valeur == 'oui':
                self.frame_arene.mode_var.set(1)
