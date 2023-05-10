#Ordre : 18,43,44,13,12,5,19,20,8,10,32,4,16,40,23,31,2,42,37,39,30,25,11,21,35,45,9,28,26,24,27,1,22,41,34, |
3,38,7,29,6,14,33,36,17,15



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
def recherche_1(a, tab):
    occurence = 0
    for element in tab:
        if element == a:
            occurence = occurence + 1
    return occurence

print(recherche_1(5, []))
print(recherche_1(5, [-2 , 3, 4, 8]))
print(recherche_1(5, [-2, 3, 1, 5, 3, 7, 4]))
print(recherche_1(5, [-2, 5, 3, 5, 4, 5]))

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
def recherche_2(tab, n):
    indice = -1
    for i in range(len(tab)):
        if tab[i] == n:
            indice = i
    return indice

print(recherche_2([2, 3, 4, 5, 6], 5))
print(recherche_2([2, 3, 4, 6, 7], 5))

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

## Exercice 2 - de 10h26 à 10h32
from random import randint

def nbre_coups():
    n = 0
    cases_vues = [0]
    case_en_cours = 0
    nbre_cases = 12
    while len(cases_vues) < nbre_cases:
        x = randint(1, 6)
        case_en_cours = (case_en_cours + x) % nbre_cases
        if case_en_cours not in cases_vues:
            cases_vues.append(case_en_cours)
        n = n + 1
    return n

print(nbre_coups())



# Sujet 8

## Exercice 1 - de 10h33 à 10h44
def max_dico(dico):
    personne = ""
    like = 0
    for cle,valeur in dico.items():
        if valeur > like:
            personne = cle
            like = valeur
    return (personne, like)

print(max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}))
print(max_dico({'Alan': 222, 'Ada': 201, 'Eve': 220, 'Tim': 50}))

## Exercice 2 - de 10h45 à 10h57
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
        if element != '+' and element != '*':
            p.empiler(element)
        else:
            if element == "+":
                resultat = p.depiler() + p.depiler()
            else:
                resultat = p.depiler() * p.depiler()
            p.empiler(resultat)
    return p.depiler()

print(eval_expression([2, 3, '+', 5, '*']))



# Sujet 10

## Exercice 1 - de 10h59 à 11h00
def maxliste(tab):
    max = tab[0]
    for element in tab:
        if max < element:
            max = element
    return max

print(maxliste([98, 12, 104, 23, 131, 9]))
print(maxliste([-27, 24, -3, 15]))

## Exercice 2 - de 11h03 à 11h19
class Pile_2:
    """
    Classe definissant une pile
    """
    def __init__(self):
        self.valeurs = []

    def est_vide(self):
        """
        Renvoie True si la pile est vide, False sinon
        """
        return self.valeurs == []

    def empiler(self, c):
        """
        Place l'element c au sommet de la pile
        """
        self.valeurs.append(c)

    def depiler(self):
        """
        Supprime l'element place au sommet de la pile, a condition qu'elle soit non vide
        """
        if self.est_vide() == False:
            self.valeurs.pop()

def parenthesage(ch):
    """
    Renvoie True si la chaine ch est bien parenthesee et False sinon
    """
    p = Pile_2()
    for c in ch:
        if c == "(":
            p.empiler(c)
        elif c == ")":
            if p.est_vide():
                return False
            else:
                p.depiler()
    return p.est_vide()

print(parenthesage("((()())(()))"))
print(parenthesage("())(()"))
print(parenthesage("(())(()"))



# Sujet 32

## Exercice 1 - de 11h20 à 11h30
def min_et_max(tab):
    resultat = {'min': tab[0], 'max':tab[0]}
    for element in tab:
        if element < resultat['min']:
            resultat['min'] = element
        elif element > resultat['max']:
            resultat['max'] = element
    return resultat

print(min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]))
print(min_et_max([0, 1, 2, 3]))
print(min_et_max([3]))
print(min_et_max([1, 3, 2, 1, 3]))
print(min_et_max([-1, -1, -1, -1, -1]))

## Exercice 2 - de 11h30 à 11h54
class Carte:
    def __init__(self, c, v):
        """ Initialise les attributs couleur (entre 1 et 4), et valeur (entre 1 et 13). """
        self.couleur = c
        self.valeur = v

    def get_valeur(self):
        """ Renvoie la valeur de la carte : As, 2, ..., 10, Valet, Dame, Roi """
        valeurs = ['As','2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi']
        return valeurs[self.valeur - 1]

    def get_couleur(self):
        """ Renvoie la couleur de la carte (parmi pique, coeur, carreau, trÃ¨fle). """
        couleurs = ['pique', 'coeur', 'carreau', 'trèle']
        return couleurs[self.couleur - 1]

class Paquet_de_cartes:
    def __init__(self):
        """ Initialise l'attribut contenu avec une liste des 52 objets Carte possibles
            rangÃ©s par valeurs croissantes en commenÃ§ant par pique, puis coeur,
            carreau et trèfle. """
        self.contenu = []
        for i in range(4):
            for j in range(13):
                self.contenu.append(Carte(i + 1,j + 1))

    def get_carte(self, pos):
        """ Renvoie la carte qui se trouve Ã  la position pos (entier compris entre 0 et 51). """
        assert type(pos) == int, "paramètre pos invalide"
        assert pos >= 0, "paramètre pos invalide"
        assert pos <= 51, "paramètre pos invalide"
        return self.contenu[pos]

jeu = Paquet_de_cartes()
carte1 = jeu.get_carte(20)
print(carte1.get_valeur() + " de " + carte1.get_couleur())
carte2 = jeu.get_carte(0)
print(carte2.get_valeur() + " de " + carte2.get_couleur())
#carte3 = jeu.get_carte(52)



# Sujet 4

