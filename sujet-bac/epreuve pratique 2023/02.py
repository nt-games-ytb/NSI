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
