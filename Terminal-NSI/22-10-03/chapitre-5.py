arbre = ["Toto",
["Tantan", ["Titi", None, None], ["Tutu", None, None]],
["Tintin", ["Furfur", None, None], ["Teïteï", ["Tojtoj", None, None], ["Têtê", None, None]]]
]

#Exercice 19
#Question 1
def test_lectureprefixe_1(une_liste):
    for element in une_liste:
        #print(une_liste[0])
        if une_liste[1] != None:
            lectureprefixe(une_liste[1])
        if une_liste[2] != None:
            lectureprefixe(une_liste[2])
        else:
            print(une_liste[0])
        
def lectureprefixe_1(une_liste):
    if une_liste == None:
        pass
    else:
        print(une_liste[0])
        lectureprefixe(une_liste[1])
        lectureprefixe(une_liste[2])
        
#Question 2
def lectureinfixe_1(une_liste):
    if une_liste == None:
        pass
    else:
        lectureprefixe(une_liste[1])
        print(une_liste[0])
        lectureprefixe(une_liste[2])
        
#Question 3
def lecturepostfixe_1(une_liste):
    if une_liste == None:
        pass
    else:
        lectureprefixe(une_liste[1])
        lectureprefixe(une_liste[2])
        print(une_liste[0])



#Exerice 21
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
        self.droiy = None
        
mon_arbre = ArbreBinaire("Toto")

mon_arbre.ajoutgauche("Tantan")
mon_arbre.gauche.ajoutgauche("Titi")
mon_arbre.gauche.ajoutdroit("Tutu")

mon_arbre.ajoutdroit("Tintin")
mon_arbre.droit.ajoutgauche("Furfur")
mon_arbre.droit.ajoutdroit("Teïteï")
mon_arbre.droit.droit.ajoutgauche("Tojtoj")
mon_arbre.droit.droit.ajoutdroit("Têtê")



#Exerice 22
#Question 1
def taille(arbreBinaire):
    if arbreBinaire == None:
        return 0
    else:
        return 1 + taille(arbreBinaire.gauche) + taille(arbreBinaire.droit)
    
#Question 2
def hauteur(arbreBinaire):
    if arbreBinaire == None:
        return 0
    else:
        return 1 + max(hauteur(arbreBinaire.gauche), hauteur(arbreBinaire.droit))
        
#Question 3
def nombrefeuille(arbreBinaire):
    if arbreBinaire == None:
        return 0
    elif arbreBinaire.gauche == None and arbreBinaire.droit == None:
        return 1
    else:
        return nombrefeuille(arbreBinaire.gauche) + nombrefeuille(arbreBinaire.droit)

#Question 4
def lectureprefixe(arbreBinaire):
    if arbreBinaire == None:
        pass
    else:
        print(arbreBinaire.valeur)
        lectureprefixe(arbreBinaire.gauche)
        lectureprefixe(arbreBinaire.droit)
        
#Question 6
def lectureinfixe(arbreBinaire):
    if arbreBinaire == None:
        pass
    else:
        lectureinfixe(arbreBinaire.gauche)
        print(arbreBinaire.valeur)
        lectureinfixe(arbreBinaire.droit)
        
#Question 7
def lecturepostfixe(arbreBinaire):
    if arbreBinaire == None:
        pass
    else:
        lecturepostfixe(arbreBinaire.gauche)
        lecturepostfixe(arbreBinaire.droit)
        print(arbreBinaire.valeur)
        
        
        
#Exerice 26
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

def test_parcourtLargeur(arbreBinaire):
    if arbreBinaire == None:
        pass
    else:
        FILE = File() 
        FILE.pousse(arbreBinaire)
        while FILE.nonvide() == True:
            abreSupprime = FILE.extraire()
            if abreSupprime == None:
                pass
            print(abreSupprime.valeur)
            FILE.pousse(abreSupprime.gauche)
            FILE.pousse(abreSupprime.droit)

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

print("Lecture préfixe :")
lectureprefixe(mon_arbre)
print("\nLecture infixe :")
lectureinfixe(mon_arbre)
print("\nLecture postfixe :")
lecturepostfixe(mon_arbre)
print("\nLecture en largeur :")
parcourtLargeur(mon_arbre)



#Exerice 29
calcul = ArbreBinaire("+")

calcul.ajoutgauche("x")
calcul.gauche.ajoutgauche("3")
calcul.gauche.ajoutdroit("2")

calcul.ajoutdroit("/")
calcul.droit.ajoutgauche("60")
calcul.droit.ajoutdroit("+")
calcul.droit.droit.ajoutgauche("4")
calcul.droit.droit.ajoutdroit("6")

print("\nLecture préfixe :")
lectureprefixe(calcul)
print("\nLecture infixe :")
lectureinfixe(calcul)
print("\nLecture postfixe :")
lecturepostfixe(calcul)