#Exercice 1
def verifie(tableau_de_valeurs):
    if len(tableau_de_valeurs) <= 1:
        return True
    premiere_valeur = tableau_de_valeurs[0]
    for i in range(1, len(tableau_de_valeurs)):
        if premiere_valeur > tableau_de_valeurs[i]:
            return False
        premiere_valeur = tableau_de_valeurs[i]
    return True

def verifie_2(tableau_de_valeurs):
    for i in range(1, len(tableau_de_valeurs)):
        if tableau_de_valeurs[i-1] > tableau_de_valeurs[i]:
            return False
    return True


#Exercice 2
urne = ['A', 'A', 'A','B', 'C', 'B', 'C','B', 'C', 'B']

def depouille(urne):
    resultat = {}#"A":0;"B":0;"C":0
    for bulletin in urne:
        if bulletin in resultat.keys():
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat

def vainqueur(election):#Erreur: vainqueur est deux fois (fonction et variable) et la variable vainqueur est inutile
    #vainqueur = ''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax :
            nmax = election[candidat]
            #vainqueur = candidat
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale
