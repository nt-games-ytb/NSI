class File:
    
    def __init__(self):
        self.stockage=[]
        
    def push(self,data):
        self.stockage.insert(0,data)
        
    def pop(self):
        return self.stockage.pop()
        
    def vide(self):
        return self.stockage==[]
    
    def nonvide(self):
        return self.stockage!=[]
        

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


class Tableau:
    def __init__(self,taille):
        self.taille=taille
        self.tablo=[None]*taille
        
    def toutvide(self):
        for element in self.tablo:
            if element!=None:
                return False
        return True
        
    def change(self,i,data):
        self.tablo[i]=data
        
    def effacer(self,i):
        self.tablo[i]=None
        
    def connaitre(self,i):
        return self.tablo[i]
        
    def affichetout(self):
        return self.tablo
        
        
class Arbre_Binaire:
    
    def __init__(self,valeur):
        self.valeur=valeur
        self.gauche=None
        self.droit=None

    def ajout_gauche(self,valeur):
        self.gauche=Arbre_Binaire(valeur)
        
    def suppr_gauche(self):
        self.gauche=None
        
    def ajout_droit(self,valeur):
        self.droit=Arbre_Binaire(valeur)
        
    def suppr_droit(self):
        self.droit=None
        
        
def taille_class(arbre):
    if arbre==None:
        return 0
    else:
        return 1+taille_class(arbre.gauche)+taille_class(arbre.droit)
        
def hauteur_class(arbre):
    if arbre==None:
        return 0
    else:
        return 1+max(hauteur_class(arbre.gauche),hauteur_class(arbre.droit))
    
def nombre_feuille_class(arbre):
    if arbre==None:
        return 0
    elif arbre.gauche==None and arbre.droit==None:
        return 1
    else:
        return nombre_feuille_class(arbre.gauche)+nombre_feuille_class(arbre.droit)

def lecture_prefixe_class(arbre):
    if arbre!=None:
        print(arbre.valeur)
        lecture_prefixe_class(arbre.gauche)
        lecture_prefixe_class(arbre.droit)
        
def lecture_infixe_class(arbre):
    if arbre!=None:
        lecture_infixe_class(arbre.gauche)
        print(arbre.valeur)
        lecture_infixe_class(arbre.droit)
        
def lecture_postfixe_class(arbre):
    if arbre!=None:
        lecture_postfixe_class(arbre.gauche)
        lecture_postfixe_class(arbre.droit)
        print(arbre.valeur)


def recherche_valeur(arbre,data):
    if arbre==None:
        return False
    elif arbre.valeur==data:
        return True
    elif data<arbre.valeur:
        return recherche_valeur(arbre.gauche,data)
    else:
        return recherche_valeur(arbre.droit,data)
        
        
def ajout_valeur(arbre,data2):
    if arbre!=None:
        if recherche_valeur(arbre,data2)==True:
            return("La valeur est deja dans l'arbre")
        else:
            if data2<arbre.valeur:
                if arbre.gauche==None:
                    arbre.ajout_gauche(data2)
                else:
                    ajout_valeur(arbre.gauche,data2)
            else:
                if arbre.droit==None:
                    arbre.ajout_droit(data2)
                else:
                    ajout_valeur(arbre.droit,data2)


def crea_arbre_recherche_opti_BADLONG(liste):
    liste.sort() #tri la liste
    md=len(liste)//2 #md est la medianne de la liste
    arbre_sortie=Arbre_Binaire(liste[md]) #on creer un arbre dont la racine est md
    file=File()
    file.push(liste[:md])
    file.push(liste[md+1:])
    while file.nonvide():
        a=file.pop()
        if a==[]:
            pass
        if len(a)==1:
            ajout_valeur(arbre_sortie,a[0])
        elif len(a)==2:
            ajout_valeur(arbre_sortie,a[0])
            ajout_valeur(arbre_sortie,a[1])
        else:
            md=len(a)//2
            ajout_valeur(arbre_sortie,a[md])
            file.push(a[:md])
            file.push(a[md+1:])
    return arbre_sortie