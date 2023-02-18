#Exercice 1

print("Exemple exercice 1 :")
print(min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]))
print(min_et_max([0, 1, 2, 3]))
print(min_et_max([3]))
print(min_et_max([1, 3, 2, 1, 3])
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
        """ Renvoie la couleur de la carte (parmi pique, coeur, carreau, trÃ¨fle). """
        couleurs = ['pique', 'coeur', 'carreau', 'trÃ¨fle']
        return couleurs[self.couleur - 1]

class Paquet_de_cartes:
    def __init__(self):
        """ Initialise l'attribut contenu avec une liste des 52 objets Carte possibles
            rangÃ©s par valeurs croissantes en commenÃ§ant par pique, puis coeur,
            carreau et trÃ©fle. """
        # A complÃ©ter

    def get_carte(self, pos):
        """ Renvoie la carte qui se trouve Ã  la position pos (entier compris entre 0 et 51). """
        # A complÃ©ter

print("Exemple exercice 2 :")
jeu = Paquet_de_cartes()
carte1 = jeu.get_carte(20)
print(carte1.get_valeur()+ " de " + carte1.get_couleur())
carte2 = jeu.get_carte(0)
print(carte2.get_valeur()+ " de " + carte2.get_couleur())
carte3 = jeu.get_carte(52)