#Chapitre 1 - Exercice 11
import random

#region Functions
#Question 1 #Pour prof : on inclu 20 ou pas ?
def liste_alea(n):
    resultat = [None] * n
    for i in range(n):
        resultat[i] = random.randint(-20, 20)
    print(resultat)#return resultat

#Question 2 
def paire(liste):
    resultat = [None] * len(liste) #surement améliorable
    for i in range(len(liste)):
        if liste[i] % 2 == 0:
            resultat[i] = liste[i]
    print(resultat)#return resultat
    
#Question 2 - Mieux 
def paire2(liste):
    taille_liste = 0
    for i in range(len(liste)):
        if liste[i] % 2 == 0:
            taille_liste = taille_liste + 1
    resultat = [None] * taille_liste
    indice = 0
    for i in range(len(liste)):
        if liste[i] % 2 == 0:
            resultat[indice] = liste[i]
            indice = indice + 1
    print(resultat)#return resultat
#endregion

#region Execute
print("Fonction 1 :")
liste_alea(14)

print("\r\nFonction 2 :")
paire([1,5,6,9,7,3,4])

print("\r\nFonction 2 - Mieux :")
paire2([1,5,6,9,7,3,4])
#endregion
