#Chapitre 2 - Exercice 2

#region Functions
#Question 2 
def diviseur(nombre):
    resultat = []
    try:
        for i in range(nombre):
            if nombre % (i + 1) == 0:
                resultat.append(i + 1)
        #print(resultat)
        return resultat
    except:
        #print(False)
        return False
    if resultat == []:
        #print(False)
        return False
    


#Question 6
def PGCD(nombre1, nombre2):#Plus grand commun diviseur
    '''
    DESCRIPTION : Une fonction qui renvoie le plus grand diviseur commun de deux nombres entiers
    '''

    resultat = 0
    #Créer l'integer "resultat" qui contiendra un nombre entier
    liste_diviseur_1 = diviseur(nombre1)
    #Créer la liste "liste_diviseur_1" qui contiendra la liste des diviseurs du 1er nombre
    liste_diviseur_2 = diviseur(nombre2)
    #Créer la liste "liste_diviseur_1" qui contiendra la liste des diviseurs du 2ème nombre
    for i in range(len(liste_diviseur_1)):
    #Le programme va faire une boucle (de 0 aux nombres d'éléments dans liste_diviseur_1) avec les 4 prochaines lignes (commentaire exceptés)
        for j in range(len(liste_diviseur_2)):
        #Le programme va faire une boucle (de 0 aux nombres d'éléments dans liste_diviseur_2) avec les 3 prochaines lignes(commentaire exceptés)
            if liste_diviseur_1[i] == liste_diviseur_2[j]:
            #Si un nombre de liste_diviseur_1 est égale à unliste_diviseur_2 alors :
                if liste_diviseur_1[i] > resultat:
                #Si ce nombre est plus grand que l'ancien plus grand commun diviseur alors :
                    resultat = liste_diviseur_1[i]
                    #Replace l'ancien plus grand commun diviseur par le nouveau
    return resultat #Renvoie le resultat (le plus grand commun diviseur)
    #print(resultat) #Affiche le resultat (le plus grand commun diviseur)
    


#Question 7    
def  decompoFacteursPremiers(nombre):
    '''
    DESCRIPTION : Une fonction qui renvoie la liste des nombres premiers (comporte deux diviseurs) d'un nombre
    '''
    resultat = []
    #Créer la liste "resultat" qui contiendra les nombres premiers
    liste_diviseur = diviseur(nombre)
    #Créer la liste "liste_diviseur_1" qui contiendra la liste des diviseurs du nombre choisis
    for i in range(len(liste_diviseur)):
    #Le programme va faire une boucle (de 0 aux nombres d'éléments dans liste_diviseur) avec les 3 prochaines lignes (commentaire exceptés)
        diviseur_du_nombre = diviseur(liste_diviseur[i])
        #Créer la liste "diviseur_du_nombre" qui contiendra la liste des diviseurs d'un des diviseur du nombre en fonction de i (soit en fonction du numéro de la boucle)
        if len(diviseur_du_nombre) == 2:
        #Si la liste contient seulement 2 éléments (caractèristique principale des nombres premiers) alors :
            resultat.append(liste_diviseur[i])
            #Ajoute ce nombre à la liste "resultat"
    return resultat #Renvoie le resultat (la liste des nombres premiers dans le nombre)
    #print(resultat) #Affiche le resultat (la liste des nombres premiers dans le nombre)
        
#endregion

#region Execute
print("Fonction 1 :")
diviseur(14)

print("\r\nFonction 2 :")
PGCD(84,36)

print("\r\nFonction 3 :")
decompoFacteursPremiers(30)
#endregion