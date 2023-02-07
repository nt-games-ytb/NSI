#Exercice 1
def recherche(a, tab):
    resultat = 0
    for element in tab:
        if element == a:
            resultat = resultat + 1
    return resultat

print("Exemple exercice 1 :")
print(recherche(5, []))
print(recherche(5, [2 , 3, 4, 8]))
print(recherche(5, [2, 3, 1, 5, 3, 7, 4]))
print(recherche(5, [2, 5, 3, 5, 4, 5]))
print()



#Exercice 2
pieces = [1, 2, 5, 10, 20, 50, 100, 200]

def rendu_monnaie(somme_due, somme_versee):

    rendu = []
    a_rendre = somme_versee - somme_due
    i = len(pieces) - 1
    while a_rendre != 0:
        if pieces[i] <= a_rendre :
            rendu.append(pieces[i])
            a_rendre = a_rendre - pieces[i]
        else :
            i = i - 1
    return rendu
    
print("Exemple exercice 2 :")
print(rendu_monnaie(700, 700))
print(rendu_monnaie(102, 500))