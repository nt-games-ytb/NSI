#Exercice 1

print("Exemple exercice 1 :")
print(tri_selection([1, 52, 6, -9, 12]))
print()



#Exerice 2
from random import randint

def plus_ou_moins():
    nb_mystere = randint(1, ...)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = ...

    while nb_mystere != ... and compteur < ...:
        compteur = compteur + ...
        if nb_mystere ... nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print("Bravo ! Le nombre etait ", ...)
        print("Nombre d'essais: ", ...)
    else:
        print("Perdu ! Le nombre etait ", ...)

print("Exemple exercice 2 :")
print(plus_ou_moins())