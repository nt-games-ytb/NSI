#Chapitre 3 - Exercice 11

#region Class
class Tableau:
    def __init__(self, taille):
        self.taille = taille
        self.tablo = [None] * taille

    def toutvide(self):
        if self.tablo==[]:
            return True
        else:
            for element in self.tablo:
                if element != None:
                    return False
            return True
            
    def change(self, i, data): 
        self.tablo[i] = data
    
    def effacer(self,i):
        self.tablo[i] = None
    
    def connaitre(self,i):
        return self.tablo[i]
        
    def affichetout(self):
        return self.tablo
#endregion

#region Functions
#Question 1
def extraire2(UnTexte):
    resultat = Tableau(len(UnTexte))
    for i in range(len(UnTexte)):
        resultat.change(i, UnTexte[i])
    return resultat
    
#Question 2
def occurence(unTableau):
    #region Comptage des caractères 
    caractère = Tableau(unTableau.taille)#
    nombre = Tableau(unTableau.taille)#
    for i in range(unTableau.taille):
        if unTableau.connaitre(i) not in caractère.affichetout():
            caractère.change(i, unTableau.connaitre(i))
            nombre.change(i, 0)
            for j in range(unTableau.taille):
                if caractère.connaitre(i) == unTableau.connaitre(j):
                    nombre.change(i, nombre.connaitre(i) + 1)
    #endregion
    
    #region Taille de la liste (resultat)
    taille = 0
    for element in caractère.affichetout():
        if element != None:
            taille = taille + 1
    taille = taille * 2
    #endregion
    
    #region Afficher le résultat
    resultat = Tableau(taille)
    indice = 0
    for k in range(taille // 2):
        resultat.change(k + indice, caractère.connaitre(k))
        resultat.change(k + 1 + indice, nombre.connaitre(k))
        indice = indice + 1
    return resultat
    #endregion

#Question 2
#endregion

#region Execute
print("Fonction 1 :")
print(extraire2("Bonjour je suis nico").affichetout())

print("\r\nFonction 2 :")
print(occurence(extraire2("Bonjour je suis nico")).affichetout())
#endregion

