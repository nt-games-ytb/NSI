liste = [9, 5, 8, 4, 0, 2, 7, 1, 10, 3, 6]

def tri_insertion(tab):
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[...]
        # la variable j sert Ã  dÃ©terminer oÃ¹ placer la valeur Ã  ranger
        j = ...
        # tant qu'on a pas trouvÃ© la place de l'Ã©lÃ©ment Ã  insÃ©rer
        # on dÃ©cale les valeurs du tableau vers la droite
        while j > ... and valeur_insertion < tab[...]:
            tab[j] = tab[j-1]
            j = ...
        tab[j] = ...