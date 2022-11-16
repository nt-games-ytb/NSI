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

calcul = ArbreBinaire("+")

calcul.ajoutgauche("x")
calcul.gauche.ajoutgauche(3)
calcul.gauche.ajoutdroit(2)

calcul.ajoutdroit("/")
calcul.droit.ajoutgauche(60)
calcul.droit.ajoutdroit("+")
calcul.droit.droit.ajoutgauche(4)
calcul.droit.droit.ajoutdroit(6)

#Question 1
def taille(arbreBinaire):
    if arbreBinaire == None:
        return 0
    else:
        return 1 + taille(arbreBinaire.gauche) + taille(arbreBinaire.droit)



#Exerice 32
liste_des_valeurs = []
def calcularbre(arbre):
    global liste_des_valeurs
    if arbre == None:
        pass
    else:
        calcularbre(arbre.gauche)
        liste_des_valeurs.append(arbre.valeur)
        calcularbre(arbre.droit)
    if taille(arbre) == len(liste_des_valeurs):
        while len(liste_des_valeurs) != 1:
            nombre1 = liste_des_valeurs[0]
            nombre2 = liste_des_valeurs[2]
            if liste_des_valeurs[1] == "+":
                resultat = nombre1 + nombre2
            if liste_des_valeurs[1] == "-":
                resultat = nombre1 - nombre2
            if liste_des_valeurs[1] == "x":
                resultat = nombre1 * nombre2
            if liste_des_valeurs[1] == "/":
                resultat = nombre1 / nombre2
            liste_des_valeurs.pop(-1)
            liste_des_valeurs.pop(-1)
            liste_des_valeurs.pop(-1)
            liste_des_valeurs = [resultat] + liste_des_valeurs
            print(liste_des_valeurs[0])
        return liste_des_valeurs[0] 

def evaluer(arbre):
    if arbre == None:
        pass
    elif arbre.valeur == "+":
        return evaluer(arbre.gauche) + evaluer(arbre.droit)   
    elif arbre.valeur == "-":
        return evaluer(arbre.gauche) - evaluer(arbre.droit)  
    elif arbre.valeur == "x":
        return evaluer(arbre.gauche) * evaluer(arbre.droit)   
    elif arbre.valeur == "/":
        return evaluer(arbre.gauche) / evaluer(arbre.droit)   