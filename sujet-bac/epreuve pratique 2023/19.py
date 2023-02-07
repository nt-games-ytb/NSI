#Exercice 1
def recherche_sans_dichotomie(tab, n):
    indice = -1
    for i in range(len(tab)):
        if tab[i] == n:
            indice = i
    return indice
    
def recherche(tab, n):
    indice_debut = 0
    indice_fin = len(tab) - 1
    while indice_debut <= indice_fin:
        indice_milieu = (indice_debut + indice_fin) // 2
        if tab[indice_milieu] == n:
            return indice_milieu
        elif tab[indice_milieu] < n:
            indice_debut = indice_milieu + 1
        else:
            indice_fin = indice_milieu - 1
    return -1
    
print("Exemple exercice 1 :")
print(recherche([2, 3, 4, 5, 6], 5))
print(recherche([2, 3, 4, 6, 7], 5))
print()



#Exercice 2
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def position_alphabet(lettre):
    return ord(lettre) - ord('A')
def cesar(message, decalage):
    resultat = ''
    for ... in message:
        if 'A' <= c and c <= 'Z':
            indice = ( ... ) % 26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = ...
    return resultat

print("Exemple exercice 2 :")
print(cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4))
print(cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5))
