class Arbrebinaire:
    def __init__(self,valeur):
        self.valeur=valeur
        self.gauche=None
        self.droit=None
        
    def ajoutgauche(self,valeur):
        self.gauche = Arbrebinaire(valeur)
    
    def supprgauche(self):
        self.gauche=None
    
    def ajoutdroit(self,valeur):
        self.droit = Arbrebinaire(valeur)
        
    def supprdroit(self):
        self.droit=None


def taille(arbre):
    if arbre==None:
        return 0
    else:
        return 1+taille(arbre.gauche)+taille(arbre.droit)
        
def hauteur(arbre):
    if arbre==None:
        return 0
    else:
        return 1+max(hauteur(arbre.gauche),hauteur(arbre.droit))

def nb_feuille(arbre):
    if arbre==None:
        return 0
    elif arbre.gauche==None and arbre.droit==None:
            return 1
    else:
        return nb_feuille(arbre.gauche)+nb_feuille(arbre.droit)

def lecture_prefixe(arbre):
    if arbre == None:
        pass
    else:
        print(arbre.valeur)
        lecture_prefixe(arbre.gauche)
        lecture_prefixe(arbre.droit)

def lecture_infixe(arbre):
    if arbre == None:
        pass
    else:
        lecture_infixe(arbre.gauche)
        print(arbre.valeur)
        lecture_infixe(arbre.droit)

def lecture_postfixe(arbre):
    if arbre == None:
        pass
    else:
        lecture_postfixe(arbre.gauche)
        lecture_postfixe(arbre.droit)
        print(arbre.valeur)

def parcoursLargeur(arbre):
    if arbre == None:
        pass
    else:
        f=File()
        f.push(arbre)
        while f.nonvide():
            a=f.pop()
            if a!=None:
                print(a.valeur)
                f.push(a.gauche)
                f.push(a.droit)

class Pile:
    def __init__(self):
        self.tablo = []


    def push(self, data):
        self.tablo.append(data)


    def pop(self):
        return self.tablo.pop()

    def vide(self):
        if self.tablo==[]:
            return True
        else:
            return False

    def nonvide(self):
        if self.tablo!=[]:
            return True
        else:
            return False

class File:
    def __init__(self):
        self.stockage=[]
    
    def pousse(self,donnee):
        self.stockage.insert(0,donnee)
        
    def extraire(self):
        return self.stockage.pop()
        
    def vide(self):
        return self.stockage==[]
        
    def nonvide(self):
        return self.stockage!=[]

class tableau:
    def __init__(self,taille):
        self.taille=taille
        self.liste=[None] * taille
        
    def toutvide(self):
        for element in self.liste:
            if element !=None:
                return False
        return True
    
    def change(self,i,data):
        self.liste[i]=data
        
    def effacer(self,i):
        self.liste[i]=None
    
    def connaitre(self,i):
        return self.liste[i]
        
    def affiche_tout(self):
        print(self.liste)

