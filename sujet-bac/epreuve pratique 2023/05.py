#Exercice 1
import random

def lancer(n):
    resultat = []
    for i in range(n):
         resultat.append(random.randint(1,6))
    return resultat
    
def paire_6(tab):
    compteur = 0
    for elt in tab:
        if elt == 6:
            compteur = compteur + 1
    return compteur >= 2

print("Exemple exercice 1 :")
lancer1 = lancer(5)
print(lancer1)
print(paire_6(lancer1))
lancer2 = lancer(5)
print(paire_6(lancer2))
lancer3 = lancer(3)
print(paire_6(lancer3))
lancer4 = lancer(0)
print(paire_6(lancer4))
print()



#Exercice 2
img=[[20, 34, 254, 145, 6], [23, 124, 237, 225, 69], [197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]

def nbLig(image):
    '''renvoie le nombre de lignes de l'image'''
    return len(image)

def nbCol(image):
    '''renvoie la largeur de l'image'''
    return len(image[0])

def negatif(image):
    '''renvoie le negatif de l'image sous la forme d'une liste de listes'''
    # on cree une image de 0 aux memes dimensions que le parametre image
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]

    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            L[i][j] = 255 - image[i][j]
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
            if image[i][j] < seuil:
                L[i][j] = 0
            else:
                L[i][j] = 1
    return L
    
print("Exemple exercice 2 :")
img = [[20, 34, 254, 145, 6], [23, 124, 237, 225, 69], [197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]
print(nbLig(img))
print(nbCol(img))
print(negatif(img))
print(binaire(img,120))