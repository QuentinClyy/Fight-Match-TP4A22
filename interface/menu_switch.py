from tkinter import Tk, messagebox, IntVar
from interface.menu_parametres import MainMenu


class Switch(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1600x900")
        self.attributes('-fullscreen', True)
        self.update()

        self.arene = None
        self.joueurs = None

        self.arene_size = None
        self.boutons_joueur = []
        self.nombre_des = None
        self.mode_var = IntVar(value=0)

        self.width = self.winfo_width()
        self.height = self.winfo_height()
        self.canvas = None
        self.switch_menu_canvas(MainMenu)

    def switch_menu_canvas(self, canvas_class):
        new_canvas = canvas_class(self)
        if self.canvas is not None:
            self.canvas.destroy()
        self.canvas = new_canvas
        self.canvas.pack(fill="both", expand=True)

    def commencer(self):
        """
        Cette méthode crée la fenêtre principale en fonction des paramètres dans les frames.
        """
        try:
            self.arene = self.obtenir_arene()
            self.joueurs = self.obtenir_joueurs(self.arene, self.obtenir_nombre_des(),
                                                self.master)
            self.grab_release()
            self.master.focus_set()
            self.destroy()

        except ValueError as e:
            messagebox.showerror("Erreur", str(e))

    def obtenir_donnees(self):
        """
        Retourne l'arène et les joueurs.

        Returns:
            Arene: L'arène créée
            list: La liste de joueurs créés
        """
        return self.arene, self.joueurs

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
            messagebox.showerror("Erreur", "Un des champs n'a pas le bon format")

    def obtenir_infos_remplissage(self):
        with open("./interface/config.txt", "r") as fichier_config:
            for ligne in fichier_config:
                cle, valeur = ligne.rstrip().split(":")
                self.ecrire_selon_cle(cle, valeur)

    def ecrire_selon_cle(self, cle, valeur):
        if cle == 'dimension':
            self.arene_size = int(valeur)
        elif cle == 'n_des':
            self.nombre_des = int(valeur)
        elif cle == 'joueurs':
            if len(valeur.split(",")) < 2:
                raise ValueError("Trop peu de joueurs!")
            i = 0
            for joueur in valeur.split(","):
                bouton_joueur = self.boutons_joueur[i]
                i += 1
                bouton_joueur.config(text=joueur)
        elif cle == 'dessiner':
            if valeur == 'oui':
                self.mode_var.set(1)
