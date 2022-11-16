#Chapitre 9
test = [4, 5, 1, 8, 5]



#Exercice 2
def recherche(liste, nombre):
    assert liste != []
    if len(liste) == 1:
        if liste[0] == nombre:
            return 1
        else :
            return 0
    else:
        moitié = len(liste)//2
        gauche = liste[moitié:]
        droite = liste[:moitié]
        return recherche(gauche, nombre) + recherche(droite, nombre)
        


#Exercice 4
def fusion(liste1, liste2):
    résultat = []
    while liste1 != [] or liste2 != []:
        if liste1 == []:
            résultat = résultat + liste2
            liste2 = []
        elif liste2 == []:
            résultat = résultat + liste1
            liste1 = []
        elif liste1[0] >= liste2[0]:
            élément_supprimé = liste2.pop(0)
            résultat.append(élément_supprimé)
        else:
            élément_supprimé = liste1.pop(0)
            résultat.append(élément_supprimé)
    return résultat
    
def fusion_prof(liste1, liste2):
    if liste1 == []:
        return liste2
    if liste2 == []:
        return liste1
    indice1 = 0
    indice2 = 0
    resultat = []
    while indice1 != len(liste1) and indice2 != len(liste2):#aucun indice est au baut
        if liste1[indice1] < liste2[indice2]:
            resultat.append(liste1[indice1])
            indice1 += 1
        else:
            resultat.append(liste2[indice2])
            indice2 += 1
    if indice1 == len(liste1): #il faut remplir avec le reste de la liste 2
        while indice2 != len(liste2):
            resultat.append(liste2[indice2])
            indice2 += 1
    else: #il faut remplir avec le reste de la liste
        while indice1 != len(liste1):
            resultat.append(liste1[indice1])
            indice1 += 1
    return resultat

print(fusion([1,6,8], [2,3,7]))

#Exercice 5
def tri_fusion(liste):
    #résultat = []
    if len(liste) == 1:
        return liste
        #résultat = liste
    else:
        moitié = len(liste)//2
        gauche = liste[:moitié]
        droite = liste[moitié:]
        print(gauche)
        print(droite)
        tri_fusion(gauche)
        tri_fusion(droite)
        print(gauche)
        print(droite)
        liste.pop(0)
        liste.pop(0)
        liste = liste + fusion_prof(droite, gauche)
        print(liste)
        #print
        #if gauche >= droite:
        #    résultat = résultat + fusion_prof(gauche, droite)
        #else:
        #    résultat = résultat + fusion_prof(droite, gauche)
    return liste#résultat
    
def tri_fusion_prof(liste):
    if len(liste) <= 1:#si liste vide ou un seul élément
        return liste
    indice_milieu = len(liste)//2
    moitié_gauche = liste[:indice_milieu]
    moitié_droite = liste[indice_milieu:]
    moitié_gauche_triée = tri_fusion_prof(moitié_gauche)
    moitié_droite_triée = tri_fusion_prof(moitié_droite)
    return fusion(moitié_gauche_triée, moitié_droite_triée)

def tri_fusion_prof_short(liste):
    if len(liste) <= 1:#si liste vide ou un seul élément
        return liste
    return fusion(tri_fusion_prof(liste[:len(liste)//2]), tri_fusion_prof(liste[len(liste)//2:]))
    
def tri_fusion_prof_long(liste):
    if len(liste) <= 1:#si liste vide ou un seul élément
        return liste
    indice_milieu = len(liste)//2
    moitié_gauche = liste[:indice_milieu]
    moitié_droite = liste[indice_milieu:]
    moitié_gauche_triée = tri_fusion_prof(moitié_gauche)
    moitié_droite_triée = tri_fusion_prof(moitié_droite)
    if moitié_gauche_triée == []:
        return moitié_droite_triée
    if moitié_droite_triée == []:
        return moitié_gauche_triée
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
    return fusion(moitié_gauche_triée, moitié_droite_triée)
    
print(tri_fusion_prof_long([6,4,7,3,8,2,1,9]))