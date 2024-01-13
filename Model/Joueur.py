from Model.Constantes import *
from Model.Pion import *
from Model.Plateau import *



#
# Ce fichier contient les fonctions gérant le joueur
#
# Un joueur sera un dictionnaire avec comme clé :
# - const.COULEUR : la couleur du joueur entre const.ROUGE et const.JAUNE
# - const.PLACER_PION : la fonction lui permettant de placer un pion, None par défaut,
#                       signifiant que le placement passe par l'interface graphique.
# - const.PLATEAU : référence sur le plateau de jeu, nécessaire pour l'IA, None par défaut
# - d'autres constantes nécessaires pour lui permettre de jouer à ajouter par la suite...
#

def type_joueur(joueur: dict) -> bool:
    """
    Détermine si le paramètre peut correspondre à un joueur.
    :param joueur: Paramètre à tester
    :return: True s'il peut correspondre à un joueur, False sinon.
    """
    if type(joueur) != dict:
        return False
    if const.COULEUR not in joueur or joueur[const.COULEUR] not in const.COULEURS:
        return False
    if const.PLACER_PION not in joueur or (joueur[const.PLACER_PION] is not None
            and not callable(joueur[const.PLACER_PION])):
        return False
    if const.PLATEAU not in joueur or (joueur[const.PLATEAU] is not None and
        not type_plateau(joueur[const.PLATEAU])):
        return False
    return True

def getCouleurJoueur(joueur: dict) -> int:
    """
    Fonction qui retourne la couleur d'un joueur passé en paramètre
    :param joueur: dict du joueur
    :return: couleur du joueur
    """
    if not type(joueur)==dict:
        raise TypeError("getCouleurJoueur : Le paramètre ne correspond pas à un joueur")
    couleur = joueur["Couleur"]
    return couleur

def getPlateauJoueur(joueur: dict) -> list:
    """
    Fonction qui retourne le plateau d'un joueur passé en paramètre
    :param joueur: dict du joueur
    :return: plateau du joueur
    """
    if not type(joueur) == dict:
        raise TypeError("getPlateauJoueur : Le paramètre ne correspond pas à un joueur")
    plateau = joueur["Plateau"]
    return plateau

def getPlacerPionJoueur(joueur: dict):
    """
    Fonction qui retourne le plateau d'un joueur passé en paramètre
    :param joueur: dict du joueur
    :return: plateau du joueur
    """
    if not type(joueur) == dict:
        raise TypeError("getPlacerPionJoueur : Le paramètre ne correspond pas à un joueur")
    fonction = joueur["Fonction"]
    return fonction