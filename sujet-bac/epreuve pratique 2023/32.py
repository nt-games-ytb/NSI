#Exercice 1
def min_et_max(tab):
    '''
    Fonction qui prend en paramètre tab, un tableau non-vide de nombres et
    qui parcours le tableau pour trouver le plus petit nombre et le plus grand nombre
    pour ainsi le renvoyer dans un dictionnaire à deux clés : "min" et "max"
    '''
    assert tab != [], "Le tableaux ne doit pas être vide !"
    resultat = {"min": tab[0], "max": tab[0]}
    for element in tab:
        if resultat["min"] > element:
            resultat["min"] = element
        if resultat["max"] < element:
            resultat["max"] = element
    return resultat

print("Exemple exercice 1 :")
print(min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]))
print(min_et_max([0, 1, 2, 3]))
print(min_et_max([3]))
print(min_et_max([1, 3, 2, 1, 3]))
print(min_et_max([-1, -1, -1, -1, -1]))
print()



#Exerice 2
class Carte:
    def __init__(self, c, v):
        """ Initialise les attributs couleur (entre 1 et 4), et valeur (entre 1 et 13). """
        self.couleur = c
        self.valeur = v

    def get_valeur(self):
        """ Renvoie la valeur de la carte : As, 2, ..., 10, Valet, Dame, Roi """
        valeurs = ['As','2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi']
        return valeurs[self.valeur - 1]

    def get_couleur(self):
        """ Renvoie la couleur de la carte (parmi pique, coeur, carreau, tréfle). """
        couleurs = ['pique', 'coeur', 'carreau', 'tréfle']
        return couleurs[self.couleur - 1]

class Paquet_de_cartes:
    def __init__(self):
        """ Initialise l'attribut contenu avec une liste des 52 objets Carte possibles
            rangés par valeurs croissantes en commençant par pique, puis coeur,
            carreau et tréfle. """
        self.paquet = []
        for couleur in range(4):
            for valeur in range(13):
                self.paquet.append(Carte(couleur + 1, valeur + 1))
    def get_carte(self, pos):
        """ Renvoie la carte qui se trouve à la position pos (entier compris entre 0 et 51). """
        assert pos >= 0, "La position est trop basse !"
        assert pos <= 51, "La position est trop haute !" 
        return self.paquet[pos]

print("Exemple exercice 2 :")
jeu = Paquet_de_cartes()
carte1 = jeu.get_carte(20)
print(carte1.get_valeur()+ " de " + carte1.get_couleur())
carte2 = jeu.get_carte(0)
print(carte2.get_valeur()+ " de " + carte2.get_couleur())
carte3 = jeu.get_carte(52)