#Exercice 1
def moyenne(tab):
    if tab == []:
        return "La liste est vide !"
    total_des_notes = 0
    for element in tab:
        total_des_notes = total_des_notes + element
    return total_des_notes / len(tab)

print("Exemple exercice 1 :")
print(moyenne([5, 3, 8]))
print(moyenne([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(moyenne([])) # Comportement différent suivant le traitement proposé.
print()



#Exerice 2
def tri(tab):
    # i est le premier indice de la zone non triee,
    # j est le dernier indice de cette zone non triée. 
    # Au debut, la zone non triee est le tableau complet.
    i = 0
    j = len(tab) - 1
    while i != j :
        if tab[i] == 0:
            i = i + 1
        else :
            valeur = tab[j]
            tab[j] = 1
            tab[i] = valeur
            j = j - 1
    return tab

print("Exemple exercice 2 :")
print(tri([0, 1, 0, 1, 0, 1, 0, 1, 0]))