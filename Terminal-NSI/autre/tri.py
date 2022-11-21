#region Tri par insertion
def tri_insertion(liste):
    '''On parcourt le tableau de la gauche vers la droite et pour chaque élément, on le classe dans la partie du tableau situé sur sa gauche.
       On aura donc un coût quadratique.'''
    for i in range(1, len(liste)):
        élément_choisis = liste[i]
        indice_élément_comparer = i                               
        
        while  indice_élément_comparer > 0 and liste[indice_élément_comparer - 1] > élément_choisis:
            liste[indice_élément_comparer] = liste[indice_élément_comparer - 1]
            indice_élément_comparer = indice_élément_comparer - 1

        liste[indice_élément_comparer] = élément_choisis 

    return liste
    #print(liste)

print("Tri par instertion : " + str(tri_insertion([9,4,5,1,7,6])) + "\n")
#endregion

#region Tri par sélection 
def tri_selection(liste):
    '''On recherche le plus petit élément et on le met à sa place (indice 0 donc),
       puis on recherche le deuxième plus petit et on le met à l'indice 1 et on continue comme cela avec tous les éléments.
       On aura donc un coût quadratique.'''
    nombre_éléments = len(liste) 
    for i in range(0, nombre_éléments):
        place_du_plus_petit = i       
        for j in range(i + 1, nombre_éléments):
            if liste[j] < liste[place_du_plus_petit]:
                place_du_plus_petit = j
        
        if place_du_plus_petit != i:
            liste[i], liste[place_du_plus_petit] = liste[place_du_plus_petit], liste[i]

    return liste
    #print(liste)

print("Tri par sélection : " + str(tri_selection([9,4,5,1,7,6])) + "\n")
#endregion

#region Tri par fusion
def tri_fusion(liste):
    '''On divise la liste en 2 puis on les divise pour avoir plusieurs paquets de 2 ou 1,
       on trie les paquet, une fois les 2 liste trié on compare un par un les éléments des 2 listes pour les trier.
       On aura donc un coût logarithmique.'''
    if len(liste) <= 1:
        return liste

    indice_milieu = len(liste) // 2
    moitié_gauche = liste[:indice_milieu]
    moitié_droite = liste[indice_milieu:]
    moitié_gauche_triée = tri_fusion(moitié_gauche)
    moitié_droite_triée = tri_fusion(moitié_droite)

    if moitié_gauche_triée == []:
        return moitié_droite_triée
    if moitié_droite_triée == []:
        return moitié_gauche_triée

    indice1 = 0
    indice2 = 0
    resultat = []

    while indice1 != len(moitié_gauche_triée) and indice2 != len(moitié_droite_triée):
        if moitié_gauche_triée[indice1] < moitié_droite_triée[indice2]:
            resultat.append(moitié_gauche_triée[indice1])
            indice1 = indice1 + 1
        else:
            resultat.append(moitié_droite_triée[indice2])
            indice2 = indice2 + 1

    if indice1 == len(moitié_gauche_triée):
        while indice2 != len(moitié_droite_triée):
            resultat.append(moitié_droite_triée[indice2])
            indice2 = indice2 + 1
    else:
        while indice1 != len(moitié_gauche_triée):
            resultat.append(moitié_gauche_triée[indice1])
            indice1 = indice1 + 1

    return resultat
    
print("Tri par fusion : " + str(tri_fusion([9,4,5,1,7,6])))
#endregion