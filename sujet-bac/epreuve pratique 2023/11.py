#Exercice 1
def convertir(tab):
    """
    tab est un tableau d'entiers, dont les éléments sont 0 ou 1,
    et représentant un entier écrit en binaire.
    Renvoie l'écriture décimale de l'entier positif dont la
    représentation binaire est donnée par le tableau tab
    """
    if len(tab) == 1:
        return tab[0]
    resultat = 0
    tab_retourner = []
    for i in range(len(tab)):
        tab_retourner.append(tab.pop(-1))
    for j in range(len(tab_retourner)):
        if tab_retourner[j] == 1:
            resultat = resultat + 2**j
    return resultat
    
def prof_convertir(tab):
    exposant = len(tab) - 1
    somme = 0
    for binaire in tab:
        somme = binaire* 2**exposant
    return somme

print("Exemple exercice 1 :")
print(convertir([1, 0, 1, 0, 0, 1, 1]))
print(convertir([1, 0, 0, 0, 0, 0, 1, 0]))
print()



#Exercice 2
liste = [9, 5, 8, 4, 0, 2, 7, 1, 10, 3, 6]

def tri_insertion(tab):
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i]
        # la variable j sert à déterminer où placer la valeur à ranger
        j = i
        # tant qu'on a pas trouvé la place de l'élément à insérer
        # on décale les valeurs du tableau vers la droite
        while j > 0 and valeur_insertion < tab[j - 1]:
            tab[j] = tab[j-1]
            j = j - 1
        tab[j] = valeur_insertion

print("Exemple exercice 2 :")
tri_insertion(liste)
print(liste)