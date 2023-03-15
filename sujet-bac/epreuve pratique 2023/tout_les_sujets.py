#Ordre : 18,43,44,13,12,5,19,20,8,10,32,4,16,40,23,31,2,42,37,39



#Sujet 18 - 17h25

## Exercice 1 - de 17h25 à 17h29
def max_et_indice(tab):
    max = tab[0]
    indice_max = 0
    for i in range(len(tab)):
        if tab[i] > max:
            max = tab[i]
            indice_max = i
    return (max, indice_max)

print(max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))
print(max_et_indice([-2]))
print(max_et_indice([-1, -1, 3, 3, 3]))
print(max_et_indice([1, 1, 1, 1]))

## Exercice 2 - de 15h29 à 15h50
def est_un_ordre(tab):
    '''
    Renvoie True si tab est de longueur n et contient tous les entiers
    de 1 à n, False sinon
    '''
    for i in range(1, len(tab)):
        if tab[i] > len(tab):
            return False
    return True


def nombre_points_rupture(ordre):
    '''
    Renvoie le nombre de point de rupture de ordre qui représente un ordre
    de gènes de chromosome
    '''
    assert est_un_ordre(ordre) # ordre n'est pas un ordre de gènes
    n = len(ordre)
    nb = 0
    if ordre[0] != 1: # le premier n'est pas 1
        nb = nb + 1
    i = 0
    while i < n - 1:
        if ordre[i] - ordre[i + 1] not in [-1, 1]: # l'écart n'est pas 1
            nb = nb + 1
        i = i + 1
    if ordre[-1] != n: # le dernier n'est pas n
        nb = nb + 1
    return nb
    
print(est_un_ordre([1, 6, 2, 8, 3, 7]))
print(est_un_ordre([5, 4, 3, 6, 7, 2, 1, 8, 9]))
print(nombre_points_rupture([5, 4, 3, 6, 7, 2, 1, 8, 9]))
print(nombre_points_rupture([1, 2, 3, 4, 5]))
print(nombre_points_rupture([1, 6, 2, 8, 3, 7, 4, 5]))
print(nombre_points_rupture([2, 1, 3, 4]))



# Sujet 43 - 16h06

## Exercice 1 - de 16h13 à 16h27
def ecriture_binaire_entier_positif(n):
    resultat = []
    if n == 0:
        resultat = [0]
    while n != 0:
        b = n%2
        n = n//2
        resultat.append(b)
    resultat.reverse()
    return resultat

print(ecriture_binaire_entier_positif(0))
print(ecriture_binaire_entier_positif(2))
print(ecriture_binaire_entier_positif(105))

## Exercice 2 - de 16h06 à 16h12 (grâce à ma mémoire)
def tri_bulles(T):
    '''
	Renvoie le tableau T trié par ordre croissant
	'''
    n = len(T)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if T[j] > T[j + 1]:
                temp = T[j]
                T[j] = T[j + 1]
                T[j+1] = temp
    return T
    
print(tri_bulles([]))
print(tri_bulles([7]))
print(tri_bulles([9, 3, 7, 2, 3, 1, 6]))
print(tri_bulles([9, 7, 4, 3]))



# Sujet 44 - 16h27

## Exercice 1 - de 16h27 à 16h29
def renverse(mot):
    resultat = ""
    for c in mot:
        resultat = c + resultat
    return resultat
    
print(renverse("informatique"))

## Exercice 2 - de 16h30 à 16h36 (grâce à ma mémoire)
def crible(n):
    """
    Renvoie un tableau contenant tous les nombres premiers plus petits
    que n
    """
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(2, n):
        if tab[i] == True:
            premiers.append(i)
            for multiple in range(2 * i, n, i):
                tab[multiple] = False
    return premiers

print(crible(40))



# Sujet 13 - 16h37

## Exercice 1 - de 16h37 à 16h41
def recherche(a, tab):
    occurence = 0
    for element in tab:
        if element == a:
            occurence = occurence + 1
    return occurence
    
print(recherche(5, []))
print(recherche(5, [-2 , 3, 4, 8]))
print(recherche(5, [-2, 3, 1, 5, 3, 7, 4]))
print(recherche(5, [-2, 5, 3, 5, 4, 5]))

## Exercice 2 - de 16h47 à 16h54
pieces = [1, 2, 5, 10, 20, 50, 100, 200]

def rendu_monnaie(somme_due, somme_versee):

    rendu = []
    a_rendre = somme_versee - somme_due
    i = len(pieces) - 1
    while a_rendre != 0 :
        if pieces[i] <= a_rendre :
            rendu.append(pieces[i])
            a_rendre = a_rendre - pieces[i]
        else :
            i = i - 1
    return rendu
    
