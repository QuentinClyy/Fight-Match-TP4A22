"""
La classe JoueurOrdinateur

Hérite de Joueur et contient une "intelligence artificielle" extrêmement rudimentaire.
"""

from random import randint, choice
from jeu.joueur import Joueur


class JoueurOrdinateur(Joueur):
    def __init__(self, numero_joueur, des_initiaux, arene):
        super().__init__(numero_joueur, des_initiaux, arene)
        self.arene = arene

    def decision_continuer(self):
        """
        Détermine si le joueur souhaite continuer son tour.
        """
        if len(self.des) <= 3 and len(self.arene.des) <= 2:
            return False
        decision = randint(1, 4)
        if decision in range(3):
            return True
        else:
            return False

    def choisir_coordonnees(self):
        """
        Détermine comment le joueur choisit les coordonnées de son lancer.
        """
        return self.piger_coordonnees()

    def choisir_angle(self, coordonnees):
        """
        Détermine comment le joueur choisit l'angle de son lancer.
        """
        x, y = coordonnees
        if x in range(int(self.arene.dimension // 2 + 1)):
            if y in range(int(self.arene.dimension // 2 + 1)):
                return choice(['S', 'SE', 'E'])
            else:
                return choice(['S', 'SO', 'O'])
        else:
            if y in range(int(self.arene.dimension // 2 + 1)):
                return choice(['N', 'NE', 'E'])
            else:
                return choice(['N', 'NO', 'O'])

    def choisir_puissance(self):
        """
        Détermine comment le joueur choisit la puissance de son lancer.
        """
        return self.piger_puissance()
