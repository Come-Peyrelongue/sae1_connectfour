# Model/Pion.py

from Model.Constantes import *

#
# Ce fichier implémente les données/fonctions concernant le pion
# dans le jeu du Puissance 4
#
# Un pion est caractérisé par :
# - sa couleur (const.ROUGE ou const.JAUNE)
# - un identifiant de type int (pour l'interface graphique)
#
# L'identifiant sera initialisé par défaut à None
#

def type_pion(pion: dict) -> bool:
    """
    Détermine si le paramètre peut être ou non un Pion

    :param pion: Paramètre dont on veut savoir si c'est un Pion ou non
    :return: True si le paramètre correspond à un Pion, False sinon.
    """
    return type(pion) == dict and len(pion) == 2 and const.COULEUR in pion.keys() \
        and const.ID in pion.keys() \
        and pion[const.COULEUR] in const.COULEURS \
        and (pion[const.ID] is None or type(pion[const.ID]) == int)


def construirePion(couleur: int) -> dict:
    """
    Fonction permettant de construire un pion
    :param color: Couleur du pion à construire
    :return: Dictionnaire représentant un pion
    """
    if type(couleur) != int:
        raise TypeError("construirePion : Le paramètre n’est pas de type entier")
    if couleur not in const.COULEURS:
        raise ValueError(f"construirePion : la couleur ({couleur}) n’est pas correcte")

    pion = {const.COULEUR : couleur, const.ID : None}
    return pion

def getCouleurPion(pion: dict) -> int:
    """
    Fonction permettant de récupérer la couleur d'un pion
    :param pion: pion dont il faut récupérer la couleur
    :return: int de la couleur du pion
    """
    if type(pion) != dict:
        raise TypeError("getCouleurPion : Le paramètre n’est pas un pion")
    return pion[const.COULEUR]

def setCouleurPion(pion: dict, couleur: int) -> None:
    """
    Fonction permettant de changer la couleur du pion
    :param pion: pion dont il faut changer la couleur
    :param couleur: nouvelle couleur du pion
    :return: None
    """
    if type(pion) != dict:
        raise TypeError("setCouleurPion : Le premier paramètre n’est pas un pion")
    if type(couleur) != int:
        raise TypeError("setCouleurPion : Le second paramètre n’est pas un entier.")
    if couleur not in const.COULEURS:
        raise ValueError(f"setCouleurPion : Le second paramètre ({couleur}) n’est pas une couleur")

    pion[const.COULEUR] = couleur
    return None

def getIdPion(pion: dict) -> int:
    """
    Fonction permettant de récupérer l'ID d'un pion
    :param pion: pion dont l'on récupère l'ID
    :return: int de l'ID
    """
    if not type_pion(pion):
        raise TypeError("getIdPion : Le paramètre n’est pas un pion")

    return pion[const.ID]

def setIdPion(pion: dict, id: int) -> None:
    """
    Fonction permettant de changer la couleur du pion
    :param pion: pion dont il faut changer la couleur
    :param id: nouvel id du pion
    :return: None
    """
    if not type_pion(pion):
        raise TypeError("setIdPion : Le premier paramètre n’est pas un pion")
    if type(id) != int:
        raise TypeError("setIdPion : Le second paramètre n’est pas un entier.")

    pion[const.ID] = id
    return None