## Exercice 1 - de 11h54 à 12h00
def a_doublon(liste):
    liste_elements = []
    for element in liste:
        if element in liste_elements:
            return True
        else:
            liste_elements.append(element)
    return False

print(a_doublon([]))
print(a_doublon([1]))
print(a_doublon([1, 2, 4, 6, 6]))
print(a_doublon([2, 5, 7, 7, 7, 9]))
print(a_doublon([0, 2, 3]))

## Exercice 2 - de 12h00 à 12h05
def voisinage(n, ligne, colonne):
    """Renvoie la liste des coordonnées des voisins de la case
    (colonne) en gérant les cases sur les bords."""
    voisins = []
    for l in range(max(0,ligne-1), min(n, ligne+2)):
        for c in range(max(0, colonne-1), min(n, colonne+2)):
            if (l, c) != (ligne, colonne):
                voisins.append((l,c))
    return voisins

def incremente_voisins(grille, ligne, colonne):
    """Incrémente de 1 toutes les cases voisines d'une bombe."""
    voisins = ...
    for l, c in voisins:
        if grille[l][c] != -1:
            grille[l][c] = grille[l][c] + 1

def genere_grille(bombes):
    n = len(bombes)
    grille = [[0 for colonne in range(n)] for ligne in range(n)]
    for ligne, colonne in bombes:
        grille[ligne][colonne] = -1
        incremente_voisins(grille, ligne, colonne)
    return grille



# Sujet 16

## Exercice 1 - de 8h10 à
def recherche_indices_classement(elt, tab):
    inferieur = []
    egal = []
    superieur = []
    for i in range(len(tab)):
        if elt == tab[i]:
            egal.append(i)
        elif elt < tab[i]:
            superieur.append(i)
        elif elt > tab[i]:
            inferieur.append(i)
    return (inferieur, egal, superieur)

print(recherche_indices_classement(3, [1, 3, 4, 2, 4, 6, 3, 0]))
print(recherche_indices_classement(3, [1, 4, 2, 4, 6, 0]))
print(recherche_indices_classement(3, [1, 1, 1, 1]))
print(recherche_indices_classement(3, []))

## Exercice 2 - de  à 8h24
resultats = {'Dupont': {
                           'DS1': [15.5, 4],
                           'DM1': [14.5, 1],
                           'DS2': [13, 4],
                           'PROJET1': [16, 3],
                           'DS3': [14, 4]
                       },
             'Durand': {
                           'DS1': [6 , 4],
                           'DM1': [14.5, 1],
                           'DS2': [8, 4],
                           'PROJET1': [9, 3],
                           'IE1': [7, 2],
                           'DS3': [8, 4],
                           'DS4':[15, 4]
                       }
            }

def moyenne_1(nom, dico_result):
    if nom in dico_result.keys():
        notes = dico_result[nom]
        total_points = 0
        total_coefficients = 0
        for valeurs  in notes.values():
            note, coefficient = valeurs
            total_points = total_points + note * coefficient
            total_coefficients = total_coefficients + coefficient
        return round(total_points / total_coefficients, 1 )
    else:
        return -1

print(moyenne_1("Durand", resultats))



# Sujet 40

## Exercice 1 - de 8h25 à 8h30
def nombre_de_mots(phrase):
    nb_mots = 0
    for element in phrase:
        if element == "!" or element == "?":
            return nb_mots
        elif element == " " or element == ".":
            nb_mots = nb_mots + 1
    return nb_mots

print(nombre_de_mots('Cet exercice est simple.'))
print(nombre_de_mots('Le point d exclamation est separe !'))
print(nombre_de_mots('Combien de mots y a t il dans cette phrase ?'))
print(nombre_de_mots('Fin.'))

## Exercice 2 - de 8h30 à
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
        if cle < self.valeur:
            # on insère à gauche
            if self.gaucheExiste():
                # on descend à gauche et on recommence le test initial
                self.gauche.inserer(cle)
            else:
                # on crée un fils gauche
                self.gauche = Noeud(cle)
        elif cle > self.valeur:
            # on insère à droite
            if self.droitExiste():
                # on descend à droite et on recommence le test initial
                self.droit.inserer(cle)
            else:
                # on crée un fils droit
                self.droit = Noeud(cle)

arbre = Noeud(7)
for cle in (3, 9, 1, 6):
    arbre.inserer(cle)
print(arbre.gauche.getValeur())
print(arbre.droit.getValeur())
print(arbre.gauche.gauche.getValeur())
print(arbre.gauche.droit.getValeur())



# Sujet 23

