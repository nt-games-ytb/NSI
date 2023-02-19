#Exercice 1
def moyenne(tab):
    '''
        moyenne(list) -> float
        Entrée : un tableau non vide d'entiers
        Sortie : nombre de type float Correspondant à la moyenne des valeurs présentes dans le tableau
    '''
    total_des_notes = 0
    for element in tab:
        total_des_notes = total_des_notes + element
    return total_des_notes / len(tab)

def moyenne_rapide(tab):
    #assert len(tab) > 0, "Le tableau ne doit pas être vide !"
    return sum(tab) / len(tab)

print("Exemple exercice 1 :")
print(moyenne([1]))
print(moyenne([1, 2, 3, 4, 5, 6, 7]))
print(moyenne([1, 2]))
print(moyenne([4, 8, 6, 3, 9]))
print()



#Exerice 2
def dichotomie(tab, x):
    """
        tab : tableau trié dans l’ordre croissant
        x : nombre entier
        La fonction renvoie True si tab contient x et False sinon
    """
    # cas du tableau vide
    if tab == []:
        return False, 1
    # cas où x n'est pas compris entre les valeurs extrêmes
    if (x < tab[0]) or (x > tab[-1]):
        return False, 2
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False, 3 

print("Exemple exercice 2 :")
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28))
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27))
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 1))
print(dichotomie([], 28))