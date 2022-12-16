"""
La classe GestionnaireIOInterface

Le GestionnaireIO centralise les entrées-sorties (input(I) / output (O)) du programme.
Ainsi, les classes du jeu peuvent simplement exprimer par exemple qu'il faut afficher quelque chose,
sans avoir à se soucier de comment ce sera affiché.
"""


class GestionnaireIOInterface:
    def __init__(self, fenetre_principale, canvas_arene, frame_description):
        """
        Constructeur de la classe GestionnaireIOInterface

        Args:
            fenetre_principale (FenetrePrincipale): la fenêtre de jeu
            canvas_arene (CanvasArene): le canvas représentant l'arène
            frame_description (FrameDescription): le frame décrivant les événements
        """
        self.fenetre_principale = fenetre_principale
        self.canvas_arene = canvas_arene
        self.frame_description = frame_description

    def temps_attente(self):
        """
        Retourne le temps entre deux actions.

        Returns:
            int: Le temps entre deux actions, en millisecondes.

        """
        return 250

    def afficher_jeu(self, arene, suite):
        """
        Affiche l'arène

        Args:
            arene (Arene): L'arène à afficher
            suite (fonction): La fonction à exécuter suite à l'affichage
        """
        self.canvas_arene.dessiner_canvas(suite)

    def afficher_table_rase(self, suite):
        """
        Affiche la présence d'une table rase

        Args:
            suite (fonction): La fonction à exécuter suite à l'affichage
        """
        self.frame_description.populer("Table rase! ", self.temps_attente(), suite)

    def afficher_fin_tour(self, suite):
        """
        Affiche la fin du tour

        Args:
            suite (fonction): La fonction à exécuter suite à l'affichage
        """
        self.fenetre_principale.frame_joueur.bouton_terminer_tour["state"] = "disabled"
        self.frame_description.populer("Fin du tour. ", self.temps_attente(), suite)

    def afficher_rangement(self, suite):
        """
        Affiche le rangement des dés

        Args:
            suite (fonction): La fonction à exécuter suite à l'affichage
        """
        self.frame_description.populer("Rangement des dés...", self.temps_attente(), suite)

    def afficher_tour(self, joueur, suite):
        """
        Affiche le tour du joueur

        Args:
            joueur (Joueur): Le joueur dont c'est le tour
            suite (fonction): La fonction à exécuter suite à l'affichage
        """
        self.fenetre_principale.afficher_joueur(joueur, self.temps_attente(), suite)

    def afficher_lancer(self, lancer, suite):
        """
        Affiche un lancer sur le canvas

        Args:
            lancer (Lancer): Le lancer à afficher
            suite (fonction): La fonction à exécuter suite à l'affichage
        """
        self.canvas_arene.afficher_lancer(lancer, self.temps_attente(), suite)

    def afficher_plusieurs_lancers(self, lancers, suite):
        """
        Affiche récursivement plusieurs lancers sur le canvas

        Args:
            lancers (list): Les lancers restants à afficher
            suite (fonction): La fonction à exécuter suite à l'affichage
        """
        if len(lancers) == 0:
            suite()
        else:
            self.afficher_lancer(lancers[0],
                                 lambda: self.afficher_plusieurs_lancers(lancers[1:], suite))

    def afficher_victoire(self, joueur):
        """
        Affiche la victoire du joueur
        Args:
            joueur (Joueur): Le joueur ayant remporté la partie
        """
        self.fenetre_principale.afficher_gagnant(joueur)
