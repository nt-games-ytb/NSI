#Exercice 1
def liste_puissances(a, n):
    resultat = []
    for i in range(n):
        resultat.append(a)
        for j in range(i):
            resultat[i] = resultat[i] * a
    return resultat
    
def liste_puissances_prof(a, n):
    liste=[]
    b = 1
    for i in range(1, n+1):
        b = b * a
        liste.append(b)
    return liste
    
def liste_puissances_prof2(a, n):
    liste=[]
    b = a
    for i in range(1, n+1):
        liste.append(b)
        b = b * a
    return liste    

def liste_puissances_borne(a, borne):
    resultat = []
    puissance = a
    while puissance < borne:
        resultat.append(puissance)
        puissance = puissance * a
    return resultat

print("Exemple exercice 1 :")
print(liste_puissances(3, 5))
print(liste_puissances(-2, 4))
print(liste_puissances_borne(2, 16))
print(liste_puissances_borne(2, 17))
print(liste_puissances_borne(5, 5))
print()



#Exercice 2
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
    if int(code_concatene) % code_additionne == 0 :
        mot_est_parfait = True
    else:
        mot_est_parfait = False
    return code_additionne, code_concatene, mot_est_parfait

print("Exemple exercice 2 :")
print(est_parfait("PAUL"))
print(est_parfait("ALAIN"))