print(rendu_monnaie(700, 700))
print(rendu_monnaie(102, 500))



# Sujet 12 - 16h55

## Exercice 1 - de 16h55 à 17h15 (galérer)
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
    if a is None:
        return ABR(None, cle, None)
    elif cle == a.cle:
        return a
    elif cle < a.cle:
        return ABR(ajoute(cle, a.gauche), a.cle, a.droit)
    else:
        return ABR(a.gauche, a.cle, ajoute(cle, a.droit))
    
n0 = ABR(None, 0, None)
n3 = ABR(None, 3, None)
n2 = ABR(None, 2, n3)
abr1 = ABR(n0, 1, n2)
print(abr1)
a = ajoute(4, abr1)
print(a)
print(ajoute(-5, abr1))
print(ajoute(2, abr1))

## Exercice 2 - de 11h30 à 11h41
def empaqueter(liste_masses, c):
    n = len(liste_masses)
    nb_boites = 0
    boites = [0]*n
    for masse in liste_masses:
        i=0
        while i <= nb_boites and boites[i] + masse > c:
            i = i + 1
        if i == nb_boites + 1:
            nb_boites = nb_boites + 1
        boites[i] = boites[i] + masse
    return nb_boites + 1
    
print(empaqueter([7, 6, 3, 4, 8, 5, 9, 2], 11))



# Sujet 5 - 11h42

## Exercice 1 - de 11h42 à 11h56
import random

def lancer(n):
    resultat = []
    for i in range(n):
        resultat.append(random.randint(1,6))
    return resultat

def paire_6(tab):
    nb_6 = 0
    for element in tab:
        if element == 6:
            nb_6 = nb_6 + 1
    if nb_6 >= 2:
        return True
    else:
        return False
    
lancer1 = lancer(5)
print(lancer1)
print(paire_6(lancer1))
lancer2 = lancer(5)
print(lancer2)
print(paire_6(lancer2))
lancer3 = lancer(3)
print(lancer3)
print(paire_6(lancer3))
lancer4 = lancer(0)
print(lancer4)
print(paire_6(lancer4))

## Exercice 2 - de 11h58 à 12h03
img=[[20, 34, 254, 145, 6], [23, 124, 237, 225, 69], [197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]

def nbLig(image):
    '''renvoie le nombre de lignes de l'image'''
    return len(image)

def nbCol(image):
    '''renvoie la largeur de l'image'''
    return len(image[0])

def negatif(image):
    '''renvoie le negatif de l'image sous la forme
       d'une liste de listes'''

    # on cree une image de 0 aux memes dimensions que le parametre image
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]

    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            L[i][j] = 255 - L[i][j]
    return L

def binaire(image, seuil):
    '''renvoie une image binarisee de l'image sous la forme
       d'une liste de listes contenant des 0 si la valeur
       du pixel est strictement inferieure au seuil
       et 1 sinon'''

    # on cree une image de 0 aux memes dimensions que le parametre image
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]

    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            if image[i][j] < seuil :
                L[i][j] = 0
            else:
                L[i][j] = 1
    return L

print(nbLig(img))
print(nbCol(img))
print(negatif(img))
print(binaire(img,120))



# Sujet 19 - 9h26

## Exercice 1 - de 9h26 à 9h29
def recherche(tab, n):
    indice = -1
    for i in range(len(tab)):
        if tab[i] == n:
            indice = i
    return indice
    
print(recherche([2, 3, 4, 5, 6], 5))
print(recherche([2, 3, 4, 6, 7], 5))

##Exercice 2 - de 9h30 à 9h41
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ord(lettre) - ord('A')
    
def cesar(message, decalage):
    resultat = ''
    for c in message:
        if 'A' <= c and c <= 'Z':
            indice = (position_alphabet(c)  + decalage) % 26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat + c
    return resultat

print(cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4))
print(cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5))



# Sujet 20 - 9h42

## Exercice 1 - de 9h43 à 9h48
def ajoute_dictionnaires(d1, d2):
    d = dict(d1)
    for element in d2:
        if element in d:
            d[element] = d[element] + d2[element]
        else:
            d[element] = d2[element]
    return d
    
print(ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}))
print(ajoute_dictionnaires({}, {2: 9, 3: 11}))
print(ajoute_dictionnaires({1: 5, 2: 7}, {}))

## Exercice 2 - de 9h49 à 
from random import randint

def nbre_coups():
    n = 0
    cases_vues = [0]
    case_en_cours = 0
    nbre_cases = 12
    while len(cases_vues) < ...:
        x = randint(1, 6)
        case_en_cours = (case_en_cours + x) % nbre_cases
        if ...:
            cases_vues.append(case_en_cours)
        n = n + 1
    return n
    
print(nbre_coups())