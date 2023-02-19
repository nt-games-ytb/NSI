#Exercice 1
def recherche_min(tab):
    min = tab[0]
    indice_min = 0
    for i in range(1, len(tab)):
        if min > tab[i]:
            min = tab[i]
            indice_min = i
    return indice_min

print("Exemple exercice 1 :")
print(recherche_min([5]))
print(recherche_min([2, 4, 1]))
print(recherche_min([5, 3, 2, 2, 4]))
print()



#Exerice 2
def separe(tab):
    gauche = 0
    droite = len(tab) - 1
    while gauche < droite :
        if tab[gauche] == 0 :
            gauche = gauche + 1
        else :
            tab[gauche], tab[droite] = tab[droite], tab[gauche]
            droite = droite - 1
    return tab

print("Exemple exercice 2 :")
print(separe([1, 0, 1, 0, 1, 0, 1, 0]))
print(separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]))