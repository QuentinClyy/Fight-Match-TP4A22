"""
La classe GlaDÉateur

Représente une partie du jeu.

Il est déconseillé de modifier cette classe car cela pourrait facilement
briser le fonctionnement du jeu (à l'exception des méthodes qui vous sont demandées!).
"""


class Gladeateur:
    """ Représente une partie du jeu.

    Attributes:
        liste_joueurs (list): La liste des joueurs.
        arene (Arene): L'arène du jeu.
        joueur_index (int): L'index du joueur actif.
        premier_lancer (bool): False si le joueur actif a fait son premier lancé de dé, False sinon.
    """
    def __init__(self, liste_joueurs, arene):
        """
        Constructeur de la classe Gladeateur.

        Args:
            liste_joueurs (list): La liste des joueurs
            arene (Arene): L'arène du jeu
        """
        self.liste_joueurs = liste_joueurs
        self.arene = arene
        self.joueur_index = 0
        self.premier_lancer = True

    def jouer_partie(self):
        """
        Point d'entrée de la boucle de jeu. On commence par une sélection d'action.

        Voir les commentaires dans le code.
        """
        vainqueur = None

        while vainqueur is None:
            # On détermine l'action à faire pour le joueur en cours
            joueur = self.joueur_en_cours()
            tour_termine = False

            if self.arene.est_vide():
                tour_termine = True
                if self.premier_lancer:
                    # Si le joueur commence son tour sur une arène vide, c'est une table rase!
                    self.afficher_arene(joueur)
                    self.table_rase(joueur)
            elif not self.premier_lancer:
                # Si le joueur a déjà joué, il doit choisir de continuer (afficher arène puis
                # effectuer un tour) ou pas (fin du tour)
                tour_termine = not joueur.choisir_continuer()

            if not tour_termine:
                self.afficher_arene(joueur)
                tour_termine = self.effectuer_tour(joueur)

            if tour_termine:
                self.fin_du_tour(joueur)

            vainqueur = self.calculer_victoire()

        # Si le jeu est terminé, on affiche le joueur victorieux et on arrête
        print("*" * 50)
        print(f"Victoire du {str(vainqueur)}")
        print("*" * 50)

    def effectuer_tour(self, joueur):
        """
        Demande au joueur de choisir son lancer et l'effectue, puis range les dés.
        Met plutôt fin au tour si le joueur est éliminé.

        Args:
            joueur (Joueur): Le joueur dont c'est le tour

        Returns:
            bool: True si le tour est terminé, False sinon
        """
        if not joueur.est_elimine():
            self.premier_lancer = False
            lancer = joueur.choisir_lancer()
            tour_termine = self.tour_normal(lancer, joueur)
        else:
            tour_termine = True
        return tour_termine

    def tour_normal(self, lancer, joueur):
        """
        Affiche le lancer, puis effectue le rangement.
        S'il y a correspondance lors de celui-ci, met fin au tour,
        sinon recommence à la sélection d'action.

        Args:
            lancer (Lancer): le lancer à afficher
            joueur (Joueur): le joueur dont c'est le tour

        Returns:
            bool: True si le tour est terminé, False sinon
        """
        print("Trajectoire : ", str(lancer))
        self.arene.effectuer_lancer(lancer)
        self.afficher_arene(None, lancer)
        tour_termine = self.arene.rangement(joueur)
        self.afficher_arene(joueur, None)
        return tour_termine

    def fin_du_tour(self, joueur):
        """
        Affiche la fin du tour, puis change de joueur,
        tout en assurant que celui-ci sera à son premier lancer.

        Args:
            joueur (Joueur): Le joueur dont le tour se termine.
        """
        print(f"Fin du tour du {str(joueur)}.")
        self.premier_lancer = True
        self.changer_joueur()

    def table_rase(self, joueur):
        """
        Affiche et déclenche une table rase pour le joueur.

        Args:
            joueur (Joueur): Le joueur qui subit la table rase.
        """
        print("Table rase! ")
        lancers = joueur.table_rase()
        trajectoires = []
        for lancer in lancers:
            print("Trajectoire : ", str(lancer))
            trajectoires = trajectoires + lancer.trajectoire

        self.arene.effectuer_plusieurs_lancers(lancers)
        print(self.arene.affichage_string(trajectoires))
        self.arene.rangement(joueur)

    def afficher_arene(self, joueur, lancer=None):
        """
        Affiche l'arène, puis soit le début du tour d'un joueur,
        ou le rangement des dés.

        Args:
            joueur (Joueur): le joueur dont c'est le tour (None si c'est un rangement de dés)
            lancer (Lancer): le lancer venant d'être produit, s'il y a lieu.
        """
        print(self.arene.affichage_string(lancer))
        if joueur is None:
            print("Rangement des dés...")
        else:
            print(f"Au tour du {str(joueur)}.")

    def joueur_en_cours(self):
        """
        Donne le joueur pointé par l'index de joueur.
        Gladeateur.liste_joueurs est la liste des joueurs, dont l'ordre ne change
        jamais, et Gladeateur.joueur_index représente l'index dans cette liste du joueur en cours.

        Returns:
            Joueur: Le joueur dont c'est le tour.
        """
        # VOTRE CODE ICI
        return self.liste_joueurs[self.joueur_index]

    def changer_joueur(self):
        """
        Cette fonction augmente l'index du joueur (Gladeateur.joueur_index).
         - L'index doit en temps normal augmenter de 1
         - Si l'index est trop grand, il doit redémarrer à 0 (utilisez un modulo!)
         - L'index doit augmenter de plus que 1 lorsqu'il y a des joueurs éliminés
         à sauter (Joueur.est_elimine)
        """
        # VOTRE CODE ICI
        self.joueur_index += 1
        if self.joueur_index % len(self.liste_joueurs) == 0:
            self.joueur_index = 0
        while self.joueur_en_cours().est_elimine():
            self.joueur_index += 1

    def calculer_victoire(self):
        """
        Cette fonction vérifie s'il y a une victoire, i.e. tous les joueurs sauf
        un sont éliminés (Joueur.est_elimine).
        Elle retourne le joueur vainqueur ou None s'il n'y a pas de victoire.

        Returns:
            Joueur: Le joueur vainqueur (ou None en l'absence de victoire)
        """
        # VOTRE CODE ICI
        liste_victoire = []
        for joueur in self.liste_joueurs:
            if not joueur.est_elimine():
                liste_victoire.append(joueur)
        if len(liste_victoire) == 1:
            return liste_victoire[0]
