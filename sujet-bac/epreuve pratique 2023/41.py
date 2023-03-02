#Exercice 1
def recherche(caractere, chaine):
    resultat = 0
    for c in chaine:
        if c == caractere:
            resultat = resultat + 1
    return resultat

print("Exemple exercice 1 :")
print(recherche('e', "sciences"))
print(recherche('i', "mississippi"))
print(recherche('a', "mississippi"))
print()



#Exerice 2
valeurs = [100,50,20,10,5,2,1]

def rendu_glouton(a_rendre, rang):
    if a_rendre == 0:
        return []
    v = valeurs[rang]
    if v <= a_rendre :
        return [v] + rendu_glouton(a_rendre - v, rang)
    else :
        return rendu_glouton(a_rendre, rang + 1)

print("Exemple exercice 2 :")
print(rendu_glouton(67, 0))
print(rendu_glouton(291, 0))
print(rendu_glouton(291,1)) # si on ne dispose pas de billets de 100