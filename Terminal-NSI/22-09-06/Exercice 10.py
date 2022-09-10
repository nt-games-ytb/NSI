#Chapitre 1 - Exercice 10

#Question 1
#liste ---> structure indexée et statique

#region Functions
#Question 2
def extraire2(un_texte):
    resultat = [None] * len(un_texte)
    for i in range(len(un_texte)):
        resultat[i] = un_texte[i]
    print(resultat)#return resultat

#Question 3
def occurence(une_liste):
    resultat = [None] * (len(une_liste) * 2)
    nombre = 0
    indice = 0
    for i in range(len(une_liste)):
        caractère = une_liste[i]#t
        for j in range(len(une_liste)):
            if caractère == une_liste[j]:
                nombre = nombre + 1
        resultat[i + indice] = caractère
        resultat[i + 1 + indice] = nombre
        nombre = 0
        indice = indice + 1
        print(resultat)
        
def occurence2(une_liste):
    #region Comptage des caractères 
    caractère = [None] * len(une_liste)
    nombre = [None] * len(une_liste)
    for i in range(len(une_liste)):
        if une_liste[i] not in caractère:
            caractère[i] = une_liste[i]
            nombre[i] = 0
            for j in range(len(une_liste)):
                if caractère[i] == une_liste[j]:
                    nombre[i] = nombre[i] + 1
    #endregion
    
    #region Taille de la liste (resultat)
    taille = 0
    for element in caractère:
        if element != None:
            taille = taille + 1
    taille = taille * 2
    #endregion
    
    #region Afficher le résultat
    resultat = [None] * taille
    indice = 0
    for k in range(taille // 2):
        resultat[k + indice] = caractère[k]
        resultat[k + 1 + indice] = nombre[k]
        indice = indice + 1
    print(resultat) #return resultat
    #endregion
    
def profOccurence():
    nb_carac_unique = 0
    liste_carac_unique = [None] * len(une_liste)
    indice = 0
    for caractere in une_liste:
        if caractere not in liste_carac_unique:
            liste_carac_unique[indice] = caractere
            indice += 1
            nb_carac_unique += 1
    liste_finale = {None * ([nb_carac_unique*2])
    
    indice = 0
    
    for caractere in liste_carac_unique:
        if caractere!=None:
            liste_finale[indice]=caractere
            indice += 1
            
            compteur = 0
            for c in une_liste:
                if caractere==c:
                    compteur += 1
            liste_finale[indice] = compteur
            indice += 1
    return liste_finale

def occurenceTri(une_liste):
    resultat = [None] * (len(une_liste) // 2)
    c = 0
    for i in range(len(une_liste) // 2):#2
        resultat[une_liste[i + 1 + c]] = une_liste[i + c]
        c = c + 1
    print(resultat)#return resultat
#endregion

#region Execute
print("Fonction 1 :")
extraire2("Bonjour je suis nico")

print("\r\nFonction 2 :")
occurence2(["e","c","b","e"])

print("\r\nFonction 3 :")
occurenceTri(["e",1,"b",0])
#endregion

