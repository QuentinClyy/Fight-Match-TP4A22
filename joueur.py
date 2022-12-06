"""
La classe Joueur

Représente un joueur.
"""

from random import randint, choice
from lancer import ANGLES, Lancer


class Joueur:
    """ Représente un joueur.

    Attributes:
        numero_joueur (int): L'index du joueur.
        des (list): Les dés possédés par le joueur.
        arene (Arene): Référence vers l'arène du jeu.
    """

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
        # VOTRE CODE ICI
        de_lancer = self.des.pop()
        return Lancer(de_lancer, coordonnees, angle, puissance)

    def choisir_lancer(self):
        """
        Crée un lancer (Joueur.creer_lancer) à partir des coordonnées (Joueur.choisir_coordonnees),
        angle (Joueur.choisir_angle) et puissance (Joueur.choisir_puissance) choisis.

        Returns:
            Lancer: Le lancer créé
        """
        coordonnees = self.choisir_coordonnees()
        angle = self.choisir_angle()
        puissance = self.choisir_puissance()
        return self.creer_lancer(coordonnees, angle, puissance)

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

    def traitement_continuer(self, entree):
        """
        Transforme "L" (ou "l") en True et "T" (ou "t") en False.
        Pour toute autre entrée, retourne None.

        Args:
            entree (str): l'entrée à traiter

        Returns:
            bool: True si l'entrée est L, False si T (None si invalide)
        """
        # VOTRE CODE ICI
        if entree in ['L', 'l']:
            return True
        elif entree in ['T', 't']:
            return False
        else:
            return None

    def traitement_coordonnees(self, entree):
        """
        Transforme une chaîne au format x,y (où x et y sont des chiffres)
        en tuple de deux entiers (x, y).
        Retourne None si:
         - Il n'y a pas exactement une virgule
         - x et y ne sont pas uniquement des chiffres
         - Les entiers représentés par x et y donnent des coordonnées hors
         de l'arène (Arene.dans_arene)

        Indice: utilisez entree.split(',') pour séparer x et y
        Utilisez la fonction int pour obtenir des entiers, si les strings
        sont numériques (chaine.isnumeric).

        Args:
            entree (str): l'entrée à traiter

        Returns:
            tuple: Coordonnées traitées (None si invalide)
        """
        # VOTRE CODE ICI
        emplacement = ()
        nombre_fois_virgule = entree.count(',')
        if nombre_fois_virgule == 1 and len(entree) == 3:
            for i in entree.split(','):
                if i.isnumeric():
                    emplacement += (int(i),)
            if self.arene.dans_arene(emplacement):
                return emplacement
        else:
            return None

    def traitement_angle(self, entree):
        """
        Vérifie que l'entrée est un des 8 points cardinaux (ANGLES.keys), puis
        le retourne, tout en majuscule.
        Pour toute autre entrée, retourne None
        Exemple:
        se -> SE
        O -> O
        sud-est -> None

        Args:
            entree: L'entrée à valider

        Returns:
            str: Le point cardinal, en majuscule (None si invalide)
        """
        # VOTRE CODE ICI
        if entree.upper() in ANGLES.keys():
            return entree.upper()
        else:
            return None

    def traitement_puissance(self, entree):
        """
        Vérifie que l'entrée représente un entier entre 1 et la dimension de l'arène (Arene.dimension)
        inclusivement, et retourne l'entier.
        Retourne None si:
         - L'entrée ne représente pas un entier
         - L'entier n'est pas inclus dans l'intervalle

        Args:
            entree: L'entrée à valider

        Returns:
            int: L'entier représenté par l'entrée (None si invalide)
        """
        # VOTRE CODE ICI
        if entree.isnumeric() and int(entree) in range(1, self.arene.dimension):
            return int(entree)
        else:
            return None

    def choisir_continuer(self):
        """
        Permet de choisir, en console, si on continue ou termine le tour.
        En cas d'entrée invalide la question est posée à nouveau.

        Returns:
            bool: True si on continue, False si on termine.
        """
        return self.choix_avec_validation(
            "Désirez-vous lancer à nouveau (L) ou terminer votre tour (T) ? ",
            self.traitement_continuer
        )

    def choisir_coordonnees(self):
        """
        Permet de choisir, en console, les coordonnées.
        En cas d'entrée invalide la question est posée à nouveau.

        Returns:
            tuple: Les coordonnées choisies

        """
        return self.choix_avec_validation(
            "Veuillez choisir des coordonnées au format x,y : ",
            self.traitement_coordonnees
        )

    def choisir_angle(self):
        """
        Permet de choisir, en console, l'angle.
        En cas d'entrée invalide la question est posée à nouveau.

        Returns:
            str: L'angle choisi

        """
        return self.choix_avec_validation(
            "Veuillez choisir un angle parmi {} : ".format(', '.join(ANGLES.keys())),
            self.traitement_angle
        )

    def choisir_puissance(self):
        """
        Permet de choisir, en console, la puissance.
        En cas d'entrée invalide la question est posée à nouveau.

        Returns:
            int: la puissance

        """
        return self.choix_avec_validation(
            "Veuillez entrer une puissance entre 1 et {} : ".format(self.arene.dimension - 1),
            self.traitement_puissance
        )

    def choix_avec_validation(self, question, traitement_entree):
        """
        Fonction utilitaire qui pose une question à l'utilisateur en console,
        et traite l'entrée selon une fonction de traitement donnée en paramètre,
        pour la retourner.
        La question est posée à nouveau tant que la fonction de traitement retourne None.

        Args:
            question (str): La question à poser à l'utilisateur
            traitement_entree (fonction): La fonction traitant l'entrée.

        Returns:
            [type variable]: la sortie de la fonction de traitement
        """

        entree_traitee = None

        while entree_traitee is None:
            entree = input(question)
            entree_traitee = traitement_entree(entree)

        return entree_traitee

    def est_elimine(self):
        """
        Vérifie si le joueur est éliminé, i.e. s'il n'a plus de dés

        Returns:
            bool: True si le joueur est éliminé, False sinon.
        """
        # VOTRE CODE ICI
        if len(self.des) == 0:
            return True
        else:
            return False

    def rendre_de(self, de):
        """
        Ajoute le dé en argument aux dés du joueur (utilisez self.des.append),
        après l'avoir rangé (De.ranger)

        Args:
            de (De): Le dé à ajouter
        """
        # VOTRE CODE ICI
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
        # VOTRE CODE ICI
        liste_lancer = []
        for i in self.des:
            liste_lancer.append(self.creer_lancer(self.piger_coordonnees(), self.piger_angle(), self.piger_puissance()))
        return liste_lancer

    def __str__(self):
        """
        Donne la représentation en chaîne de caractères du joueur.

        Returns:
            str: la représentation en chaîne de caractères
        """
        return f"joueur {self.numero_joueur} ({len(self.des)} dés)"
