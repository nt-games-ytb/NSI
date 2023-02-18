#Exercice 1

print("Exemple exercice 1 :")
print(moyenne())
print()



#Exerice 2
def dichotomie(tab, x):
    """
        tab : tableau trié dans l’ordre croissant
        x : nombre entier
        La fonction renvoie True si tab contient x et False sinon
    """
    # cas du tableau vide
    if ...:
        return False, 1
    # cas où x n'est pas compris entre les valeurs extrêmes
    if (x < tab[0]) or ...:
        return False, 2
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = ...
        if x == tab[m]:
            return ...
        if x > tab[m]:
            debut = m + 1
        else:
            fin = ...
    return ...

print("Exemple exercice 2 :")
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28))
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27))
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 1))
print(dichotomie([], 28))