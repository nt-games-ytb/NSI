#Exercice 1
def delta(liste):
    resultat = []
    resultat.append(liste[0])
    for i in range(len(liste) - 1):
        valeur = liste[i] - liste[i + 1]
        resultat.append(-valeur) # ou juste faire resultat.append(-liste[i] - liste[i + 1])
    return resultat    

print("Exemple exercice 1 :")
print(delta([1000, 800, 802, 1000, 1003]))
print(delta([42]))
print()



#Exercice 2
class Noeud:
    '''
    classe implémentant un noeud d'arbre binaire
    '''

    def __init__(self, g, v, d):
        '''
        un objet Noeud possède 3 attributs :
        - gauche : le sous,
        - arbre gauche,-valeur : la valeur de l'étiquette,
        - droit : le sous-arbre droit.'''
        self.gauche = g
        self.valeur = v
        self.droit = d

    def __str__(self):
        '''
        renvoie la représentation du noeud en chaine de caractères
        '''
        return str(self.valeur)

    def est_une_feuille(self):
        '''
        renvoie True si et seulement si le noeud est une feuille
        '''
        return self.gauche is None and self.droit is None

def expression_infixe(e):
    s = ""
    if e.gauche is not None:
        s = '(' + s + expression_infixe(e.gauche)
    s = s + str(e.valeur)
    if e.droit is not None:
        s = s + expression_infixe(e.droit) +  ')'
    return s
    
print("Exemple exercice 2 :")
e = Noeud(Noeud(Noeud(None, 3, None),
    '*', Noeud(Noeud(None, 8, None), '+', Noeud(None, 7, None))),
    '-', Noeud(Noeud(None, 2, None), '+', Noeud(None, 1, None)))
print(expression_infixe(e))

#Dans l'exercice 1, nous fessons une fonction qui permet de soustraire un élément de la liste donné avec le prochain élément de la liste donné. Ainsi nous mettrons ce résultat dans une liste qui contiendra tout les résultats. la liste commence toujours par le premier élément de la liste donné et elle sera de même longueur que la liste donné. Voir les exemples et la correction