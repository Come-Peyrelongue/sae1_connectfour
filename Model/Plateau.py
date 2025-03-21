from Model.Constantes import *
from Model.Pion import *


#
# Le plateau représente la grille où sont placés les pions.
# Il constitue le coeur du jeu car c'est dans ce fichier
# où vont être programmées toutes les règles du jeu.
#
# Un plateau sera simplement une liste de liste.
# Ce sera en fait une liste de lignes.
# Les cases du plateau ne pourront contenir que None ou un pion
#
# Pour améliorer la "rapidité" du programme, il n'y aura aucun test sur les paramètres.
# (mais c'est peut-être déjà trop tard car les tests sont fait en amont, ce qui ralentit le programme...)
#

def type_plateau(plateau: list) -> bool:
    """
    Permet de vérifier que le paramètre correspond à un plateau.
    Renvoie True si c'est le cas, False sinon.

    :param plateau: Objet qu'on veut tester
    :return: True s'il correspond à un plateau, False sinon
    """
    if type(plateau) != list:
        return False
    if len(plateau) != const.NB_LINES:
        return False
    wrong = "Erreur !"
    if next((wrong for line in plateau if type(line) != list or len(line) != const.NB_COLUMNS), True) == wrong:
        return False
    if next((wrong for line in plateau for c in line if not(c is None) and not type_pion(c)), True) == wrong:
        return False
    return True


def construirePlateau() -> list:
    """
    Fonction qui créé un tableau de NB_LIGNES et NB_COLUMNS
    :return: tableau
    """
    tableau = []
    for i in range(const.NB_LINES):
        ligne = []
        for y in range(const.NB_COLUMNS):
            ligne.append(None)
        tableau.append(ligne)
    return tableau

