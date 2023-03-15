#Exercice 1
def tri_selection(tab):
    for i in range(len(tab)):
        plus_petite_valeur = tab[i]
        indice_plus_petit = i

        for j in range(i, len(tab)):
            if plus_petite_valeur > tab[j]:
                plus_petite_valeur = tab[j]
                indice_plus_petit = j

        tab[indice_plus_petit], tab[i] = tab[i], tab[indice_plus_petit]
    return tab
    
def tri_selection_prof(tab):
    if len(tab) <= 1:
        return tab
    for indice in range(len(tab)-1):
        indice_mini = indice
        for i in range(indice+1, len(tab)):
            if tab[indice_mini] > tab[i]:
                indice_mini = i
                

print("Exemple exercice 1 :")
print(tri_selection([1, 52, 6, -9, 12]))
print()



#Exerice 2
from random import randint

def plus_ou_moins():
    nb_mystere = randint(1, 99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 0

    while nb_mystere != nb_test and compteur < 9:
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print("Bravo ! Le nombre etait", nb_mystere)
        print("Nombre d'essais: ", compteur)
    else:
        print("Perdu ! Le nombre etait", nb_mystere)

print("Exemple exercice 2 :")
plus_ou_moins()
