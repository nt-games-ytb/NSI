#Exercice 1

print("Exemple exercice 1 :")
print(moyenne([5, 3, 8]))
print(moyenne([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(moyenne([])) # Comportement différent suivant le traitement proposé.
print()



#Exerice 2
def tri(tab):
    # i est le premier indice de la zone non triee,
    # j est le dernier indice de cette zone non triÃ©e. 
    # Au debut, la zone non triee est le tableau complet.
    i= ...
    j= ...
    while i != j :
        if tab[i] == 0:
            i= ...
        else :
            valeur = tab[j]
            tab[j] = ...
            ...
            j= ...
    ...

print("Exemple exercice 2 :")
print(tri([0, 1, 0, 1, 0, 1, 0, 1, 0]))