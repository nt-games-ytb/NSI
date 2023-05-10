# Chapitre 17

## Exercice 2
def rechercheTextuBASIQUE(sequence, texte):
    indice_depart = 0
    indice_fin = 0
    mot = False
    i = 0
    while mot == False and i < len(texte):
        if sequence[0] == texte[i]:
            indice_depart = i
            bon = True
            j = 0
            while bon == True:
                if j == len(sequence) - 1:
                    bon = False
                    indice_fin = i + j
                    mot = True
                elif len(texte) - i < len(sequence) or texte[i + j] != sequence[j]:
                    bon = False
                j = j + 1
                #print(i, j, bon)
        i = i + 1
    if mot == True:
        print([indice_depart, indice_fin])
    return mot

print(rechercheTextuBASIQUE("coucou","Bonjour, coucou!"))
        
def rechercheTextuBASIQUE_v2(sequence, texte):
    indice_depart = 0
    indice_fin = 0
    mot = False
    i = 0
    while mot == False and i < len(texte) - len(sequence) + 1:
        if sequence[0] == texte[i]:
            indice_depart = i
            bon = True
            j = 0
            while bon == True:
                if j == len(sequence) - 1:
                    bon = False
                    indice_fin = i + j
                    mot = True
                elif texte[i + j] != sequence[j]:
                    bon = False
                j = j + 1
                #print(i, j, bon)
        i = i + 1
    if mot == True:
        print([indice_depart, indice_fin])
    return mot

print(rechercheTextuBASIQUE_v2("coucou","Bonjour, coucou!"))
    
def rechercheTextuBASIQUE_prof(sequence, texte):
    if len(sequence) > len(texte):
        return False
    indice = 0
    while indice < len(texte) - len(sequence):
        correspondance = True
        indice_sequence = 0
        indice_texte = indice
        while correspondance and len(sequence) > indice_sequence:
            if texte[indice_texte] == sequence[indice_sequence]:
                indice_sequence = indice_sequence + 1
                indice_texte = indice_texte + 1
            else:
                correspondance = False
        if correspondance:
            print([indice, indice + len(sequence) -1])
            return True
        indice = indice + 1
    return False

print(rechercheTextuBASIQUE_prof("coucou","Bonjour, coucou!"))



## Exercice 4
def constru_dico(sequence):
    dico = {}
    for i in range(len(sequence) - 1):
        dico[sequence[i]] = len(sequence) - i -1
    return dico

print(constru_dico("coucou"))
   


## Exercice 5 
def recherche_BOYER_MOORE(sequence, texte):
    dico = constru_dico(sequence)
    if len(sequence) > len(texte):
        return False
    curseur = len(sequence) - 1
    while curseur < len(texte):
        correspondance = True
        indice_sequence = len(sequence) - 1
        indice_texte = curseur
        while correspondance and indice_sequence > 0: #len(sequence) > indice_sequence #moins simple
            if texte[indice_texte] != sequence[indice_sequence]:
                correspondance = False
            else:
                indice_sequence = indice_sequence - 1
                indice_texte = indice_texte - 1
        if correspondance:
            return True
        if texte[curseur] in dico.keys():
            curseur = curseur + dico[texte[curseur]]
        else:
            curseur = curseur + len(sequence)
    return False

print(recherche_BOYER_MOORE("coucou","Bonjour, coucou!"))      