"""
La classe Dé.

Représente un dé à 6 faces.
"""

from random import randint
import interface.texture_loader as tl


class De:
    """ Représente un dé à 6 faces.

    Attributes:
        valeur (int): Un nombre de 1 à 6 inclusivement.
    """

    def __init__(self):
        """
        Constructeur de la classe De.
        Avant d'être lancé, sa valeur est None.
        """
        self.valeur = None

    def affichage_de(self, mode):
        """
        Donne la représentation en chaîne de caractères de la valeur
        du dé, selon le mode [2,3,4,5,6] ou [⚁,⚂,⚃,⚄,⚅].
        Si sa valeur est 1, on affiche X peu importe le mode.

        Args:
            mode (int): Le mode (1 pour [2,3,4,5,6], 2 pour [⚁,⚂,⚃,⚄,⚅]).

        Returns:
            str: La représentation de la valeur du dé.
        """
        # VOTRE CODE ICI
        if mode == 1:
            pass
        elif mode == 2:
            liste = ["de_1", "de_2", "de_3", "de_4", "de_5", "de_6"]
            return liste[int(self.valeur) - 1]

    def lancer(self):
        """
        Modifie aléatoirement la valeur du dé.
        """
        self.valeur = randint(1, 6)

    def ranger(self):
        """
        Met la valeur du dé à None.
        """
        self.valeur = None
