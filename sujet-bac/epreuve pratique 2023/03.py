#Exercice 1
def moyenne(liste):
    valeur = 0.0
    coefficient = 0.0
    for i in range(len(liste)):
        valeur = valeur + liste[i][0] * liste[i][1]
        coefficient = coefficient + liste[i][1]
    if coefficient == 0.0:
        return None
    else:
        return valeur/coefficient

print("Exemple exercice 1 :")
print(moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]))
print(moyenne([(3, 0), (5, 0)]))
print()



#Exercice 2
coeur = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
def affiche(dessin):
    for ligne in dessin:
        for col in ligne:
            if col == 1:
                print(" *", end= "")
            else:
                print("  ", end= "")
        print()

def zoomListe(liste_depart, k):
    liste_zoom = []
    for elt in liste_depart:
        for i in range(k):
            liste_zoom.append(elt)
    return liste_zoom

def zoomDessin(grille, k):
    grille_zoom = []
    for elt in grille:
        liste_zoom = zoomListe(elt, k)
        for i in range(k):
            grille_zoom.append(liste_zoom)
    return grille_zoom

print("Exemple exercice 2 :")
print(affiche(coeur))
print(affiche(zoomDessin(coeur, 3)))