def placerPionPlateau(plateau: list, pion: dict, numColumn: int):
    """
    Fonction qui place le pion dans la colonne choisie, en fonction des éléments placés en dessous.
    :param plateau: plateau de jeu
    :param pion: pion que l'on veut placer
    :param numColumn: numéro de la colonne où l'on veux placer notre pion
    :return: on return la position du pion, ou -1 si la colonne est complète
    """
    if type(plateau) != list:
        raise TypeError("placerPionPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(pion) != dict:
        raise TypeError("placerPionPlateau : Le second paramètre n’est pas un pion")
    if type(numColumn) != int:
        raise TypeError("placerPionPlateau : Le troisième paramètre n’est pas un entier")
    if numColumn > const.NB_COLUMNS:
        raise ValueError(f"placerPionPlateau : La valeur de la colonne ({num}) n’est pas correcte")

    positionPion = const.NB_LINES - 1
    while positionPion > -1 and plateau[positionPion][numColumn] is not None:
        positionPion -= 1
    plateau[positionPion][numColumn] = pion

    return positionPion

def toStringPlateau(plateau: list) -> str:
    """
    Fonction retournant le plateau en chaine de charactère avec couleur
    :param plateau: plateau
    :return: le plateau en chaine de charatère
    """
    tableau = ""
    for ligne in plateau:
        for case in ligne:
            tableau += "|"
            if case is None:
                tableau += " "
            else:
                couleur = getCouleurPion(case)
                if couleur == const.JAUNE:
                    tableau += "\x1B[43m \x1B[0m"
                elif couleur == const.ROUGE:
                    tableau += "\x1B[41m \x1B[0m"
        tableau += "|\n"
    tableau += "-" * 15 + "\n"
    tableau += "1 2 3 4 5 6"
    return tableau

def detecter4horizontalPlateau(plateau: list, couleur: int) -> list:
    """
    Fonction qui permet de détecter les lignes de 4 pions de la couleur donnée
    :param plateau: plateau à analyser
    :param couleur: couleur donnée à détecter sur le plateau
    :return: on return une liste de séries ou une liste vide s'il n'y a aucune série
    """
    if not type_plateau(plateau):
        raise TypeError("detecter4horizontalPlateau : Le premier paramètre ne correspond pas à un plateau")
    elif type(couleur) is not int:
        raise TypeError("detecter4horizontalPlateau : Le second paramètre n’est pas un entier")
    elif couleur not in const.COULEURS:
        raise ValueError(f"détecter4horizontalPlateau : La valeur de la couleur ({couleur}) n’est pas correcte")

    listesSeries = []

    for ligne in plateau:
        compteur = 0
        liste = []
        for hole in ligne:
            if hole is not None and getCouleurPion(hole) == couleur:
                compteur += 1
                liste.append(hole)
            else:
                compteur = 0
                liste = []
            if compteur == 4:
                listesSeries = list(liste[:4])
    return listesSeries

def detecter4verticalPlateau(plateau: list, couleur: int) -> list:
    """
    Fonction qui permet de détecter les colonnes de 4 pions de la couleur donnée
    :param plateau: plateau à analyser
    :param couleur: couleur donnée à détecter sur le plateau
    :return: on return une liste de séries ou une liste vide s'il n'y a aucune série
    """
    if not type_plateau(plateau):
        raise TypeError("detecter4verticalPlateau : Le premier paramètre ne correspond pas à un plateau")
    elif type(couleur) != int:
        raise TypeError("detecter4verticalPlateau : Le second paramètre n’est pas un entier")
    elif couleur not in const.COULEURS:
        raise ValueError(f"detecter4verticalPlateau : La valeur de la couleur ({couleur}) n’est pas correcte")

    listesSeries = []

    for colonne in range(const.NB_COLUMNS):
        compteur = 0
        liste = []
        for ligne in range(const.NB_LINES):
            pion = plateau[ligne][colonne]
            if pion is not None and getCouleurPion(pion) == couleur:
                compteur += 1
                liste.append(pion)
            else:
                compteur = 0
                liste = []
            if compteur == 4:
                listesSeries = list(liste[:4])

    return listesSeries

def detecter4diagonaleDirectePlateau(plateau: list, couleur: int) -> list:
    """
    Fonction qui permet de détecter les diagonales directes de 4 pions de la couleur donnée
    :param plateau: plateau à analyser
    :param couleur: couleur donnée à détecter sur le plateau
    :return: on return une liste de séries ou une liste vide s'il n'y a aucune série
    """
    if not type_plateau(plateau):
        raise TypeError("detecter4diagonaleDirectePlateau : Le premier paramètre ne correspond pas à un plateau")
    elif type(couleur) != int:
        raise TypeError("detecter4diagonaleDirectePlateau : Le second paramètre n’est pas un entier")
    elif couleur not in const.COULEURS:
        raise ValueError(f"detecter4diagonaleDirectePlateau : La valeur de la couleur ({couleur}) n’est pas correcte")

    listesSeries = []

    for ligne in range(const.NB_LINES - 3):
        for colonne in range(const.NB_COLUMNS - 3):
            compteur = 0
            liste = []
            for i in range(4):
                pion = plateau[ligne + i][colonne + i]
                if pion is not None and getCouleurPion(pion) == couleur:
                    compteur += 1
                    liste.append(pion)
                else:
                    compteur = 0
                    liste = []
                if compteur == 4:
                    listesSeries = list(liste[:4])
    return listesSeries

def detecter4diagonaleIndirectePlateau(plateau: list, couleur: int) -> list:
    """
    Fonction qui permet de détecter les diagonales indirectes de 4 pions de la couleur donnée
    :param plateau: plateau à analyser
    :param couleur: couleur donnée à détecter sur le plateau
    :return: on return une liste de séries ou une liste vide s'il n'y a aucune série
    """
    if not type_plateau(plateau):
        raise TypeError("detecter4diagonaleIndirectePlateau : Le premier paramètre ne correspond pas à un plateau")
    elif type(couleur) != int:
        raise TypeError("detecter4diagonaleIndirectePlateau : Le second paramètre n’est pas un entier")
    elif couleur not in const.COULEURS:
        raise ValueError(f"detecter4diagonaleIndirectePlateau : La valeur de la couleur ({couleur}) n’est pas correcte")

    listeSeries = []

    for ligne in range(const.NB_LINES - 3):
        for colonne in range(3, const.NB_COLUMNS):
            compteur = 0
            liste = []
            for i in range(4):
                pion = plateau[ligne + i][colonne - i]
                if pion is not None and getCouleurPion(pion) == couleur:
                    compteur += 1
                    liste.append(pion)
                else:
                    compteur = 0
                    liste = []
                if compteur == 4:
                    listeSeries = list(liste[:4])
    return listeSeries

def getPionsGagnantsPlateau(plateau: list) -> list:
    """
    Fonction qui permet de récupérer une liste des séries gagnantes du plateau.
    :param plateau: plateau
    :return: liste remplie si il y a des séries gagnantes ou liste vide sinon
    """
    if not type_plateau(plateau):
        raise TypeError("getPionsGagnantsPlateau : Le paramètre n’est pas un plateau")

    """horizontal1 = detecter4horizontalPlateau(plateau,1)
    vertical1 = detecter4verticalPlateau(plateau,1)
    diagDirecte1 = detecter4diagonaleDirectePlateau(plateau,1)
    diagIndirecte1 = detecter4diagonaleIndirectePlateau(plateau,1)
    horizontal0 = detecter4horizontalPlateau(plateau, 0)
    vertical0 = detecter4verticalPlateau(plateau, 0)
    diagDirecte0 = detecter4diagonaleDirectePlateau(plateau, 0)
    diagIndirecte0 = detecter4diagonaleIndirectePlateau(plateau, 0)"""

    liste = []
    liste += detecter4horizontalPlateau(plateau,1)
    liste += detecter4verticalPlateau(plateau,1)
    liste += detecter4diagonaleDirectePlateau(plateau,1)
    liste += detecter4diagonaleIndirectePlateau(plateau,1)
    liste += detecter4horizontalPlateau(plateau, 0)
    liste += detecter4verticalPlateau(plateau, 0)
    liste += detecter4diagonaleDirectePlateau(plateau, 0)
    liste += detecter4diagonaleIndirectePlateau(plateau, 0)
    return liste

def  isRempliPlateau(plateau: list) -> bool:
    """
    Fonction qui défini si un plateau est rempli ou non
    :param plateau:
    :return: true si plateau rempli ou false si plateau non rempli
    """
    if not type_plateau(plateau):
        raise TypeError("isRempliPlateau : Le paramètre n’est pas un plateau")
    res=True
    for colonne in range(const.NB_COLUMNS):
        compteur = 0
        for ligne in range(const.NB_LINES):
            pion = plateau[ligne][colonne]
            if pion is not None:
                compteur += 1
            else:
                compteur = 0
            if compteur > 0:
                res=False
    return res

def construireJoueur(couleur: int) -> dict:
    """
    Fonction qui permet de construire un joueur à partir d'une couleur
    :param couleur: int de la couleur attribuée au joueur
    :return: dict du joueur
    """
    if not type(couleur)==int:
        raise TypeError("construireJoueur : Le paramètre n’est pas un entier")
    if couleur not in const.COULEURS:
        raise ValueError(f"construirePion : la couleur ({couleur}) n’est pas correcte")
    joueur = {"Couleur": couleur, "Plateau": None, "Fonction": None}
    return joueur

def placerPionLignePlateau(plateau: list, pion: dict, ligne: int, left: bool) -> tuple:
    """
    Fonction qui permet de placer un pion dans un lign et non une colonne
    :param plateau: plateau du jeu
    :param pion: pion a pousser
    :param ligne: numéro de la ligne dans laquelle mettre le pion
    :param left: mettre le pion depuis la droite ou la gauche
    :return: truple des pions ayant été poussé
    """
    if not type_plateau(plateau):
        raise TypeError("placerPionLignePlateau : Le premier paramètre n’est pas un plateau")
    if not type_pion(pion):
        raise TypeError("placerPionLignePlateau : Le second paramètre n’est pas un pion")
    if type(ligne) != int:
        raise TypeError("placerPionLignePlateau : le troisième paramètre n’est pas un entier")
    if ligne < 0 and ligne >= const.NB_LINES:
        raise ValueError("placerPionLignePlateau : Le troisième paramètre (valeur_du_paramètre) ne désigne pas une "
                         "ligne")
    if type(left) != bool:
        raise TypeError("« placerPionLignePlateau : le quatrième paramètre n’est pas un booléen")

    pions_pousse = [pion]
    tombe = None

    if left:
        colonne = 0
        while colonne < const.NB_COLUMNS and plateau[ligne][colonne] is not None:
            pions_pousse.append(plateau[ligne][colonne])
            colonne += 1
    else:
        colonne = const.NB_COLUMNS - 1
        while colonne > -1 and plateau[ligne][colonne] is not None :
            pions_pousse.append(plateau[ligne][colonne])
            colonne -= 1

    if colonne < const.NB_COLUMNS - 1:
        tombe = const.NB_LINES
        i = 0
        while ligne + i < const.NB_LINES and plateau[ligne + i][colonne] is None:
            tombe = ligne + i
            i += 1

    res = (pions_pousse, tombe)
    return res

