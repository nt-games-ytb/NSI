# Activité 2

## Question 1
def Fibo_Itera(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
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
    
def Fibo_Itera_Prof(n):
    if n in [0, 1]:
        return n
    precedent = 1
    suivant = 1
    for i in range(n - 2):
        suivant, precedent = suivant + precedent, suivant
    return suivant
    
print(Fibo_Itera(15))
    
## Question 2
def Fibo_Recur(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return Fibo_Recur(n - 1) + Fibo_Recur(n - 2)
    
def Fibo_Recur_Prof(n):
    if n in [0,1]:
        return n
    return Fibo_Recur(n - 1) + Fibo_Recur(n - 2)
    
print(Fibo_Recur(15))

## Question 3
dico_recur = {}
    
def Fibo_Recur_Dyna(n):
    global dico_recur
    if n in dico_recur.keys():
        return dico_recur[n]
    if n in [0,1]:
        return n
    valeur = Fibo_Recur_Dyna(n - 1) + Fibo_Recur_Dyna(n - 2)
    dico_recur[n] = valeur
    return valeur

print(Fibo_Recur_Dyna(15))

## Question 4
dico_itera = {}

def Fibo_Itera_Dyna(n):#test
    global dico_itera
    if n in dico_itera.keys():
        return dico_itera[n]
    else:
        if n in [0,1]:
            return n
        precedent = 1
        suivant = 1
        for i in range(n - 2):
            if i + 3 in dico_itera.keys() and i > 2:
                precedent = dico_itera[n - 1]
                suivant = dico_itera[n]
            else:
                suivant, precedent = suivant + precedent, suivant
                dico_itera[i + 3] = suivant
        return suivant

def Fibo_Itera_Dyna_Prof(n):
    global dico_itera
    if n in dico_itera.keys():
        return dico_itera[n]
    if n in [0, 1]:
        return n
    precedent = 1
    suivant = 1
    for i in range(n - 2):
        suivant, precedent = suivant + precedent, suivant
        dico_itera[i + 3] = suivant
    return suivant

print(Fibo_Itera_Dyna(15))
        

    
# Activité 4
        
## Question 1
P = (200, 100, 50, 20, 10, 5, 2, 1)

def rendu_Itera(n):
    somme = 0
    i = 0
    while n != 0:
        if n == P[i]:
            somme = somme + 1
            n = n - P[i]
        elif n > P[i]:
            somme = somme + 1
            n = n - P[i]
        elif n < P[i]:
            i = i + 1
    return somme

print(rendu_Itera(567))

## Question 2
def rendu_Recur(n):
    if n == 0:
        return 0
    for indice in range(len(P)):
        if P[indice] <= n:
            return 1 + rendu_Recur(n - P[indice])

print(rendu_Recur(567))

## Question 3      
dico = {}
            
def rendu_Recur_Dyna(n):#ne sauvegarde pas toute les valeurs
    if n == 0:
        return 0
    global dico
    if n in dico.keys():
        return[n]
    for indice in range(len(P)):
        if P[indice] <= n:
            #print(n)
            valeur = 1 + rendu_Recur_Dyna(n - P[indice])
            dico[n] = valeur
            return valeur

def rendu_recur_Dyna_Prof(n):
    if n == 0:
        return 0
    if n in dico:
        return dico[n]
    min_nb_pieces = n
    for p in P:
        if p <= n:
            nb_pieces = 1 + rendu_recur_Dyna_Prof(n - p)
            min_nb_pieces = min(min_nb_pieces, nb_pieces)
    dico[n] = min_nb_pieces
    return min_nb_pieces

print(rendu_Recur_Dyna(567))
print(dico)
dico = {}
print(rendu_recur_Dyna_Prof(567))
print(dico)