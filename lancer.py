"""
La classe Lancer

Représente un lancer de dé.
"""

from random import randint

# Le dictionnaire associant les points cardinaux à leur direction.
# À importer lorsqu'on veut connaître les points cardinaux possibles.
ANGLES = {
    'NO': (-1, -1),
    'N': (-1, 0),
    'NE': (-1, 1),
    'E': (0, 1),
    'SE': (1, 1),
    'S': (1, 0),
    'SO': (1, -1),
    'O': (0, -1)
}


class Lancer:
    """ Représente un lancer de dé.

    Attributes:
            de (De): le dé lancé
        trajectoire (list): La trajectoire du dé, sous forme de liste de coordonnées.
    """

    def __init__(self, de, emplacement_depart, angle, puissance):
        """
        Constructeur de la classe Lancer.
        Un lancer démarre à un emplacement initial dans l'arène et roule dans
        l'arène suivant un angle et une puissance, lesquels sont sujets à des déviations
        aléatoires.

        Args:
            de (De): le dé lancé
            emplacement_depart ((int, int)): Les coordonnées de l'emplacement où le dé atterit d'abord
            angle (str): Le point cardinal vers lequel le dé roule
            puissance (int): Le nombre de case approximatif que le dé parcourt
        """
        self.de = de
        self.trajectoire = self.obtenir_trajectoire(emplacement_depart, angle, puissance)

    def obtenir_trajectoire(self, emplacement_depart, angle, puissance):
        """
        Calcule la trajectoire du dé, selon l'emplacement initial, l'angle (des déviations
        peuvent survenir) et la puissance.

        Returns:
            list: La trajectoire, sous forme de liste de coordonnées.
                Le premier tuple de coordonnées est l'emplacement initial
                et le dernier est l'emplacement où le dé s'arrête.
        """
        emplacement = emplacement_depart
        trajectoire = [emplacement]
        for i in range(puissance):
            direction = self.obtenir_direction(angle)
            emplacement = emplacement[0] + direction[0], emplacement[1] + direction[1]
            trajectoire.append(emplacement)
        return trajectoire

    def obtenir_direction(self, angle):
        """
        À partir d'un point cardinal, retourne la différence entre l'emplacement précédent et
        le prochain.

        Args:
            angle (str): Le point cardinal

        Returns:
            (int, int): Le déplacement en x et en y

        """
        direction_base = ANGLES[angle]
        return self.deviation(direction_base)

    def deviation(self, dir_base):
        """
        À chaque déplacement du dé dans l'arène, il y a une chance sur 16
        que celui-ci se mette à aller plus vers sa gauche, une chance sur 16
        qu'il aille plus vers la droite, et 7 chances sur 8 qu'il ne dévie pas.

        Args:
            dir_base ((int, int)): La direction de base, avant déviation

        Returns:
            (int, int): La direction, une fois (possiblement) déviée
        """
        devier = randint(0, 15)
        if devier == 0:  # rotation sens horaire
            rotation = ((1, 1), (-1, 1))
        elif devier == 1:  # rotation sens anti-horaire
            rotation = ((1, -1), (1, 1))
        else:  # pas de déviation
            rotation = ((1, 0), (0, 1))

        dir_x = self.signe(rotation[0][0] * dir_base[0] + rotation[0][1] * dir_base[1])
        dir_y = self.signe(rotation[1][0] * dir_base[0] + rotation[1][1] * dir_base[1])
        return dir_x, dir_y

    def signe(self, x):
        """
        Fonction utilitaire retournant -1 pour un nombre négatif, 0 pour 0 et +1 pour un
        nombre positif.

        Args:
            x (int):

        Returns:
            int: +1 si l'entrée est positive, 0 si elle est 0, et -1 si elle est négative.
        """
        if x == 0:
            return 0
        return 2 * int(x > 0) - 1

    def __str__(self):
        """
        Pour afficher les emplacements de la trajectoire.

        Returns:
            str: Les coordonnées sous forme de longue chaîne de caractères.
        """
        s = str(self.trajectoire[0])
        for coordonnee in self.trajectoire[1:]:
            s += ' -> ' + str(coordonnee)
        return s
