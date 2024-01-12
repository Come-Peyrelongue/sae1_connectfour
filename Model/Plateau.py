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
                listesSeries.append(list(liste[:4]))
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
                listesSeries.append(list(liste[:4]))

    return listesSeries

def detecter4diagonaleDirectePlateau(plateau: list, couleur: int) -> list:
    """
    Fonction qui permet de détecter les diagonales de 4 pions de la couleur donnée
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
                    listesSeries.append(list(liste[:4]))
    return listesSeries