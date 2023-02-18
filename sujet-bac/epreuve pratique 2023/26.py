#Exercice 1
def multiplication(n1, n2):
    resultat = 0
    negatif = False
    if n2 < 0:
        n2 = -n2
        negatif = True
    for i in range(n2):
        resultat = resultat + n1
    if negatif == True:
        resultat = -resultat
    return resultat

print("Exemple exercice 1 :")
print(multiplication(3, 5))
print(multiplication(-4, -8))
print(multiplication(-2, 6))
print(multiplication(-2, 0))
print()



#Exerice 2
def dichotomie(tab, x):
    """
    tab : tableau d’entiers trié dans l’ordre croissant
    x   : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    debut = 0
    fin = len(tab) - 1 #8
    while debut <= fin:
        m = (debut + fin) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False

print("Exemple exercice 2 :")
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28))
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27))