graph = [["Toto", "Tantan", "Tutu", "Titi", "Fifi", "Fufu", "Foufou", "Tôtô", "Furfur", "Tintin", "Teïteï", "Têtê", "Tojtoj", "Tajtaj", "Tijtij"],[("Toto", "Tantan"), ("Toto", "Tôtô"), ("Toto", "Tintin"), ("Tutu", "Tantan"), ("Tutu", "Tôtô"), ("Tantan", "Titi"), ("Titi", "Fifi"), ("Fifi", "Fufu"), ("Fufu", "Foufou"), ("Tôtô", "Tijtij"), ("Tijtij", "Tojtoj"), ("Tojtoj", "Tajtaj"), ("Tojtoj", "Teïteï"), ("Teïteï", "Têtê"), ("Teïteï", "Tintin"), ("Tintin", "Furfur"), ("Furfur", "Tôtô")]]


def ajoutArete(arete):
    global graph
    graph[1].append(arete)
    return graph
    
def suppressionArete(arete):
    global graph
    indice_pop = -1
    for i in range(len(graph[1])):
        if graph[1][i][0] == arete[0] or graph[1][i][0] == arete[1]:
            if graph[1][i][1] == arete[0] or graph[1][i][1] == arete[1]:
                #graph[1].pop(i)
                #return graph
                indice_pop = i
    if indice_pop != -1:
        graph[1].pop(indice_pop)
    else:
        return "Arête introuvable !"
    
def ajoutSommet(sommet):
    global graph
    graph[0].append(sommet)
    return graph
    
def suppressionSommet(sommet):
    global graph
    indice_pop = -1
    for i in range(len(graph[0])):
        if graph[0][i] == sommet:
            indice_pop = i
    if indice_pop != -1:
        graph[0].pop(indice_pop)
    else:
        return "Sommet introuvable !"
        
    liste_arete_pop = []
    for j in range(len(graph[1])):
        if graph[1][j][0] == sommet or graph[1][j][1] == sommet:
            liste_arete_pop.append(j)
    for element in liste_arete_pop:
        graph[1].pop(element)
    #Version prof :
    #indice = 0
    #while indice < len(graph[1])!
    #    if sommet in graph[1][indice]:
    #        graph[1].pop(indice)
    #    else:
    #        indice=+1
    return graph
    
def nombreSommets():
    global graph
    return len(graph[0])
    
def nombreAretes():
    global graph
    return len(gtaph[1])
    
def degreSommet(sommet):
    global graph
    compteur = 0
    for i in range(len(graph[1])):
        if graph[1][i][0] == sommet or graph[1][i][1] == sommet:
            compteur = compteur + 1 
    return compteur
    
def degreSommet_Prof(sommet):
    global graph
    compteur = 0
    for arete in graph[1]:
        for elt in arete:
            if elt == sommet:
                compteur += 1 
    return compteur
    
def adjacentSommets(sommet1,sommet2): #qui renvoie un booléen.
    global graph
    for i in range(len(graph[1])):
        if graph[1][i][0] == sommet1 or graph[1][i][0] == sommet2:
            if graph[1][i][1] == sommet1 or graph[1][i][1] == sommet2:
                return True
    return False
    
dico = {"Toto":0, "Tantan":1, "Tintin":2, "Titi":3, "Tutu":4, "Tôtô":5, "Furfur":6, "Teïteï":7, "Têtê":8, "Tajtaj":9, "Tojtoj":10, "Tijtij":11, "Fifi":12, "Fufu":13, "Foufou":14}
matrice = []
for i in range(15):
    matrice.append([])
    for j in range(15):
        matrice[i].append(0)
for arete in graph[1]:
    matrice[dico[arete[0]]][dico[arete[1]]]+=1

    matrice[dico[arete[1]]][dico[arete[0]]]+=1
    
    
    