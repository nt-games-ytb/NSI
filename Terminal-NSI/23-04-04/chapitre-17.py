def rechercheTextuBASIQUE(sequence, texte):
    indice_depart = 0
    indice_fin = 0
    mot = False
    for i in range(len(texte)):
        if sequence[0] == c:
            bon = True
            j = 0
            while bon == True:
                if j == len(sequence) - 1:
                    bon = False
                    indice_fin = i +j
                    mot = True
                elif texte[i + j] != sequence[i]:
                    bon = False
                    j = j + 1
    if mot == True:
        print([indice_depart, indice_fin])
    return mot
        
                