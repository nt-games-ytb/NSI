#Exercice 2

#Question 1
def factRECURN(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factRECURN(n - 1)
    
#Question 2
def factITERA(n):
    for i in range(1, n):
        n = n * i
    return n
    


#Exerice 3

#Question 1
def fiboRECURN(n):
    if n == 0 or n == 1 or n == 2:
        return 1
    else:
        return fiboRECURN(n - 1) + fiboRECURN(n - 2)
       
#Question 2
def fiboITERA(n):
    if n == 0 or n == 1 or n == 2:
        return 1
    else:
        terme_avant_avant = 1
        terme_avant = 1
        terme = 2
        for i in range(n - 3):
            terme_avant_avant = terme_avant
            terme_avant = terme
            terme = terme_avant_avant + terme_avant
    return terme



    
#Exercice 4

#Question 1
comptage = 0
def compteVoyelleRECUR(texte):
    global comptage
    if texte == "":
        return comptage
    if texte[0] == "a" or texte[0] == "e" or texte[0] == "i" or texte[0] == "o" or texte[0] == "u" or texte[0] == "y":
        comptage = comptage + 1
    return compteVoyelleRECUR(texte[1:])
#prof:
#else:
#    if texte[0] ... (ce que j'ai mis)
#        return 1 + compteVoyelleRECUR(texte[1:])
#    else: 
#        return compteVoyelleRECUR(texte[1:])
  
#Question 2
def compteVoyelleITERA(texte):
    resultat = 0
    for i in range(len(texte)):
        if texte[i] == "a" or texte[i] == "e" or texte[i] == "i" or texte[i] == "o" or texte[i] == "u" or texte[i] == "y":
            resultat = resultat + 1
    return resultat
    


#Exercice 5

#Question 1
lapin_adulte = 2
lapin_ado = 0
lapin_bébé = 0
def lapinRECUR(mois):
    '''global lapin
    if mois == 0:
        return lapin
        
    else:
        if mois % 2 == 0:
            lapin = lapin + (lapin * 2)
        return lapinRECUR(mois - 1)'''
    '''if mois == 0:
        return 2
    elif mois == 1:
        return 4
    else:
        return lapinRECUR(mois - 1) + lapinRECUR(mois - 2)'''
    global lapin_adulte
    global lapin_ado
    global lapin_bébé
    if mois == 0:
        return lapin_adulte + lapin_ado + lapin_bébé
    else:
        lapin_adulte = lapin_adulte + lapin_ado
        lapin_ado = lapin_bébé  
        lapin_bébé = lapin_adulte
        return lapinRECUR(mois - 1)
        
def lapinRECUR2(echeance, adulte = 2, ado = 0, bebe = 0):
    if echeance == 0:
        return adulte + ado + bebe
    return lapinRECUR2(echeance - 1, adulte + ado, bebe, adulte)
    
def lapinITERA(mois, adulte = 2, ado = 0, bebe = 0):
    for i in range(mois + 1):
        if mois == i:
            print(adulte)
            print(ado)
            print(bebe)
            return adulte + ado + bebe
        save = adulte
        adulte = adulte + ado
        ado = bebe 
        bebe = save
        
def lapinITERAprof(mois):
    adulte = 2
    ado = 0
    bebe = 0
    for i in range(mois):
        ancien_adulte = adulte
        adulte =+ ado
        ado = bebe 
        bebe = ancien_adulte
    return adulte + ado + bebe