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