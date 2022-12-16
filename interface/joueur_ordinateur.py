"""
La classe JoueurOrdinateur

Hérite de Joueur et contient une "intelligence artificielle" extrêmement rudimentaire.
"""

from random import randint
from jeu.joueur import Joueur


class JoueurOrdinateur(Joueur):
    def __init__(self, numero_joueur, des_initiaux, arene):
        super().__init__(numero_joueur, des_initiaux, arene)

    def decision_continuer(self):
        """
        Détermine si le joueur souhaite continuer son tour.
        """
        decision = randint(1, 4)
        if decision in range(3):
            return True
        else:
            return False

    def choisir_coordonnees(self):
        """
        Détermine comment le joueur choisit les coordonnées de son lancer.
        Doit être implémenté par les classes enfant de Joueur.
        """
        return self.piger_coordonnees()

    def choisir_angle(self):
        """
        Détermine comment le joueur choisit l'angle de son lancer.
        Doit être implémenté par les classes enfant de Joueur.
        """
        return self.piger_angle()

    def choisir_puissance(self):
        """
        Détermine comment le joueur choisit la puissance de son lancer.
        Doit être implémenté par les classes enfant de Joueur.
        """
        return self.piger_puissance()
