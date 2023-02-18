#------------EXERCICE 1---------------------------
#---------ajout d'une valeur dans un ABR----------
class ABR:
    def __init__(self, g0, v0, d0):
        self.gauche = g0
        self.cle = v0
        self.droit = d0

    def __repr__(self):
        if self is None:
            return ''
        else:
            return '(' + (self.gauche).__repr__() + ',' + str(self.cle) + ',' +(self.droit).__repr__() + ')'

n0 = ABR(None, 0, None)
n3 = ABR(None, 3, None)
n2 = ABR(None, 2, n3)
abr1 = ABR(n0, 1, n2)
    
def ajoute(cle, a):
    if cle < a.cle:
        if a.gauche == None:
            a.gauche = (None, cle, None)
        else:    
            ajoute(cle, a.gauche)
    elif cle > a.cle:
        if a.droit == None:
            a.droit = (None, cle, None)
        else:    
            ajoute(cle, a.droit)
    return a

def ajoute_test(cle, a):#marche pas car renvoie le dernier arbre
    if cle < a.cle:
        if a.gauche == None:
            a.gauche = (None, cle, None)
        else:    
            return ajoute_test(cle, a.gauche)
    elif cle > a.cle:
        if a.droit == None:
            a.droit = (None, cle, None)
        else:    
            return ajoute_test(cle, a.droit)
    return a

def ajoute_test_1(cle, a):#marche mais interdit car recréer un arbre
    if a == None:
        return ABR(None, cle, None)
    if cle < a.cle:
        return ABR(ajoute_test_1(cle, a.gauche), a.cle, a.droit)
    elif cle > a.cle:
        return ABR(a.gauche, a.cle, ajoute_test_1(cle, a.droit))
    else:
        return a
    
print("Exemple exercice 1 :")
print(abr1)
a = ajoute(4, abr1)
print(a)
print(ajoute(-5, abr1))
print(ajoute(2, abr1))
print()



#------------EXERCICE 2---------------------------
#-------algorithme glouton de mise en boite-------
def empaqueter(liste_masses, c):
    n = len(liste_masses) #8
    nb_boites = 0 #ou 1 si return sans +1
    boites = [0]*n #[0,0,0,0,0,0,0,0]
    for masse in liste_masses:
        i=0
        while i <= nb_boites and boites[i] + masse > c:
            i = i + 1
        if i == nb_boites + 1:
            nb_boites = nb_boites + 1
        boites[i] = boites[i] + masse
    return nb_boites + 1

print("Exemple exercice 2 :")
print(empaqueter([7, 6, 3, 4, 8, 5, 9, 2], 11))