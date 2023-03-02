#Exercice 1
def couples_consecutifs(tab):
    '''
    une fonction couples_consecutifs qui prend en paramètre une liste de nombres entiers
    tab non vide, et qui renvoie la liste (éventuellement vide) des couples d'entiers
    consécutifs successifs qu'il peut y avoir dans tab.
    '''
    resultat = []
    for i in range(len(tab) - 1):
        if tab[i] + 1 == tab[i + 1]:
            resultat.append((tab[i], tab[i + 1]))
    return resultat 

print("Exemple exercice 1 :")
print(couples_consecutifs([1, 4, 3, 5]))
print(couples_consecutifs([1, 4, 5, 3]))
print(couples_consecutifs([1, 1, 2, 4]))
print(couples_consecutifs([7, 1, 2, 5, 3, 4]))
print(couples_consecutifs([5, 1, 2, 3, 8, -5, -4, 7]))
print()



#Exerice 2
def propager(M, i, j, val):
    if M[i][j] == 1:
        M[i][j] = val

    # l'element en haut fait partie de la composante
    if i-1 >= 0 and M[i-1][j] == 1:
        propager(M, i-1, j, val)

    # l'element en bas fait partie de la composante
    if i+1 < len(M) and M[i+1][j] == 1:
        propager(M, i + 1, j, val)

    # l'element à gauche fait partie de la composante
    if j-1 >= 0 and M[i][j-1] == 1:
        propager(M, i, j-1, val)

    # l'element à droite fait partie de la composante
    if j+1 < len(M) and M[i][j+1] == 1:
        propager(M, i, j+1, val)

print("Exemple exercice 2 :")
M = [[0,0,1,0],[0,1,0,1],[1,1,1,0],[0,1,1,0]]
propager(M,2,1,3)
print(M)