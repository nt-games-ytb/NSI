#Exercice 1
class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None

def taille(a):
    if a == None:
        return 0
    else:
        return 1 + taille(a.fg) + taille(a.fd)
    
def hauteur(a):
    if a == None:
        return 0
    else:
        return 1 + max(hauteur(a.fg), hauteur(a.fd))

print("Exemple exercice 1 :")
a1=Arbre(1)
a1.fg=Arbre(4)
a1.fd=Arbre(0)
a1.fd.fd=Arbre(7)
print(taille(a1))
print(hauteur(a1))
a2=Arbre(0)
a2.fg=Arbre(1)
a2.fd=Arbre(2)
a2.fg.fg=Arbre(3)
a2.fd.fg=Arbre(4)
a2.fd.fd=Arbre(5)
a2.fd.fg.fd=Arbre(6)
print(taille(a2))
print(hauteur(a2))
print()



#Exerice 2
def ajoute(indice, element, liste):
    nbre_elts = len(liste)
    L = [0 for i in range(nbre_elts + 1)]
    if indice < nbre_elts:
        for i in range(indice):
            L[i] = liste[i]
        L[indice] = element
        for i in range(indice + 1, nbre_elts + 1):
            L[i] = liste[i - 1]
    else:
        for i in range(nbre_elts):
            L[i] = liste[i]
        L[-1] = element #ou L[nbre_elts] = element
    return L

print("Exemple exercice 2 :")
print(ajoute(1, 4, [7, 8, 9]))
print(ajoute(3, 4, [7, 8, 9]))
print(ajoute(4, 4, [7, 8, 9]))