#Exercice 1

print("Exemple exercice 1 :")
print(recherche_min([5]))
print(recherche_min([2, 4, 1]))
print(recherche_min([5, 3, 2, 2, 4]))
print()



#Exerice 2
def separe(tab):

    gauche = 0
    droite = ...
    while gauche < droite :
        if tab[gauche] == 0 :
            gauche = ...
        else :
            tab[gauche], tab[droite] = ...
            droite = ...
    return tab

print("Exemple exercice 2 :")
print(separe([1, 0, 1, 0, 1, 0, 1, 0]))
print(separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]))