#Exercice 1
def recherche(tab, n):
    resultat = len(tab) 
    for i in range(len(tab)):
        if tab[i] == n:
            resultat = i
    return resultat

print("Exemple exercice 1 :")
print(recherche([5, 3],1))
print(recherche([2,4],2))
print(recherche([2,3,5,2,4],2))
print()



#Exercice 2
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
            min_dist = distance(tab[i], depart)
    return point

print("Exemple exercice 2 :")
print(distance((1,0),(5,3)))
print(distance((1,0),(0,1)))
print(plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0)))
print(plus_courte_distance([(7, 9), (2, 5), (5, 2)], (5, 2)))