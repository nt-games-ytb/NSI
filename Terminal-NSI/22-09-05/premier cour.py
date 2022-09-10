#region Functions
def extraire(un_texte):
    resultat = []
    for c in un_texte:
        resultat.insert(len(resultat), c)
    print(resultat)#return resultat
    
def voyelle(une_liste):
    for c in une_liste:
        if c == "a" or c == "A" or c == "e" or c == "E" or c == "i" or c == "I" or c == "o" or c == "O" or c == "u" or c == "U" or c == "y" or c == "Y":
            print(c) 
            
            
def plus_grand(une_liste):
    plus_grand = 0
    for i in range(len(une_liste)):
        if plus_grand < une_liste[i]:
            plus_grand = une_liste[i]
    print("Le plus grand nombre est " + str(plus_grand))
#endregion

#region Execute
print("Fonction 1 :")
extraire("Bonjour")

print("\nFonction 2 :")
voyelle(["B", "o", "n", "j", "o", "u", "r"])

print("\nFonction 3 :")
plus_grand([1, 5, 9, 6])
#endregion