'''Comment jouer :
- Divisez les 54 cartes en deux (Jokers inclut)
- Retournez une carte de chaque paquets
- Celui qui as la plus forte remporte la carte de l'autre et met les carte dans son paquets de "cartes gagner"
(Si c'est la même carte il y a une bataille, on retourne une carte face caché et encore une autre et ainsi de suite)
- On continue jusqu'à ce que plus personne ait de cartes
- Quand plus personne n'a de carte on demande si ils veulent continuer et si il veulent on continue avec le paquets de "cartes gagner"
- C'est celui qui as le plus de cartes qui as gagner
'''

'''A faire :
[ ] Faire un dictionnaire paquets avec keys (carreaux, tréfles, coeurs, piques et jokers) et values (2,3,4,5,6,7,8,9,10,Valets,Dame,Rois et As)
[ ] Faire la distibution
    [ ] Faire une boucle qui s'arrête quand carte distribuer est à 54
    [ ] Faire une sous boucle qui s'arrête à la moitier du paquets (27)
    [ ] Un nombre random qui prend une keys (entre 1 et 5) en les listant
    [ ] Un nombre random qui prend une values (entre 1 et 3)
    [ ] Check si la valeur ne vaut pas " "
    [ ] Sinon :
        [ ] Ajouter 1 à carte distribuer
        [ ] On ajoute juste la valeur de la carte ou un tableau de la valeur et du type de la carte dans le tableau joueur1 et joueur2
        [ ] On remplace la valeur par " "
[ ] Faire une boucle jusqu'à ce que les tableaux soit vides
    [ ] Chaque paquets met sa première carte 
    [ ] Si s'est la même alors faire une boucle qui s'arrête quznd c'est bon et mettre une carte sans comparer et dire les noms puis mettre une autre et recomparer et si s'est pas bon la boucle recommence
    [ ] Sinon ajouter la carte à paquets_gagnant_joueur puis supprimer la carte du paquet du joueur
[ ] Quand s'est finis demander de recommencer et si oui demande si à partir du paquets obtenue (+ verif si y'a pas zéro carte dans un paquets) sinon recommencer du début et sinon exit
Bonus :
[ ] Faire un design avec PyQT
[ ] Faire un menu 
    [ ] Faire une partie paramètres
    [ ] Faire une partie crédits/règles du jeu
[ ] Faire un speedmode
[ ] Faire des plus grosses parties (9,6,3,etc)
'''

import sys
import os
from pathlib import Path

color = {
    "Noir": "\u001b[30m",
    "Rouge": "\u001b[31m",
    "Vert": "\u001b[32m",
    "Jaune": "\u001b[33m",
    "Bleu": "\u001b[34m",
    "Magenta": "\u001b[35m",
    "Cyan": "\u001b[36m",
    "Blanc": "\u001b[37m",
    "Normal": "\u001b[0m"
}

paquet_simple = {
    "carreaux" : ["2", "3" , "4", "5", "6", "7", "8" ,"9" , "10", "valet", "dame" , "roi", "as"],
    "cœurs" : ["2", "3" , "4", "5", "6", "7", "8" ,"9" , "10", "valet", "dame" , "roi", "as"],
    "piques" : ["2", "3" , "4", "5", "6", "7", "8" ,"9" , "10", "valet", "dame" , "roi", "as"],
    "trèfles" : ["2", "3" , "4", "5", "6", "7", "8" ,"9" , "10", "valet", "dame" , "roi", "as"],
    "jokers" : ["jokers1", "jokers2"]
}

def creation():
    print(color["Bleu"] + "===============================================================")
    print("|  _             ____        _        _ _ _                   |")
    print("| | |           |  _ \      | |      (_) | |                  |")
    print("| | |     __ _  | |_) | __ _| |_ __ _ _| | | ___              |")
    print("| | |    / _` | |  _ < / _` | __/ _` | | | |/ _ \             |")
    print("| | |___| (_| | | |_) | (_| | || (_| | | | |  __/             |")
    print("| |______\__,_| |____/ \__,_|\__\__,_|_|_|_|\___| by nt games |")
    print("|                                                             |")
    print("===============================================================\n" + color["Cyan"])

    print("Que voulez-vous faire ?")
    print("1 - Créer une partie")
    print("2 - Paramètres")
    print("3 - Crédits")
    choix = int(input("Choix : "))

    #if os.path.exists('test.txt'):
    pass

def reprendre():
    if os.path.exists("a"):
        #reprendre
        
        print("a")
    else:
        #supprime l'ancienne sav et en créer une
        creation()
    pass

def distribution(paquet):
    pass



reprendre()
