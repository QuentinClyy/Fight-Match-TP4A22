"""
La classe GlaDÉateur

Représente une partie du jeu.

Attention: cette classe a été retravaillée pour être utilisable avec une
interface graphique. Elle s'appuie donc grandement sur le principe des callbacks.
Ainsi, il est déconseillé de modifier cette classe car cela pourrait facilement
briser le fonctionnement du jeu.
"""


class Gladeateur:
    """ Représente une partie du jeu.

    Attributes:
        liste_joueurs (list): La liste des joueurs.
        arene (Arene): L'arène du jeu.
        gestionnaire_io (GestionnaireIO): L'instance gérant les entrées/sorties
        joueur_index (int): L'index du joueur actif.
        premier_lancer (bool): False si le joueur actif a fait son premier lancé de dé, False sinon.
    """

    def __init__(self, liste_joueurs, arene, gestionnaire_io):
        """
        Constructeur de la classe Gladeateur.
        Reçoit en paramètre le gestionnaire_io, une classe qui permet au Gladeateur
        de déléguer toutes les interactions avec l'interface afin qu'on puisse se
        concentrer sur la logique du jeu ici et non comment c'est affiché.

        Args:
            liste_joueurs (list): La liste des joueurs
            arene (Arene): L'arène du jeu
            gestionnaire_io (GestionnaireIO): L'instance gérant les entrées/sorties
        """
        self.liste_joueurs = liste_joueurs
        self.arene = arene
        self.gestionnaire_io = gestionnaire_io
        self.joueur_index = 0
        self.premier_lancer = True

    def jouer_partie(self):
        """
        Point d'entrée de la boucle de jeu. On commence par une sélection d'action.
        """
        self.selection_action()

    def selection_action(self):
        """
        Fonction qui définit quelle action doit être jouée.
        Voir les commentaires dans le code.
        """

        # Si le jeu est terminé, on affiche le joueur victorieux et on arrête
        vainqueur = self.calculer_victoire()
        if self.calculer_victoire() is not None:
            self.gestionnaire_io.afficher_victoire(vainqueur)
        else:
            # Sinon, on détermine l'action à faire pour le joueur en cours
            joueur = self.joueur_en_cours()
            if self.arene.est_vide():
                if self.premier_lancer:
                    # Si le joueur commence son tour sur une arène vide, c'est une table rase!
                    self.afficher_arene(joueur, lambda: self.table_rase_a(joueur))
                else:
                    # Si le joueur vient d'éliminer les derniers dés dans l'arène,
                    # il passe au prochain qui subira une table rase.
                    self.fin_du_tour_a()
            else:
                # Si le joueur a déjà joué, il doit choisir de continuer (afficher arène puis
                # effectuer un tour) ou pas (fin du tour)
                joueur.choisir_continuer(self.premier_lancer,
                                         lambda: self.afficher_arene(joueur,
                                                                     lambda: self.effectuer_tour(joueur)),
                                         self.fin_du_tour_a)

    def effectuer_tour(self, joueur):
        """
        Demande au joueur de choisir son lancer et l'effectue, puis range les dés.
        Met plutôt fin au tour si le joueur est éliminé.

        Args:
            joueur (Joueur): Le joueur dont c'est le tour
        """
        if not joueur.est_elimine():
            self.premier_lancer = False
            joueur.choisir_lancer(self.tour_normal_a)
        else:
            self.fin_du_tour_a()

    def tour_normal_a(self, lancer, joueur):
        """
        Affiche le lancer, puis poursuit le tour.

        Args:
            lancer (Lancer): le lancer à afficher
            joueur (Joueur): le joueur dont c'est le tour
        """
        self.gestionnaire_io.afficher_lancer(lancer,
                                             lambda: self.tour_normal_b(lancer, joueur))

    def tour_normal_b(self, lancer, joueur):
        """
        Exécute le lancer sur l'arène

        Args:
            lancer (Lancer): le lancer à effectuer
            joueur (Joueur): le joueur dont c'est le tour
        """
        self.arene.effectuer_lancer(lancer)
        self.afficher_arene(None, lambda: self.tour_normal_c(joueur))

    def tour_normal_c(self, joueur):
        """
        Effectue le rangement, affiche l'arène, puis redémarre la boucle de jeu
        avec une nouvelle sélection d'action.

        Args:
            joueur (Joueur): le joueur dont c'est le tour
        """
        correspondance = self.arene.rangement(joueur)
        if correspondance:
            prochaine_action = self.fin_du_tour_a
        else:
            prochaine_action = self.selection_action
        self.afficher_arene(joueur, prochaine_action)

    def fin_du_tour_a(self):
        """
        Affiche la fin du tour, puis poursuit le processus de fin du tour
        """
        self.gestionnaire_io.afficher_fin_tour(self.fin_du_tour_b)

    def fin_du_tour_b(self):
        """
        Change de joueur, tout en assurant que celui-ci sera à son premier lancer.
        """
        self.premier_lancer = True
        self.changer_joueur()
        self.selection_action()

    def table_rase_a(self, joueur):
        """
        Affiche et déclenche une table rase pour le joueur.

        Args:
            joueur (Joueur): Le joueur qui subit la table rase.
        """
        self.gestionnaire_io.afficher_table_rase(lambda: self.table_rase_b(joueur))

    def table_rase_b(self, joueur):
        """
        Obtient les lancers de table rase du joueur et les affiche, puis poursuit
        le processus de table rase.

        Args:
            joueur (Joueur): Le joueur qui subit la table rase.
        """
        lancers = joueur.table_rase()
        self.gestionnaire_io.afficher_plusieurs_lancers(lancers,
                                                        lambda: self.table_rase_c(joueur, lancers))

    def table_rase_c(self, joueur, lancers):
        """
        Effectue les lancers dans l'arène, fait le rangement des dés,
        puis change le joueur et recommence la boucle de jeu.

        Args:
            joueur (Joueur): le joueur qui subit la table rase
            lancers (list): La liste des lancers à effectuer.

        Returns:

        """
        self.arene.effectuer_plusieurs_lancers(lancers)
        self.arene.rangement(joueur)
        self.changer_joueur()
        self.selection_action()

    def afficher_arene(self, joueur, suite):
        """
        Affiche l'arène.

        Args:
            joueur (Joueur): le joueur dont c'est le tour
            suite (fonction): la suite du programme à exécuter
        """
        self.gestionnaire_io.afficher_jeu(self.arene,
                                          lambda: self.afficher_apres_arene(joueur, suite))

    def afficher_apres_arene(self, joueur, suite):
        """
        Affiche un message après l'affichage de l'arène.
        Soit le début du tour d'un joueur, ou le rangement des dés.
        Args:
            joueur (Joueur): le joueur dont c'est le tour (None si c'est un rangement de dés)
            suite (fonction): la suite du programme à exécuter
        """
        if joueur is None:
            self.gestionnaire_io.afficher_rangement(suite)
        else:
            self.gestionnaire_io.afficher_tour(joueur, suite)

    def joueur_en_cours(self):
        """
        Donne le joueur pointé par l'index de joueur.
        Gladeateur.liste_joueurs est la liste des joueurs, dont l'ordre ne change
        jamais, et Gladeateur.joueur_index représente l'index dans cette liste du joueur en cours.

        Returns:
            Joueur: Le joueur dont c'est le tour.
        """
        return self.liste_joueurs[self.joueur_index]

    def changer_joueur(self):
        """
        Cette fonction augmente l'index du joueur (Gladeateur.joueur_index).
         - L'index doit en temps normal augmenter de 1
         - Si l'index est trop grand, il doit redémarrer à 0 (utilisez un modulo!)
         - L'index doit augmenter de plus que 1 lorsqu'il y a des joueurs éliminés
         à sauter (Joueur.est_elimine)
        """
        self.joueur_index = (self.joueur_index + 1) % len(self.liste_joueurs)
        while self.joueur_en_cours().est_elimine():
            self.joueur_index = (self.joueur_index + 1) % len(self.liste_joueurs)

    def calculer_victoire(self):
        """
        Cette fonction vérifie s'il y a une victoire, i.e. tous les joueurs sauf
        un sont éliminés (Joueur.est_elimine).
        Elle retourne le joueur vainqueur ou None s'il n'y a pas de victoire.

        Returns:
            Joueur: Le joueur vainqueur (ou None en l'absence de victoire)
        """
        n_joueurs_en_vie, joueur_vainqueur = 0, None
        for joueur in self.liste_joueurs:
            if not joueur.est_elimine():
                joueur_vainqueur = joueur
                n_joueurs_en_vie += 1
        if n_joueurs_en_vie > 1:
            return None
        else:
            return joueur_vainqueur
