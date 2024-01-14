from Model.Constantes import *
from Model.Pion import *
from Model.Plateau import *
from random import *



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

def getPionJoueur(joueur: dict) -> dict:
    if not type(joueur) == dict:
        raise TypeError("getPionJoueur : Le paramètre ne correspond pas à un joueur")
    couleur = joueur["Couleur"]
    pion = {const.COULEUR: couleur, const.ID: None}
    return pion

def setPlateauJoueur(joueur: dict, plateau: list) -> None:
    """
    Fonction qui affecte le plateau au joueur
    :param joueur: dict représentant le jour
    :param plateau: list représentant le plateau
    :return: none
    """
    if not type(joueur) == dict:
        raise TypeError("setPlateauJoueur : Le paramètre ne correspond pas à un joueur")
    if not type(plateau) == list:
        raise TypeError("setPlateauJoueur : Le paramètre ne correspond pas à un plateau")
    joueur["Plateau"] = plateau
    return None

def setPlacerPionJoueur(joueur: dict, affecter: callable) -> None:
    """
    Fonction qui affecte le plateau au joueur
    :param joueur: dict représentant le jour
    :param plateau: list représentant le plateau
    :return: none
    """
    if not type(joueur) == dict:
        raise TypeError("setPlacerPionJoueur : Le paramètre ne correspond pas à un joueur")
    if not callable(affecter) == True:
        raise TypeError("setPlacerPionJoueur : Le paramètre ne correspond pas à une fonction")
    joueur[const.PLACER_PION] = affecter
    return None

def _placerPionJoueur(joueur: dict) -> int:
    """
    Fonction qui tire un numéro de colonne à jouer au hasard
    :param joueur: joueur qui va jouer dans la colonne
    :return: num de la colonne
    """
    if not type(joueur) == dict:
        raise TypeError("initialiserIAJoueur : Le premier paramètre n’est pas un joueurr")
    nombre = randint(0, (const.NB_COLUMNS-1))
    return nombre

def initialiserIAJoueur(joueur: dict, rang: bool) -> None:
    if not type(joueur) == dict:
        raise TypeError("initialiserIAJoueur : Le premier paramètre n’est pas un joueurr")
    if not type(rang) == bool:
        raise TypeError("initialiserIAJoueur : Le second paramètre n’est pas un booléen")
    setPlacerPionJoueur(joueur,  _placerPionJoueur(joueur))
    return None

def setModeEtenduJoueur(joueur: dict, oui: bool) -> None:
    if oui == True:
        destFichier= r"../Constantes.py"
        with open(destFichier, "a") as f:
            f.write("const.MODE_ETENDU = \"ModeEtendu\"")
    else:
        with open("Constantes.py", "r+") as fp:
            lines = fp.readlines()
            fp.seek(0)
            fp.truncate()
            fp.writelines(lines[:1])