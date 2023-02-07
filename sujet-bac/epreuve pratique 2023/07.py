#Exercice 1
def fusion(tab1, tab2): #Mon alternative
    tab3 = []
    while tab1 != []:
        while tab2 != []:
            if tab1 == []:
                tab3 = tab3 + tab2
                tab2 = []
            elif tab1[0] <= tab2[0]:
                tab3.append(tab1.pop(0))
            else:
                tab3.append(tab2.pop(0))
            #print(tab1, tab2)
        if tab2 == [] and tab1 != []:
            tab3 = tab3 + tab1
    return tab3

#venant du tri par fusion
'''
    indice1 = 0
    indice2 = 0
    resultat = []
    while indice1 != len(moitié_gauche_triée) and indice2 != len(moitié_droite_triée):#aucun indice est au baut
        if moitié_gauche_triée[indice1] < moitié_droite_triée[indice2]:
            resultat.append(moitié_gauche_triée[indice1])
            indice1 += 1
        else:
            resultat.append(moitié_droite_triée[indice2])
            indice2 += 1
    if indice1 == len(moitié_gauche_triée): #il faut remplir avec le reste de la moitié_droite_triée
        while indice2 != len(moitié_droite_triée):
            resultat.append(moitié_droite_triée[indice2])
            indice2 += 1
    else: #il faut remplir avec le reste de la liste
        while indice1 != len(moitié_gauche_triée):
            resultat.append(moitié_gauche_triée[indice1])
            indice1 += 1
    return resultat
'''



#Exercice 2 à modifier
romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def traduire_romain(nombre) :
    """ Renvoie l'ecriture decimale du nombre donnÃ© en chiffres romains """

    if len(nombre) == 1:
        return romains[nombre]

    elif romains[nombre[0]] >= romains[nombre[1]]:
        return romains[nombre[0]] + traduire_romain(nombre[:1])
    else:
        return -romains[nombre[0]] + traduire_romain(nombre[:1])