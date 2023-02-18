#Exercice 1

print("Exemple exercice 1 :")
a=Arbre(1)
a.fg=Arbre(4)
a.fd=Arbre(0)
a.fd.fd=Arbre(7)
print(a)
print()



#Exerice 2
def ajoute(indice, element, liste):
    nbre_elts = len(liste)
    L = [0 for i in range(nbre_elts + 1)]
    if ...:
        for i in range(indice):
            L[i] = ...
        L[...] = ...
        for i in range(indice + 1, nbre_elts + 1):
            L[i] = ...
    else:
        for i in range(nbre_elts):
            L[i] = ...
        L[...] = ...
    return L

print("Exemple exercice 2 :")
print(ajoute(1, 4, [7, 8, 9]))
print(ajoute(3, 4, [7, 8, 9]))
print(ajoute(4, 4, [7, 8, 9]))