## Exercice 1 - de 8h40 à 8h46
animaux = [ {'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2},
{'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5},
{'nom':'Tom', 'espece':'chat', 'age':7, 'enclos':4},
{'nom':'Belle', 'espece':'chien', 'age':6, 'enclos':3},
{'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]

def selection_enclos(table_animaux, num_enclos):
    resultat = []
    for element in table_animaux:
        if element['enclos'] == num_enclos:
            resultat.append(element)
    return resultat

print(selection_enclos(animaux, 5))
print(selection_enclos(animaux, 2))
print(selection_enclos(animaux, 7))

## Exercice 2 - de 8h48 à 9h01
tab_a = [3, 3, 3, 9, 9, 9, 1, 1, 1, 7, 2, 2, 2, 4, 4, 4, 8, 8, 8, 5, 5, 5]

tab_b = [8, 5, 5, 5, 9, 9, 9, 18, 18, 18, 3, 3, 3]

tab_c = [5, 5, 5, 1, 1, 1, 0, 0, 0, 6, 6, 6, 3, 8, 8, 8]

def trouver_intrus(tab, g, d):
    '''
    Renvoie la valeur de l'intrus situe entre les indices g et d
    dans la liste tab ou :
        tab verifie les conditions de l'exercice,
        g et d sont des multiples de 3.
    '''
    if g == d:
        return tab[g]

    else:
        nombre_de_triplets = (d - g)// 3
        indice = g + 3 * (nombre_de_triplets // 2)
        if tab[indice] == tab[indice + 1]:
            return trouver_intrus(tab, indice + 3, d)
        else:
            return trouver_intrus(tab, g, indice)

print(trouver_intrus([3, 3, 3, 9, 9, 9, 1, 1, 1, 7, 2, 2, 2, 4, 4, 4, 8, 8, 8, 5, 5, 5], 0, 21))
print(trouver_intrus([8, 5, 5, 5, 9, 9, 9, 18, 18, 18, 3, 3, 3], 0, 12))
print(trouver_intrus([5, 5, 5, 1, 1, 1, 0, 0, 0, 6, 6, 6, 3, 8, 8, 8], 0, 15))



# Sujet 31

## Exercice 1 - de 9h05 à 9h08
def nb_repetitions(elt, tab):
    repetitions = 0
    for element in tab:
        if element == elt:
            repetitions = repetitions + 1
    return repetitions

print(nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5]))
print(nb_repetitions('A', [ 'B', 'A', 'B', 'A', 'R']))
print(nb_repetitions(12, [1, '! ', 7, 21, 36, 44]))

## Exercice 2 - de 9h09 de 9h18
def binaire_2(a):
    bin_a = str(a%2)
    a = a // 2
    while a != 0:
        bin_a = str(a%2) + bin_a
        a = a//2
    return bin_a

print(binaire_2(0))
print(binaire_2(77))



# Sujet 2

## Exercice 1 - de 9h19 à 9h25
def indices_maxi(tab):
    max = tab[0]
    indice_occurence = [0]
    for i in range(1, len(tab)):
        if max == tab[i]:
            indice_occurence.append(i)
        elif max < tab[i]:
            max = tab[i]
            indice_occurence = [i]
    return (max, indice_occurence)


print(indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))
print(indices_maxi([7]))

## Exercice 2 - de 9h26 à 9h30
def positif(pile):
    pile_1 = list(pile)
    pile_2 = []
    while pile_1 != []:
        x = pile_1.pop()
        if x >= 0:
            pile_2.append(x)
    while pile_2 != []:
        x = pile_2.pop()
        pile_1.append(x)
    return pile_1

print(positif([-1, 0, 5, -3, 4, -6, 10, 9, -8]))
print(positif([-2]))



# Sujet 42

## Exercice 1 - de 9h31 à 9h45
def tri_selection(tab): # pas sur sur que ce soit un tri par selection mais je l'ai fais sans tricher
    for i in range(len(tab)):
        minimum = tab[i]
        indice_minimum = i
        for j in range(i + 1, len(tab)):
            if minimum > tab[j]:
                minimum = tab[j]
                indice_minimum = j
        tab[i], tab[indice_minimum] = minimum, tab[i]
    return tab

print(tri_selection([1, 52, 6, -9, 12]))

## Exercice 2 - de 9h53 à
from random import randint

def plus_ou_moins():
    nb_mystere = randint(1, 99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 0

    while nb_mystere != nb_test and compteur < 9:
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print("Bravo ! Le nombre etait ", nb_mystere)
        print("Nombre d'essais: ", compteur)
    else:
        print("Perdu ! Le nombre etait ", compteur)



# Sujet 37 - de 9h45 à

## Exercice 1 - de 9h46 à 9h49
def recherche_3(elt, tab):
    indice = -1
    for i in range(len(tab)):
        if elt == tab[i]:
            indice = i
    return indice

print(recherche_3(1, [2, 3, 4]))
print(recherche_3(1, [10, 12, 1, 56]))
print(recherche_3(1, [1, 0, 42, 7]))
print(recherche_3(1, [1, 50, 1]))
print(recherche_3(1, [8, 1, 10, 1, 7, 1, 8]))

## Exercice 2 - de 9h50 à 9h55
class AdresseIP:

    def __init__(self, adresse):
        self.adresse = adresse

    def liste_octet(self):
        """renvoie une liste de nombres entiers,
           la liste des octets de l'adresse IP"""
        return [int(i) for i in self.adresse.split(".")]

    def est_reservee(self):
        """renvoie True si l'adresse IP est une adresse
           reservee, False sinon"""
        return self.adresse == "192.168.0.0" or self.adresse == "192.168.0.255"

    def adresse_suivante(self):
        """renvoie un objet de AdresseIP avec l'adresse
           IP qui suit l'adresse self
           si elle existe et False sinon"""
        if self.liste_octet()[3] < 254:
            octet_nouveau = self.liste_octet()[3] + 1
            return AdresseIP('192.168.0.' + str(octet_nouveau))
        else:
            return False

adresse1, adresse2, adresse3 = AdresseIP('192.168.0.1'), AdresseIP('192.168.0.2'), AdresseIP('192.168.0.0')
print(adresse1.est_reservee())
print(adresse3.est_reservee())
print(adresse2.adresse_suivante().adresse)



# Sujet 39

## Exercice 1 - de 0h45 à 0h54
def fibonacci(n):
    if n ==1 or n ==2:
        return 1
    else:
        premier_terme = 1
        second_terme = 1
        somme = 2

        for i in range(n - 3):
            premier_terme = second_terme
            second_terme = somme
            somme = premier_terme + second_terme
    return somme

## Exercice 2 - de 0h54 à 0h56
def pantheon(eleves, notes):
    note_maxi = 0
    meilleurs_eleves = []

    for i in range(len(eleves)) :
        if notes[i] == note_maxi:
            meilleurs_eleves.append(eleves[i])
        elif notes[i] > note_maxi:
            note_maxi = notes[i]
            meilleurs_eleves = [eleves[i]]

    return (note_maxi,meilleurs_eleves)

eleves_nsi = ['a','b','c','d','e','f','g','h','i','j']
notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]

print(pantheon(eleves_nsi,notes_nsi))
print(pantheon([], []))



# Sujet 30

## Exercice 1 - de 0h58 à 1h01
def moyenne_2(tab):
    total_de_notes = 0
    nb_notes = 0
    for element in tab:
        total_de_notes = total_de_notes + element
        nb_notes = nb_notes + 1
    return total_de_notes / nb_notes

print(moyenne_2([1.0]))
print(moyenne_2([1.0, 2.0, 4.0]))

## Exercice 2 - de 1h02 à 1h05
def binaire_3(a):
    bin_a = str(a % 2)
    a = a // 2
    while a != 0 :
        bin_a = str(a%2) + bin_a
        a = a // 2
    return bin_a

print(binaire_3(83))
print(binaire_3(127))
print(binaire_3(0))



# Sujet 25

## Exercice 1 - de 15h20 à 15h29
def enumere(L):
    d = {}
    for i in range(len(L)):
        if L[i] in d.keys():
            d[L[i]] = d[L[i]] + [i]
        else:
            d[L[i]] = [i]
    return d

print(enumere([1, 1, 2, 3, 2, 1]))

## Exercice 2 - de 15h29 à 15h35
class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None

def parcours(arbre, liste):
    if arbre != None:
        parcours(arbre.fg, liste)
        liste.append(arbre.v)
        parcours(arbre.fd, liste)
    return liste

def insere_1(arbre, cle):
    """ arbre est une instance de la classe Arbre qui implÃ©mente
        un arbre binaire de recherche.
    """
    if cle < arbre.v:
        if arbre.fg == None:
            insere_1(arbre.fg, cle)
        else:
            arbre.fg = Arbre(cle)
    else:
        if arbre.fd == None:
            insere_1(arbre.fd, cle)
        else:
            arbre.fd = Arbre(cle)

arbre_test = Arbre(5)
arbre_test.fg = Arbre(2)
arbre_test.fd = Arbre(7)
arbre_test.fg.fd = Arbre(3)
insere_1(arbre_test, 1)
insere_1(arbre_test, 4)
insere_1(arbre_test, 6)
insere_1(arbre_test, 8)
print(parcours(arbre_test,[]))



# Sujet 11

## Exercice 1 - de 15h36 à 15h52
def convertir(tab):
    """
    tab est un tableau d'entiers, dont les éléments sont 0 ou 1,
    et représentant un entier écrit en binaire.
    Renvoie l'écriture décimale de l'entier positif dont la représentation
    binaire est donnée par le tableau tab
    """
    resultat = 0
    for i in range(len(tab)):
        resultat = resultat + tab[i] * 2**(len(tab) - i - 1)
    return resultat

print(convertir([1, 0, 1, 0, 0, 1, 1]))
print(convertir([1, 0, 0, 0, 0, 0, 1, 0]))

## Exercice 2 - de 15h52 à 16h02
liste = [9, 5, 8, 4, 0, 2, 7, 1, 10, 3, 6]

def tri_insertion(tab):
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i]
        # la variable j sert Ã  dÃ©terminer oÃ¹ placer la valeur Ã  ranger
        j = i
        # tant qu'on a pas trouvÃ© la place de l'Ã©lÃ©ment Ã  insÃ©rer
        # on dÃ©cale les valeurs du tableau vers la droite
        while j > 0 and valeur_insertion < tab[j - 1]:
            tab[j] = tab[j-1]
            j = j - 1
        tab[j] = valeur_insertion

liste = [9, 5, 8, 4, 0, 2, 7, 1, 10, 3, 6]
tri_insertion(liste)
print(liste)



# Sujet 21

## Exercice 1 - de 16h22 à 16h27
def delta(liste):
    resultat = [liste[0]]
    for i in range(1,len(liste)):
        resultat.append(liste[i] - liste[i - 1])
    return resultat

print(delta([1000, 800, 802, 1000, 1003]))
print(delta([42]))

## Exercice 2 - de 16h04 à 16h22
class Noeud:
    '''
    classe implÃ©mentant un noeud d'arbre binaire
    '''

    def __init__(self, g, v, d):
        '''
        un objet Noeud possÃ¨de 3 attributs :
        - gauche : le sous-arbre gauche,
        - valeur : la valeur de l'Ã©tiquette,
        - droit : le sous-arbre droit.
        '''
        self.gauche = g
        self.valeur = v
        self.droit = d

    def __str__(self):
        '''
        renvoie la reprÃ©sentation du noeud en chaine de caractÃ¨res
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
        s = s + expression_infixe(e.droit) + ')'
    return s

e = Noeud(Noeud(Noeud(None, 3, None),
    '*', Noeud(Noeud(None, 8, None), '+', Noeud(None, 7, None))),
    '-', Noeud(Noeud(None, 2, None), '+', Noeud(None, 1, None)))
print(expression_infixe(e))



# Sujet 35

## Exercice 1 - de 16h28 à 16h37
def ou_exclusif(tab_1, tab_2):
    resultat = []
    for i in range(len(tab_1)):
        if tab_1[i] == 1 and tab_2[i] == 0:
            resultat.append(1)
        elif tab_1[i] == 0 and tab_2[i] == 1:
            resultat.append(1)
        else:
            resultat.append(0)
    return resultat

a = [1, 0, 1, 0, 1, 1, 0, 1]
b = [0, 1, 1, 1, 0, 1, 0, 0]
c = [1, 1, 0, 1]
d = [0, 0, 1, 1]
print(ou_exclusif(a, b))
print(ou_exclusif(c, d))

## Exercice 2 - de 16h37 à 16h59
c2 = [[1, 7], [7, 1]]
c3 = [[3, 4, 5], [4, 4, 4], [5, 4, 3]]
c3bis = [[2, 9, 4], [7, 0, 3], [6, 1, 8]]


class Carre:
    def __init__(self, liste, n):
        self.ordre = n
        self.tableau = [[liste[i + j * n] for i in range(n)] for j in range(n)]

    def affiche(self):
        '''Affiche un carrÃ©'''
        for i in range(self.ordre):
            print(self.tableau[i])

    def somme_ligne(self, i):
        '''Calcule la somme des valeurs de la ligne i'''
        somme = 0
        for j in range(self.ordre):
            somme = somme + self.tableau[i][j]
        return somme

    def somme_col(self, j):
        '''Calcule la somme des valeurs de la colonne j'''
        somme = 0
        for i in range(self.ordre):
            somme = somme + self.tableau[i][j]
        return somme

    def est_semimagique(self):
        s = self.somme_ligne(0)

        #test de la somme de chaque ligne
        for i in range(len(self.tableau)):
            if self.somme_ligne(i) != s:
                return False

        #test de la somme de chaque colonne
        for j in range(len(self.tableau)):
            if self.somme_col(j) != s:
                return False

        return True

liste_c2 = (1, 7, 7, 1)
liste_c3 = (3, 4, 5, 4, 4, 4, 5, 4, 3)
liste_c3bis = (2, 9, 4, 7, 0, 3, 6, 1, 8)
c2 = Carre(liste_c2, 2)
c3 = Carre(liste_c3, 3)
c3bis = Carre(liste_c3bis, 3)
print(c3.affiche())
print(c2.est_semimagique())
print(c3.est_semimagique())
print(c3bis.est_semimagique())



# Sujet 45

## Exercice 1 - de 10h20 à 10h25
def rangement_valeurs(notes_eval):
    resultat = [0] * 11
    for element in notes_eval:
        resultat[element] = resultat[element] + 1
    return resultat

def notes_triees(liste):
    resultat = []
    for i in range(len(liste)):
        for j in range(liste[i]):
            resultat.append(i)
    return resultat


notes_eval = [2, 0, 5, 9, 6, 9, 10, 5, 7, 9, 9, 5, 0, 9, 6, 5, 4]
print(notes_eval)
effectifs_notes = rangement_valeurs(notes_eval)
print(effectifs_notes)
print(notes_triees(effectifs_notes))


## Exercice 2 - de 10h25 à 10h32
def dec_to_bin (nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == 0:
        return str(r)
    else:
        return dec_to_bin(q) + str(r)

def bin_to_dec(nb_bin):
    if nb_bin == '0':
        return 0
    elif nb_bin == '1':
        return 1
    else:
        if nb_bin[-1] == '0':
            bit_droit = 0
        else:
            bit_droit = 1
        return 2 * bin_to_dec(nb_bin[:-1]) + bit_droit

print(dec_to_bin(25))
print(bin_to_dec('101010'))



# Sujet 9

## Exercice 1 - de 10h32 à 10h37
def multiplication_1(n1, n2):
    resultat = 0
    for i in range(abs(n1)):
        if n1 > 0:
            resultat = resultat + n2
        else:
            resultat = resultat - n2
    return resultat

print(multiplication_1(3, 5))
print(multiplication_1(-4, -8))
print(multiplication_1(-2, 6))
print(multiplication_1(-2, 0))

## Exercice 2 - de 10h38 10h52
def chercher(tab, n, i, j):
    if i < 0 or j > len(tab):
        return None
    elif i > j:
        return None
    m = (i + j) // 2
    if tab[m] < n:
        return chercher(tab, n, m, j)
    elif tab[m] > n:
        return chercher(tab, n, i + 1, m)
    else:
        return m

print(chercher([1, 5, 6, 6, 9, 12], 7, 0, 10))
print(chercher([1, 5, 6, 6, 9, 12], 7, 0, 5))
print(chercher([1, 5, 6, 6, 9, 12], 9, 0, 5))
print(chercher([1, 5, 6, 6, 9, 12], 6, 0, 5))



# Sujet 28

## Exercice 1 - de 10h53 à 10h57
def moyenne_3(tab):
    '''
    moyenne(list) -> float
    Entrée : un tableau non vide d'entiers
    Sortie : nombre de type float
    Correspondant à la moyenne des valeurs présentes dans le
    tableau
    '''
    somme = 0
    nb_valeurs = len(tab)
    for element in tab:
        somme = somme + element
    return somme / nb_valeurs

print(moyenne_3([1]) == 1)
print(moyenne_3([1, 2, 3, 4, 5, 6, 7]) == 4)
print(moyenne_3([1, 2]) == 1.5)

## Exercice 2 - de 10h58 à 11h03
def dichotomie(tab, x):
    """
        tab : tableau trié dans l’ordre croissant
        x : nombre entier
        La fonction renvoie True si tab contient x et False sinon
    """
    # cas du tableau vide
    if tab == []:
        return False, 1
    # cas où x n'est pas compris entre les valeurs extrêmes
    if (x < tab[0]) or (x > tab[-1]):
        return False, 2
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False, 3

print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28))
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27))
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 1))
print(dichotomie([], 28))



# Sujet 26

## Exercice 1 - de 11h04 à 11h05
def multiplication(n1, n2):
    resultat = 0
    for i in range(abs(n1)):
        if n1 > 0:
            resultat = resultat + n2
        else:
            resultat = resultat - n2
    return resultat

print(multiplication(3, 5))
print(multiplication(-4, -8))
print(multiplication(-2, 6))
print(multiplication(-2, 0))

## Exercice 2 - de 11h15 à 11h18
def dichotomie(tab, x):
    """
    tab : tableau d’entiers trié dans l’ordre croissant
    x   : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
             fin = m - 1
    return False

print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28))
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27))



# Sujet 24

## Exercice 1 - de 11h20 à 11h24
def nbr_occurences(chaine):
    resultat = {}
    for c in chaine:
        if c in resultat:
            resultat[c] = resultat[c] + 1
        else:
            resultat[c] = 1
    return resultat

print(nbr_occurences('Hello world'))

## Exercice 2 - de 11h24 à 11h32
def fusion_1(lst1, lst2):
    n1 = len(lst1)
    n2 = len(lst2)
    lst12 = [0] * (n1 + n2)
    i1 = 0
    i2 = 0
    i=0
    while i1 < n1 and i2 < n2:
        if lst1[i1] < lst2[i2]:
            lst12[i] = lst1[i1]
            i1 = i1 + 1
        else:
            lst12[i] = lst2[i2]
            i2 = i2 + 1
        i += 1
    while i1 < n1:
        lst12[i] = lst1[i1]
        i1 = i1 + 1
        i = i + 1
    while i2 < n2:
        lst12[i] = lst2[i2]
        i2 = i2 + 1
        i = i + 1
    return lst12

print(fusion_1([1, 6, 10], [0, 7, 8, 9]))



# Sujet 27

## Exercice 1 - de 11h40 à 11h42
def recherche_min(tab):
    indice_min = 0
    for i in range(len(tab)):
        if tab[indice_min] > tab[i]:
            indice_min = i
    return indice_min

print(recherche_min([5]))
print(recherche_min([2, 4, 1]))
print(recherche_min([5, 3, 2, 2, 4]))

## Exercice 2 - de 11h43 à 11h46
def separe(tab):
    gauche = 0
    droite = len(tab) - 1
    while gauche < droite :
        if tab[gauche] == 0 :
            gauche = gauche + 1
        else :
            tab[gauche], tab[droite] = tab[droite], tab[gauche]
            droite = droite - 1
    return tab

print(separe([1, 0, 1, 0, 1, 0, 1, 0]))
print(separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]))



# Sujet 1

## Exercice 1 - de 11h47 à 11h51
def verifie(tab):
    for i in range(1, len(tab)):
        if tab[i - 1] > tab[i]:
            return False
    return True

print(verifie([0, 5, 8, 8, 9]))
print(verifie([8, 12, 4]))
print(verifie([-1, 4]))
print(verifie([5]))

## Exercice 2 - de 11h51 à 12h03
urne = ['A', 'A', 'A','B', 'C', 'B', 'C','B', 'C', 'B']

def depouille(urne):
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat

def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax :
            nmax = election[candidat]
            vainqueur = candidat
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return [vainqueur]

election = depouille(urne)
print(election)
{'B': 4, 'A': 3, 'C': 3}
print(vainqueur(election))



# Sujet 22

## Exercice 1 - de 20h24 à 20h40
def liste_puissances(a, n):
    resultat = [a]
    for i in range(1, n):
        resultat.append(a * resultat[-1])
    return resultat

def liste_puissances_borne(a, borne):
    assert a >= 2
    if a == borne:
        return []
    resultat = [a]
    while resultat[-1] * a < borne:
        resultat.append(a * resultat[-1])
    return resultat

print(liste_puissances(3, 5))
print(liste_puissances(-2, 4))
print(liste_puissances_borne(2, 16))
print(liste_puissances_borne(2, 17))
print(liste_puissances_borne(5, 5))

## Exercice 2 - de 0h43 à 0h49
dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
        "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
        "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
        "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
        "W": 23, "X": 24, "Y": 25, "Z": 26}


def est_parfait(mot):
    # mot est une chaîne de caractères (en lettres majuscules)
    code_concatene = ""
    code_additionne = 0
    for c in mot:
        code_concatene = code_concatene + str(dico[c])
        code_additionne = code_additionne + dico[c]
    code_concatene = int(code_concatene)
    if code_concatene % code_additionne == 0:
        mot_est_parfait = True
    else:
        mot_est_parfait = False
    return code_additionne, code_concatene, mot_est_parfait

print(est_parfait("PAUL"))
print(est_parfait("ALAIN"))



# Sujet 41

## Exercice 1 - de 11h15 à 11h20 #ez
def recherche_6(caractere, chaine):
    occurence = 0
    for c in chaine:
        if c == caractere:
            occurence = occurence + 1
    return occurence

print(recherche_6('e', "sciences"))
print(recherche_6('i', "mississippi"))
print(recherche_6('a', "mississippi"))

## Exercice 2 - de 11h21 à 11h24 #ez
valeurs = [100,50,20,10,5,2,1]

def rendu_glouton(a_rendre, rang):
    if a_rendre == 0:
        return []
    v = valeurs[rang]
    if v <= a_rendre:
        return [v] + rendu_glouton(a_rendre - v, rang)
    else :
        return rendu_glouton(a_rendre, rang + 1)

print(rendu_glouton(67, 0))
print(rendu_glouton(291, 0))
print(rendu_glouton(291,1)) # si on ne dispose pas de billets de 100



# Sujet 34

## Exercice 1 - de 11h33 à 11h38 #ez
def moyenne_4(tab):
    if tab == []:
        return None
    somme = 0
    for element in tab:
        somme = somme + element
    return somme / len(tab)

print(moyenne_4([5, 3, 8]))
print(moyenne_4([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(moyenne_4([]))

## Exercice 2 - de 11h43 à 11h48 #ez
def tri(tab):
    # i est le premier indice de la zone non triee,
    # j est le dernier indice de cette zone non triÃ©e.
    # Au debut, la zone non triee est le tableau complet.
    i= 0
    j= len(tab) - 1
    while i != j :
        if tab[i] == 0:
            i= i + 1
        else :
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i] = valeur
            j= j - 1
    return tab

print(tri([0, 1, 0, 1, 0, 1, 0, 1, 0]))



# Sujet 3

## Exercice 1 - de 15h06 à 15h09
def moyenne(liste):
    somme = 0
    coefficient = 0
    for element in liste:
        somme = somme + element[0] * element[1]
        coefficient = coefficient + element[1]
    if coefficient == 0:
        return None
    return somme / coefficient

print(moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]))
print(moyenne([(3, 0), (5, 0)]))

## Exercice 2 - de 15h12 à 15h21
coeur = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def affiche(dessin):
    for ligne in dessin:
        for col in ligne:
            if col == 1:
                print(" *", end= "")
            else:
                print("  ", end= "")
        print()

def zoomListe(liste_depart, k):
    liste_zoom = []
    for elt in liste_depart:
        for i in range(k):
            liste_zoom.append(elt)
    return liste_zoom

def zoomDessin(grille, k):
    grille_zoom = []
    for elt in grille:
        liste_zoom = zoomListe(elt, k)
        for i in range(k):
            grille_zoom.append(liste_zoom)
    return grille_zoom

print(affiche(coeur))
print(affiche(zoomDessin(coeur, 3)))



# Sujet 38

## Exercice 1 - de 15h28 à 15h34
def correspond(mot, mot_a_trous):
    if len(mot) != len(mot_a_trous):
        return False
    for i in range(len(mot_a_trous)):
        if mot_a_trous[i] == '*':
            pass
        elif mot_a_trous[i] == mot[i]:
            pass
        else:
            return False
    return True

print(correspond('INFORMATIQUE', 'INFO*MA*IQUE'))
print(correspond('AUTOMATIQUE', 'INFO*MA*IQUE'))
print(correspond('STOP', 'S*'))
print(correspond('AUTO', '*UT*'))

## Exercice 2 - de 15h37 à 15h41
def est_cyclique(plan):
    '''
    Prend en paramÃ¨tre un dictionnaire `plan` correspondant Ã  un plan d'envoi de messages (ici entre les personnes A, B, C, D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et False sinon.
    '''
    expediteur = 'A'
    destinataire = plan[expediteur]
    nb_destinaires = 1
    
    while destinataire != expediteur:
        destinataire = plan[destinataire]
        nb_destinaires += 1

    return nb_destinaires == len(plan)

print(est_cyclique({'A':'E', 'F':'A', 'C':'D', 'E':'B', 'B':'F', 'D':'C'}))
print(est_cyclique({'A':'E', 'F':'C', 'C':'D', 'E':'B', 'B':'F', 'D':'A'}))
print(est_cyclique({'A':'B', 'F':'C', 'C':'D', 'E':'A', 'B':'F', 'D':'E'}))
print(est_cyclique({'A':'B', 'F':'A', 'C':'D', 'E':'C', 'B':'F', 'D':'E'}))



# Sujet 7 

## Exercice 1 - de 16h05 à 16h15
def fusion(tab1, tab2):
    resultat = []
    while tab1 != [] and tab2 != []:
        if tab1[0] < tab2[0]:
            resultat.append(tab1.pop(0))
        else:
            resultat.append(tab2.pop(0))
    while tab1 != []:
        resultat.append(tab1.pop(0))
    while tab2 != []:
        resultat.append(tab2.pop(0))
    return resultat

print(fusion([3, 5], [2, 5]))
print(fusion([-2, 4], [-3, 5, 10]))
print(fusion([4], [2, 6]))

## Exercice 2 - de 16h43 à 16h49
romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def traduire_romain(nombre) :
    """ Renvoie l'ecriture decimale du nombre donné en chiffres romains """

    if len(nombre) == 1:
        return romains[nombre]

    elif romains[nombre[0]] >= romains[nombre[1]]:
        return romains[nombre[0]] + traduire_romain(nombre[1:])
    else:
        return traduire_romain(nombre[1:]) - romains[nombre[0]]

print(traduire_romain("XIV"))
print(traduire_romain("CXLII"))
print(traduire_romain("MMXXIII"))



# Sujet 29 

## Exercice 1 - de 16h52 à 17h05
class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None

a = Arbre(1)
a.fg = Arbre(4)
a.fd = Arbre(0)
a.fd.fd = Arbre(7)
a2 = Arbre(0)
a2.fg = Arbre(1)
a2.fd = Arbre(2)
a2.fg.fg = Arbre(3)
a2.fd.fg = Arbre(4)
a2.fd.fd = Arbre(5)
a2.fd.fg.fd = Arbre(6)

def taille(a):
    if a == None:
        return 0
    else:
        return 1 + taille(a.fg) + taille(a.fd)

def hauteur(a):
    if a == None:
        return 0
    else:
        return 1 + max(hauteur(a.fg), hauteur(a.fd))

print(taille(a))
print(hauteur(a))
print(taille(a2))
print(hauteur(a2))

## Exercice 2 - de 17h05 à 17h15
def ajoute(indice, element, liste):
    nbre_elts = len(liste)
    L = [0 for i in range(nbre_elts + 1)]
    if indice < nbre_elts:
        for i in range(indice):
            L[i] = liste[i]
        L[indice] = element
        for i in range(indice + 1, nbre_elts + 1):
            L[i] = liste[i - 1]
    else:
        for i in range(nbre_elts):
            L[i] = liste[i]
        L[-1] = element
    return L

print(ajoute(1, 4, [7, 8, 9]))
print(ajoute(3, 4, [7, 8, 9]))
print(ajoute(4, 4, [7, 8, 9]))



# Sujet 6 

## Exercice 1 - de 17h21 à 17h24
def recherche_7(tab, n):
    dernier_indice = len(tab)
    for i in range(len(tab)):
        if tab[i] == n:
            dernier_indice = i
    return dernier_indice

print(recherche_7([5, 3], 1))
print(recherche_7([2, 4], 2))
print(recherche_7([2, 3, 5, 2, 4], 2))

## Exercice 2 - de 17h25 à 17h29
from math import sqrt   # import de la fonction racine carree

def distance(point1, point2):
    """ Calcule et renvoie la distance entre deux points. """
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def plus_courte_distance(tab, depart):
    """ Renvoie le point du tableau tab se trouvant a la plus
    courte distance du point depart."""
    point = tab[0]
    min_dist = distance(point, depart)
    for i in range (1, len(tab)):
        if distance(tab[i], depart) < min_dist:
            point = tab[i]
            min_dist = distance(point, depart)
    return point

print(distance((1, 0), (5, 3)))
print(distance((1, 0), (0, 1)))
print(plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0)))
print(plus_courte_distance([(7, 9), (2, 5), (5, 2)], (5, 2)))



# Sujet 14 

## Exercice 1 - de 17h31 à 17h35
def recherche(elt, tab):
    for i in range(len(tab)):
        if tab[i] == elt:
            return i
    return -1

print(recherche(1, [2, 3, 4]))
print(recherche(1, [10, 12, 1, 56]))
print(recherche(50, [1, 50, 1]))
print(recherche(15, [8, 9, 10, 15]))
print(recherche(50, []))
print(recherche(4, [2, 4, 4, 3, 4]))

## Exercice 2 - de 19h33 à 19h40
def insere(a, tab):
    """ Insère l'élément a (int) dans le tableau tab (list)
        trié par ordre croissant à sa place et renvoie le
        nouveau tableau.
    """
    l = list(tab) #l contient les memes elements que tab
    l.append(a)
    i = len(l) - 2
    while i >= 0 and a < tab[i]: 
        l[i+1] = l[i]
        l[i] = a
        i = i - 1
        print(l, i)
    return l

print(insere(3, [1, 2, 4, 5]))
print(insere(30, [1, 2, 7, 12, 14, 25]))
print(insere(1, [2, 3, 4]))
print(insere(1, []))



# Sujet 33 

## Exercice 1 - de 19h50 à 19h56
def taille(arbre, lettre):
    if lettre == '':
        return 0
    else :
        return 1 + taille(arbre, arbre[lettre][0]) + taille(arbre, arbre[lettre][1])

arbre = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'],
     'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'],
     'H':['','']}
print(taille(arbre, 'F'))

## Exercice 2 - de 19h57 à 20h01
def tri_selection(tab):
    N = len(tab)
    for k in range(N):
        imin = k
        for i in range(k , N):
            if tab[i] < tab[imin] :
                imin = i
        tab[k] , tab[imin] = tab[imin] , tab[k]

liste = [41, 55, 21, 18, 12, 6, 25]
tri_selection(liste)
print(liste)



# Sujet 36 

## Exercice 1 - de 20h06 à 20h12
def couples_consecutifs(tab):
    liste_de_couples = []
    for i in range(1,len(tab)):
        if tab[i - 1] + 1 == tab[i]:
            liste_de_couples.append((tab[i - 1], tab[i]))
    return liste_de_couples

print(couples_consecutifs([1, 4, 3, 5]))
print(couples_consecutifs([1, 4, 5, 3]))
print(couples_consecutifs([1, 1, 2, 4]))
print(couples_consecutifs([7, 1, 2, 5, 3, 4]))
print(couples_consecutifs ([5, 1, 2, 3, 8, -5, -4, 7]))

## Exercice 2 - de 20h23 à 20h30
def propager(M, i, j, val):
    if M[i][j] == 1:
        M[i][j] = val

    # l'element en haut fait partie de la composante
    if i-1 >= 0 and M[i-1][j] == 1:
        propager(M, i-1, j, val)

    # l'element en bas fait partie de la composante
    if i + 1 < len(M) and M[i+1][j] == 1:
        propager(M, i + 1, j, val)

    # l'element Ã  gauche fait partie de la composante
    if j - 1 >= 0 and M[i][j-1] == 1:
        propager(M, i, j - 1, val)

    # l'element Ã  droite fait partie de la composante
    if j + 1 < len(M) and M[i][j+1] == 1:
        propager(M, i, j + 1, val)

M = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0]]
propager(M, 2, 1, 3)
print(M)



# Sujet 17 

## Exercice 1 - de 20h32 à 20h34
def moyenne(liste_notes):
    somme = 0
    coefficient = 0
    for element in liste_notes:
        somme = somme + element[0] * element[1]
        coefficient = coefficient + element[1]
    if coefficient == 0:
        return None
    return somme / coefficient

print(moyenne([(15, 2), (9, 1), (12, 3)]))

## Exercice 2 - de 20h40 à 20h52
def pascal(n):
    triangle = [[1]]
    for k in range(1,n):
        ligne_k = [1]
        for i in range(1,k):
            ligne_k.append(triangle[-1][i-1]+triangle[-1][i])
        ligne_k.append(1)
        triangle.append(ligne_k)
    return triangle



# Sujet 15 

## Exercice 1 - de 00h05 à 00h09
def mini(releve, date):
    indice_minimun = 0
    for i in range(1, len(releve)):
        if releve[indice_minimun] > releve[i]:
            indice_minimun = i
    return (releve[indice_minimun], date[indice_minimun])

t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
print(mini(t_moy, annees))

## Exercice 2 - de 00h10 à 00h12
def inverse_chaine(chaine):
    result = ""
    for caractere in chaine:
       result = caractere + result
    return result

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return chaine == inverse
    
def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)

print(inverse_chaine('bac'))
print(est_palindrome('NSI'))
print(est_palindrome('ISN-NSI'))
print(est_nbre_palindrome(214312))
print(est_nbre_palindrome(213312))
