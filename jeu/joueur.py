"""
La classe Joueur

Représente un joueur.
Ne peut exister en soi, sert plutôt de classe abstraite pour des types de joueurs concrets.
"""

from random import randint, choice
from jeu.lancer import ANGLES, Lancer


class Joueur:
    def __init__(self, numero_joueur, des_initiaux, arene):
        """
        Constructeur de la classe Joueur.

        Args:
            numero_joueur (int): Le numéro identifiant le joueur
            des_initiaux (list): Les dés en possession du joueur en début de partie
            arene (Arene): l'arène du jeu
        """
        self.numero_joueur = numero_joueur
        self.des = des_initiaux
        self.arene = arene

    def choisir_continuer(self, forcer_continuer, suite_continuer, suite_terminer):
        """
        Détermine si le joueur décide de lancer à nouveau ou de mettre fin à son tour.

        Args:
            forcer_continuer (bool): Si True, on continue nécessairement.
            suite_continuer (fonction): Action à faire si on continue le tour.
            suite_terminer (fonction): Action à faire si on arrête le tour.
        """
        if forcer_continuer or self.decision_continuer():
            suite_continuer()
        else:
            suite_terminer()

    def decision_continuer(self):
        """
        Détermine si le joueur souhaite continuer son tour.
        Doit être implémenté par la classe JoueurOrdinateur.
        """
        raise NotImplementedError("La classe enfant JoueurOrdinateur doit implémenter cette méthode. ")

    def choisir_coordonnees(self):
        """
        Détermine comment le joueur choisit les coordonnées de son lancer.
        Doit être implémenté par les classes enfant de Joueur.
        """
        raise NotImplementedError("Les classes enfant doivent implémenter cette méthode. ")

    def choisir_angle(self):
        """
        Détermine comment le joueur choisit l'angle de son lancer.
        Doit être implémenté par les classes enfant de Joueur.
        """
        raise NotImplementedError("Les classes enfant doivent implémenter cette méthode. ")

    def choisir_puissance(self):
        """
        Détermine comment le joueur choisit la puissance de son lancer.
        Doit être implémenté par les classes enfant de Joueur.
        """
        raise NotImplementedError("Les classes enfant doivent implémenter cette méthode. ")

    def creer_lancer(self, coordonnees, angle, puissance):
        """
        Crée un lancer avec les paramètres donnés en entrée.
        Enlève un dé du joueur (vous pouvez utiliser self.des.pop)
        pour le donner au lancer.

        Args:
            coordonnees ((int, int)): emplacement initial du lancer
            angle (str): point cardinal donnant l'angle du lancer
            puissance (int): puissance du lancer

        Returns:
            Lancer: Le lancer créé
        """
        return Lancer(self.des.pop(), coordonnees, angle, puissance)

    def choisir_lancer(self, suite):
        """
        Crée un lancer (Joueur.creer_lancer) à partir des coordonnées (Joueur.choisir_coordonnees),
        angle (Joueur.choisir_angle) et puissance (Joueur.choisir_puissance) choisis.
        Déclenche la suite.

        Args:
            suite (fonction): La fonction à exécuter pour la suite du programme.
                Prend en argument le lancer créé et le joueur.
        """
        coordonnees = self.choisir_coordonnees()
        angle = self.choisir_angle()
        puissance = self.choisir_puissance()
        lancer = self.creer_lancer(coordonnees, angle, puissance)
        suite(lancer, self)

    def est_elimine(self):
        """
        Vérifie si le joueur est éliminé, i.e. s'il n'a plus de dés

        Returns:
            bool: True si le joueur est éliminé, False sinon.
        """
        return len(self.des) == 0

    def rendre_de(self, de):
        """
        Ajoute le dé en argument aux dés du joueur (utilisez self.des.append),
        après l'avoir rangé (De.ranger)

        Args:
            de (De): Le dé à ajouter
        """
        de.ranger()
        self.des.append(de)

    def table_rase(self):
        """
        Crée une liste avec autant de lancers (Joueur.creer_lancer) que le joueur a de dés.
        Les lancers doivent avoir des paramètres aléatoires (Joueur.piger_coordonnees,
        Joueur.piger_angle, Joueur.piger_puissance)

        Returns:
            liste: La liste des lancers
        """
        liste_lancers = []
        for i in range(len(self.des)):
            lancer = self.creer_lancer(self.piger_coordonnees(),
                                       self.piger_angle(),
                                       self.piger_puissance())
            liste_lancers.append(lancer)
        return liste_lancers

    def piger_coordonnees(self):
        """
        Donne des coordonnées au hasard dans l'arène.

        Returns:
            (int, int): Le centre de l'arène
        """
        return randint(0, self.arene.dimension - 1), \
               randint(0, self.arene.dimension - 1)

    def piger_angle(self):
        """
        L'angle est pigé aléatoirement parmi les 8 points cardinaux

        Returns:
            str: Le point cardinal pigé
        """
        return choice(list(ANGLES.keys()))

    def piger_puissance(self):
        """
        La puissance est pigée aléatoirement entre 1 et le quart de la dimension de l'arène.

        Returns:
            int: La puissance pigée
        """
        return randint(1, max(1, self.arene.dimension // 4))

    def __str__(self):
        """
        Donne la représentation en chaîne de caractères du joueur.

        Returns:
            str: la représentation en chaîne de caractères
        """
        return f"joueur {self.numero_joueur} ({len(self.des)} dés)"
