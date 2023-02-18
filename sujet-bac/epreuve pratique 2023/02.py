#Exercice 1
def indices_maxi(tab):
    plus_grande_valeur = tab[0]
    indice_plus_grande_valeur = []
    for i in range(1, len(tab)):
        if tab[i] == plus_grande_valeur:
            indice_plus_grande_valeur.append(i)
        elif tab[i] > plus_grande_valeur:
            indice_plus_grande_valeur = []
            plus_grande_valeur = tab[i]
            indice_plus_grande_valeur.append(i)
    return (plus_grande_valeur, indice_plus_grande_valeur)

print("Exemple exercice 1 :")
print(indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))
print(indices_maxi([7]))
print()



#Exercice 2
def positif(pile):
    pile_1 = list(pile)
    pile_2 = []
    while pile_1 != []:
        x = pile_1.pop()
        if x >= 0:
            pile_2.append(x)
    while pile_2 != []:
        x = pile_2.pop()
        pile_1.append(x)
    return pile_1

print("Exemple exercice 2 :")
print(positif([-1, 0, 5, -3, 4, -6, 10, 9, -8]))
print(positif([-2]))