#Exercice 1
dico = {'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}

def max_dico(dico):
    meilleur_nom = ""#dico[0]
    meilleur_like = -1#dico[meilleur_nom]
    for nom in dico.keys():
        if dico[nom] > meilleur_like:
            meilleur_nom = nom
            meilleur_like = dico[nom]
    return (meilleur_nom, meilleur_like)



#Exercice 2
class Pile:
    """
    Classe definissant une structure de pile.
    """
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """
        Renvoie le booleen True si la pile est vide, False sinon.
        """
        return self.contenu == []

    def empiler(self, v):
        """
        Place l'element v au sommet de la pile
        """
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l'element place au sommet de la pile,
        si la pile n'est pas vide.
        """
        if not self.est_vide():
            return self.contenu.pop()


def eval_expression(tab):
    p = Pile()
    for element in tab:
        if element != '+' or element != '*':#nombre #jsp pk les or ne marchent pas
            p.empiler(element)
        else:#opérateur
            if element == "+":
                resultat = p.depiler() + p.depiler()
            else:
                resultat = p.depiler() * p.depiler()
            p.empiler(resultat)
    return p.depiler()