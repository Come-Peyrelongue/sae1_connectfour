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
        raise ValueError("placerPionPlateau : La valeur de la colonne (numColumn) n’est pas correcte")

    positionPion = const.NB_LINES - 1
    while positionPion > -1 and plateau[positionPion][numColumn] is not None:
        positionPion -= 1
    plateau[positionPion][numColumn] = pion

    return positionPion