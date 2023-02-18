#Exercice 1

print("Exemple exercice 1 :")
print(couples_consecutifs([1, 4, 3, 5]))
print(couples_consecutifs([1, 4, 5, 3]))
print(couples_consecutifs([1, 1, 2, 4]))
print(couples_consecutifs([7, 1, 2, 5, 3, 4]))
print(couples_consecutifs([5, 1, 2, 3, 8, -5, -4, 7]))
print()



#Exerice 2
def propager(M, i, j, val):
    if M[i][j] == ...:
        M[i][j] = val

    # l'element en haut fait partie de la composante
    if i-1 >= 0 and M[i-1][j] == ...:
        propager(M, i-1, j, val)

    # l'element en bas fait partie de la composante
    if ... < len(M) and M[i+1][j] == 1:
        propager(M, ..., j, val)

    # l'element Ã  gauche fait partie de la composante
    if ... and M[i][j-1] == 1:
        propager(M, ..., ..., val)

    # l'element Ã  droite fait partie de la composante
    if ... and ...:
        propager(..., ..., ..., ...)

print("Exemple exercice 2 :")
M = [[0,0,1,0],[0,1,0,1],[1,1,1,0],[0,1,1,0]]
propager(M,2,1,3)
print(M)