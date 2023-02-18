#Exercice 1
def ajoute_dictionnaires(d1, d2):
    d = dict(d1)
    '''
    si tu veux copié d1 sans dict() :
    for cle in d1.keys():
        d[cle] = d1[cle]
    '''
    for cle, valeur in d2.items():
        #print(d, cle, valeur)
        if cle in d.keys():
            d[cle] = d[cle] + valeur
        else:
            d[cle] = d2[cle]
    return d
        
print("Exemple exercice 1 :")
print(ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}))
print(ajoute_dictionnaires({}, {2: 9, 3: 11}))
print(ajoute_dictionnaires({1: 5, 2: 7}, {}))
print()



#Exercice 2
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
    
print("Exemple exercice 2 :")
print(nbre_coups())