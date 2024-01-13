from Model.Constantes import *
from Model.Plateau import *
from Model.Joueur import *
from Model.Pion import *
from random import randint, choice
p = construirePlateau()
print(p)
pion = construirePion(const.JAUNE)
line = placerPionPlateau(p, pion, 2)
print("Placement d’un pion en colonne 2. Numéro de ligne :", line)
print(p)
# Essais sur les couleurs
print("\x1B[43m \x1B[0m : carré jaune ")
print("\x1B[41m \x1B[0m : carré rouge ")
print("\x1B[41mA\x1B[0m : A sur fond rouge")

for _ in range(20):
    placerPionPlateau(p, construirePion(choice(const.COULEURS)), randint(0, const.NB_COLUMNS - 1))
print(toStringPlateau(p))

print("Pions gagnants : ",getPionsGagnantsPlateau(p))
print("Plateau rempli : ",isRempliPlateau(p))
joueur = construireJoueur(1)
print("Joueur : ",joueur)
print("Couleur du joueur : ",getCouleurJoueur(joueur))
print("Plateau du joueur : ",getPlateauJoueur(joueur))
print("Fonction du joueur : ",getPlacerPionJoueur(joueur))
print("Pion du joueur : ",getPionJoueur(joueur))
print("Placer Pion du joueur : ",setPlacerPionJoueur(joueur,))