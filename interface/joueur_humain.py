"""
Ce module comporte la classe JoueurHumainTk. Il s'agit d'une version du joueur
humain qui réagit aux clics dans l'interface (par opposition à entrer des informations en console
au TP3).
"""
from jeu.joueur import Joueur


class JoueurHumain(Joueur):
    def __init__(self, numero_joueur, des_initiaux, arene, fenetre_jeu):
        """
        Constructeur de la classe JoueurHumainConsole.

        Args:
            numero_joueur (int): Le numéro identifiant le joueur
            des_initiaux (list): Les dés en possession du joueur en début de partie
            arene (Arene): l'arène du jeu
            fenetre_jeu (FenetrePrincipale): La fenêtre de jeu.
        """
        super().__init__(numero_joueur, des_initiaux, arene)
        self.fenetre_jeu = fenetre_jeu

    def choisir_lancer(self, suite_lancer):
        """
        Permet de cliquer sur toutes les cases pour sélectionner les coordonnées
        de départ.

        Args:
            suite_lancer (fonction): Suite du programme après le choix du lancer en entier
        """
        self.fenetre_jeu.canvas_arene.permettre_clics(
            lambda coordonnees: True,
            lambda coordonnees: self.choisir_coordonnees_fin(coordonnees, suite_lancer)
        )

    def choisir_coordonnees_fin(self, coordonnees_debut, suite_lancer):
        """
        Permet de cliquer sur les cases alignées avec les coordonnées déjà sélectionnées

        Args:
            coordonnees_debut ((int, int)): Les coordonnées où le dé atterit
            suite_lancer (fonction): Suite du programme après le choix du lancer en entier
        """
        x1, y1 = coordonnees_debut

        def coordonnees_cliquables(coordonnees_fin):
            """
            Fonction locale utilitaire qui retourne vrai pour les emplacements
            alignées avec l'emplacement du début

            Args:
                coordonnees_fin ((int, int)): Les coordonnées à vérifier

            Returns:
                bool: True si aligné, False sinon
            """
            x2, y2 = coordonnees_fin
            return not (x2 == x1 and y2 == y1) and \
                   (x2 == x1 or y2 == y1 or y2 - y1 == x2 - x1 or y2 - x1 == y1 - x2)

        self.fenetre_jeu.canvas_arene.permettre_clics(
            coordonnees_cliquables,
            lambda coordonnees: self.calculer_lancer(coordonnees_debut, coordonnees, suite_lancer)
        )

    def calculer_lancer(self, coordonnees_debut, coordonnees_fin, suite_lancer):
        """
        Crée un lancer à partir de l'angle et la puissance déduits, puis exécute la
        suite avec ce lancer.

        Args:
            coordonnees_debut ((int, int)): coordonnées du début
            coordonnees_fin ((int, int)): coordonnées visées
            suite_lancer (fonction): Suite du programme après le choix du lancer en entier
        """
        angle, puissance = self.calculer_angle_puissance(coordonnees_debut, coordonnees_fin)
        lancer = self.creer_lancer(coordonnees_debut, angle, puissance)
        suite_lancer(lancer, self)

    def calculer_angle_puissance(self, coordonnees_debut, coordonnees_fin):
        """
        Déduit l'angle et la puissance en fonction des coordonnées de début et celles visées

        Args:
            coordonnees_debut ((int, int)): coordonnées du début
            coordonnees_fin ((int, int)): coordonnées visées

        Returns:
            str, int: L'angle et la puissance
        """
        x2, y2 = coordonnees_fin
        x1, y1 = coordonnees_debut
        if x2 == x1 and y2 == y1:
            raise ValueError
        elif x2 == x1:
            if y2 > y1:
                return "E", y2 - y1
            else:
                return "O", y1 - y2
        elif y2 == y1:
            if x2 > x1:
                return "S", x2 - x1
            else:
                return "N", x1 - x2
        elif y2 - y1 == x2 - x1:
            if y2 > y1:
                return "SE", y2 - y1
            else:
                return "NO", y1 - y2
        elif y2 - x1 == y1 - x2:
            if y2 > y1:
                return "NE", y2 - y1
            else:
                return "SO", y1 - y2
        else:
            raise ValueError

    def choisir_continuer(self, forcer_continuer, suite_continuer, suite_terminer):
        """
        Permet d'appuyer sur le bouton de fin du tour.
        On écrase la méthode choisir_continuer de Joueur car ce n'est pas du tout
        la même chose pour un joueur humain qu'un joueur ordinateur.

        Args:
            forcer_continuer (bool): Si True, on n'active pas le bouton.
            suite_continuer (fonction): Action à faire si on ne clique pas sur le bouton
            suite_terminer (fonction): Action à faire si on clique sur le bouton
        """
        if not forcer_continuer:
            self.fenetre_jeu.frame_joueur.activer_bouton(suite_terminer)
        suite_continuer()
