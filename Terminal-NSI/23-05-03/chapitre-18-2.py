# Chapitre 18

## Exercice 7
""""
### Question 1
dico = {0:"Toto", 1:"Tantan", 2:"Tutu", 3:"Tôtô", 4:"Titi", 5:"Fifi", 6:"Fufu", 7:"Foufou", 8:"Tijtij", 9:"Tojtoj", 10:"Tajtaj", 11:"Teïteï", 12:"Têtê", 13:"Tintin", 14:"Furfur"}

### Question 2
liste_arete = [[0,1], [1,2], [2,3], [1,4], [4,5], [5,6], [6,7], [3,8], [8,9], [9,10], [9,11], [11,12], [11,13], [13,14], [14,3], [13, 0], [0,3]]

### Question 3
def ajoutArete(arete):#marche
    global liste_arete
    liste_arete.append(arete)
    return liste_arete
    
def suppressionArete(arete):#marche
    global liste_arete
    indice_pop = -1
    for i in range(len(liste_arete)):
        if liste_arete[i][0] == arete[0] or liste_arete[i][0] == arete[1]:
            if liste_arete[i][1] == arete[0] or liste_arete[i][1] == arete[1]:
                indice_pop = i
    if indice_pop != -1:
        liste_arete.pop(indice_pop)
    else:
        return "Arête introuvable !"
    
def ajoutSommet(sommet):#marche
    global dico
    nombre_de_sommet = len(dico)
    dico[nombre_de_sommet] = sommet
    return dico
    
def suppressionSommet(sommet):
    global dico
    indice_pop = -1
    for i in range(len(dico)):
        if dico[i] == sommet:
            indice_pop = i
    if indice_pop != -1:
        del dico[indice_pop]
    else:
        return "Sommet introuvable !"
        
    global liste_arete
    liste_arete_pop = []
    for j in range(len(liste_arete)):
        if liste_arete[j][0] == sommet or liste_arete[j][1] == sommet:
            liste_arete_pop.append(j)
    for element in liste_arete_pop:
        del liste_arete[element]
    return str(dico) + str(liste_arete)"""
    
    
### Question 1
dico = {"Toto":0, "Tantan":1, "Tintin":2, "Titi":3, "Tutu":4, "Tôtô":5, "Furfur":6, "Teïteï":7, "Têtê":8, "Tajtaj":9, "Tojtoj":10, "Tijtij":11, "Fifi":12, "Fufu":13, "Foufou":14}

### Question 2
liste_arete = [
    [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    ]

### Question 3
def ajoutArete(arete):#marche
    global dico
    global liste_arete
    
    liste_arete[dico[arete[0]]][dico[arete[1]]] += 1
    liste_arete[dico[arete[1]]][dico[arete[0]]] += 1
    
    return str(dico) + str(liste_arete)
    
    
    
def suppressionArete(arete):#marche
    global dico
    global liste_arete
    
    if liste_arete[dico[arete[0]]][dico[arete[1]]] != 0:
        liste_arete[dico[arete[0]]][dico[arete[1]]] -= 1
    else:
        return "Arête introuvable !"
        
    return str(dico) + str(liste_arete)
    
    
    
def ajoutSommet(sommet):
    global dico
    global liste_arete
    
    dico[sommet] = len(dico)
    
    for i in range(len(liste_arete)):
        liste_arete[i].append(0)
    liste_arete.append([])
    for j in range(len(liste_arete[0])):
        liste_arete[len(liste_arete) - 1].append(0)
        
    return str(dico) + str(liste_arete)
    
    
    
def suppressionSommet(sommet):
    global dico
    global liste_arete
    
    indice_pop = dico[sommet]
    del dico[sommet]
    
    liste_arete.pop(indice_pop)
    for ligne in liste_arete:
        ligne.pop(indice_pop)
        
    return str(dico) + str(liste_arete)