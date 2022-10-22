#region Arbre binaire
class ArbreBinaire:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droit = None
        
    def ajoutgauche(self, valeur):
        self.gauche = ArbreBinaire(valeur)
        
    def supprgauche(self):
        self.gauche = None
    
    def ajoutdroit(self, valeur):
        self.droit = ArbreBinaire(valeur)
        
    def supprdroit(self):
        self.droit = None
        
class File:
    def __init__(self):
        self.tablo = []

    def pousse(self, data):
        self.tablo = [data] + self.tablo

    def extraire(self):
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

def taille(arbreBinaire):
    if arbreBinaire == None:
        return 0
    else:
        return 1 + taille(arbreBinaire.gauche) + taille(arbreBinaire.droit)
        
def hauteur(arbreBinaire):
    if arbreBinaire == None:
        return 0
    else:
        return 1 + max(hauteur(arbreBinaire.gauche), hauteur(arbreBinaire.droit))

def nombrefeuille(arbreBinaire):
    if arbreBinaire == None:
        return 0
    elif arbreBinaire.gauche == None and arbreBinaire.droit == None:
        return 1
    else:
        return nombrefeuille(arbreBinaire.gauche) + nombrefeuille(arbreBinaire.droit)

def lectureprefixe(arbreBinaire):
    if arbreBinaire == None:
        pass
    else:
        print(arbreBinaire.valeur)
        lectureprefixe(arbreBinaire.gauche)
        lectureprefixe(arbreBinaire.droit)

def lectureinfixe(arbreBinaire):
    if arbreBinaire == None:
        pass
    else:
        lectureinfixe(arbreBinaire.gauche)
        print(arbreBinaire.valeur)
        lectureinfixe(arbreBinaire.droit)

def lecturepostfixe(arbreBinaire):
    if arbreBinaire == None:
        pass
    else:
        lecturepostfixe(arbreBinaire.gauche)
        lecturepostfixe(arbreBinaire.droit)
        print(arbreBinaire.valeur)
        
def parcourtLargeur(arbreBinaire):
    if arbreBinaire == None:
        pass
    else:
        FILE = File() 
        FILE.pousse(arbreBinaire)
        while FILE.nonvide() == True:
            abreSupprime = FILE.extraire()
            if abreSupprime != None:
                print(abreSupprime.valeur)
                FILE.pousse(abreSupprime.gauche)
                FILE.pousse(abreSupprime.droit)
#endregion



#Exercice 2
arbre_de_recherche = ArbreBinaire(65)

arbre_de_recherche.ajoutgauche(40)
arbre_de_recherche.gauche.ajoutgauche(30)
arbre_de_recherche.gauche.ajoutdroit(57)
arbre_de_recherche.gauche.gauche.ajoutgauche(25)
arbre_de_recherche.gauche.gauche.ajoutdroit(32)
arbre_de_recherche.gauche.droit.ajoutgauche(43)
arbre_de_recherche.gauche.droit.ajoutdroit(58)

arbre_de_recherche.ajoutdroit(70)
arbre_de_recherche.droit.ajoutgauche(68)
arbre_de_recherche.droit.ajoutdroit(103)
arbre_de_recherche.droit.gauche.ajoutgauche(63)
arbre_de_recherche.droit.gauche.ajoutdroit(69)
arbre_de_recherche.droit.droit.ajoutgauche(102)



#Exerice 4
resultat = False
def rechercheValeur(arbreBinaire, valeur):
    global resultat
    if arbreBinaire == None:
        pass
    elif arbreBinaire.valeur == valeur:
        resultat = True
    else:
        rechercheValeur(arbreBinaire.gauche, valeur)
        rechercheValeur(arbreBinaire.droit, valeur)
    return resultat
#print(rechercheValeur(arbre_de_recherche, 69))
        
        
        
#Exerice 5
def ajoutValeur(arbreBinaire, valeur):
    #region Pas obligatoire
    if arbreBinaire == None:
        pass
    elif rechercheValeur(arbreBinaire, valeur) == True:
        return "Valeur déjà présente !"
    #endregion
    else:
        if valeur < arbreBinaire.valeur:
            if arbreBinaire.gauche == None:
                arbreBinaire.gauche = ArbreBinaire(valeur)
                #return lectureprefixe(arbre_de_recherche)#du coup non
            else:
                ajoutValeur(arbreBinaire.gauche, valeur)
        elif valeur > arbreBinaire.valeur:
            if arbreBinaire.droit == None:
                arbreBinaire.droit = ArbreBinaire(valeur)
                #return lectureprefixe(arbre_de_recherche)
            else:
                ajoutValeur(arbreBinaire.droit, valeur)
#print(ajoutValeur(arbre_de_recherche, 80))
#print(rechercheValeur(arbre_de_recherche, 28))



#Exerice 6
def creaabrederecherche(une_liste):
    arbre_binaire = ArbreBinaire(une_liste[0])
    une_liste.pop(0)
    while une_liste != []:
        valeur_supprimé = une_liste.pop(0)
        #print(une_liste)
        ajoutValeur(arbre_binaire, valeur_supprimé)
    return arbre_binaire
#print(lectureprefixe(creaabrederecherche([65,40,30,57,25,32,43,58,70,68,103,63,69,102])))



#Exerice 8
def creaabrederecherche_optimise(une_liste):
    une_liste.sort()
    arbre_binaire = ArbreBinaire(une_liste[len(une_liste) // 2])
    une_liste.pop(len(une_liste) // 2)
    FILE = File() 
    for element in une_liste:
        valeur_supprimé = une_liste.pop(len(une_liste) // 2)
        FILE.pousse(valeur_supprimé)
    while FILE.tablo != []:
        valeur_supprimé = FILE.extraire
        ajoutValeur(arbre_binaire, valeur_supprimé)
    return arbre_binaire
    #return creaabrederecherche(une_liste)
print("Exerice 8:")
print(lectureprefixe(creaabrederecherche_optimise([65,40,30,57,25,32,43,58,70,68,103,63,69,102])))

def crea_abre_de_recherche_opti_prof(liste):
    liste.sort() #Trie la liste
    milieu = len(liste) // 2 #Milieu est l'indice de la médiane
    arbre_sortie = ArbreBinaire(liste[milieu]) #Crée un ArbreBinaire dont la racine est l'élément du milieu
    file = File() #On crée une file vide
    file.push(liste[:milieu]) #On met dans la file, la sous liste à gauche de la médiane (dont le sous arbre gauche)
    file.push(liste[milieu-1:]) #On met dans la file, la sous liste à droite de la médiane (dont le sous arbre droit)
    while file.non_vide():
        a = file.pop()
        if a == []:
            pass
        if len(a) == 1:
            ajoutValeur(arbre_sortie, a[0])
        elif len(a) == 2:
            ajoutValeur(arbre_sortie, a[0])
            ajoutValeur(arbre_sortie, a[1])
        else: