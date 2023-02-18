#Exercice 1
def enumere(L):
    d = {}
    for i in range(len(L)):
        if L[i] in d:
            d[L[i]].append(i)
        else:
            d[L[i]] = [i]
    return d

print("Exemple exercice 1 :")
print(enumere([1, 1, 2, 3, 2, 1]))
print()



#Exerice 2
class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None

def parcours(arbre, liste):
    if arbre != None:
        parcours(arbre.fg, liste)
        liste.append(arbre.v)
        parcours(arbre.fd, liste)
    return liste

def insere(arbre, cle):
    """ arbre est une instance de la classe Arbre qui implémente
        un arbre binaire de recherche.
    """
    if arbre.v > cle:
        if arbre.fg != None:
            insere(arbre.fg, cle)
        else:
            arbre.fg = Arbre(cle)
    else:
        if arbre.fd != None:
            insere(arbre.fd, cle)
        else:
            arbre.fd = Arbre(cle)

print("Exemple exercice 2 :")
arbre_de_test = Arbre(5)
arbre_de_test.fg = Arbre(2)
arbre_de_test.fd = Arbre(7)
arbre_de_test.fg.fd = Arbre(3)
insere(arbre_de_test, 1)
insere(arbre_de_test, 4)
insere(arbre_de_test, 6)
insere(arbre_de_test, 8)