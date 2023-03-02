#Exercice 1
def nombre_de_mots(phrase):
    resultat = 0
    for c in phrase:
        if c in [".", " "]:
            resultat = resultat + 1
    return resultat

print("Exemple exercice 1 :")
print(nombre_de_mots('Cet exercice est simple.'))
print(nombre_de_mots('Le point d exclamation est separe !'))
print(nombre_de_mots('Combien de mots y a t il dans cette phrase ?'))
print(nombre_de_mots('Fin.'))
print()



#Exerice 2
class Noeud:
    def __init__(self, valeur):
        '''Méthode constructeur pour la classe Noeud. Paramètre d'entrée : valeur (int)'''
        self.valeur = valeur
        self.gauche = None
        self.droit = None
    def getValeur(self):
        '''Méthode accesseur pour obtenir la valeur du noeud Aucun paramètre en entrée'''
        return self.valeur
    def droitExiste(self):
        '''Méthode renvoyant True si le sous-arbre droit est non vide Aucun paramètre en entrée'''
        return (self.droit is not None)
    def gaucheExiste(self):
        '''Méthode renvoyant True si le sous-arbre gauche est non vide Aucun paramètre en entrée'''
        return (self.gauche is not None)
    def inserer(self, cle):
        '''Méthode d'insertion de clé dans un arbre binaire de recherche Paramètre d'entrée : cle (int)'''
        if cle < self.valeur : #ou self.getValeur()
            # on insère à gauche
            if self.gaucheExiste():
                # on descend à gauche et on recommence le test initial
                self.gauche.inserer(cle)
            else:
                # on crée un fils gauche
                self.gauche = Noeud(cle)
        elif cle > self.valeur: #ou self.getValeur()
            # on insère à droite
            if self.droitExiste():
                # on descend à droite et on recommence le test initial
                self.droit.inserer(cle)
            else:
                # on crée un fils droit
                self.droit = Noeud(cle)

print("Exemple exercice 2 :")
arbre = Noeud(7)
for cle in (3, 9, 1, 6):
    arbre.inserer(cle)
print(arbre.gauche.getValeur())
print(arbre.droit.getValeur())
print(arbre.gauche.gauche.getValeur())
print(arbre.gauche.droit.getValeur())
