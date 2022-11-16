#Chapitre 5
import ast

#Exercie 15
arbre = ["Toto",
["Tantan", ["Titi", None, None], ["Tutu", None, None]],
["Tintin", ["Furfur", None, None], ["Teïteï", ["Tojtoj", None, None], ["Têtê", None, None]]]
]

#Exercice 16
#Question 1
def ajoutfeuilletoutagauche(une_liste, une_valeur):#Ajout tout à gauche
    if une_liste[1] != None:
        ajoutfeuilletoutagauche(une_liste[1], une_valeur)
    else:
        une_liste[1] = [une_valeur, None, None]
    return arbre

def ajoutfeuillegauche(une_liste, une_valeur):
    une_liste[1] = [une_valeur, None, None]
    
#Question 2
def ajoutfeuilledroite(une_liste, une_valeur):
    une_liste[2] = [une_valeur, None, None]
    
#Question 3
def test_taille(une_liste, resultat):
    '''résultat = 1 #car racine obligatoire
    résultat_gauche = 0
    résultat_droite = 0
    if une_liste[1] != None:
        résultat_gauche = 1
        taille(une_liste[1])
    if une_liste[2] != None:
        résultat_droite = 1
        taille(une_liste[2])
    return résultat_gauche + résultat_droite'''
    if une_liste[1] != None and une_liste[2] != None:
        taille(une_liste[1])
        taille(une_liste[2])
        resultat += 2
        return 2
    elif une_liste[1] != None:
        taille(une_liste[1])
        resultat += 1
        return 1
    elif une_liste[2] != None:
        taille(une_liste[2])
        resultat += 1
        return 1
    else:
        return 0

def taille(une_liste):
    if une_liste == None:
        return 0
    else:
        return 1 + taille(une_liste[1]) + taille(une_liste[2])
    
#Question 4
compteur = 0
def test_hauteur(une_liste):
    global compteur
    taille_gauche = taille(une_liste[1])
    taille_droite = taille(une_liste[2])
    if taille_gauche >= taille_droite:
        compteur += 1
        if une_liste[1] == None:
            test_hauteur(une_liste[1])
    elif taille_gauche < taille_droite :
        compteur += 1
        if une_liste[1] == None:
            test_hauteur(une_liste[2])
    return compteur 
    
def hauteur(une_liste):
    if une_liste == None:
        return 0
    else:
        return 1 + max(hauteur(une_liste[1]), hauteur(une_liste[2]))
    
#Question 5
def test_nombrefeuille(une_liste):
    if une_liste[1] == None:
        return 1
    elif une_liste[2] == None:
        return 1
    else:
        return test_nombrefeuille(une_liste[1]) + test_nombrefeuille(une_liste[2])
        
def nombrefeuille(une_liste):
    if une_liste == None:
        return 0
    elif une_liste[1] == None and une_liste[2] == None:
        return 1
    else:
        return nombrefeuille(une_liste[1]) + nombrefeuille(une_liste[2])