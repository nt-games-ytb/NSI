#Chapitre 3 - Exercice 7

#region Class
class File:
    def __init__(self):
        self.stockage = []

    def pousse(self, donnee):
        self.stockage.insert(0, donnee)

    def extraire(self):
        return self.stockage.pop()

    def vide(self):
        return self.stockage==[]
            
    def nonvide(self):
        return self.stockage!=[]
#endregion

#region Functions
#Question 1
def extraire(UnTexte):
    resultat = File()
    for c in UnTexte:
        resultat.pousse(c)
    return resultat

#Question 2
def voyelle(UneFile):
    while UneFile.nonvide():
        c = UneFile.extraire()
        if c == "a" or c == "A" or c == "e" or c == "E" or c == "i" or c == "I" or c == "o" or c == "O" or c == "u" or c == "U" or c == "y" or c == "Y":
            print(c) 
            
#☻Question 3
'''
QUESTION : 
Creer une fonction  qui prend une file qui contient des nombres et renvoie le plus grand nombre de la file
'''
def plus_grand(UneFile):
    plus_grand = UneFile.stockage[0]
    while UneFile.nonvide():
        nombre = UneFile.extraire()
        if plus_grand < nombre:
            plus_grand = nombre
    return "Le plus grand nombre est " + str(plus_grand)
#endregion

#region Execute
print("Fonction 1 :")
print(extraire("Bonjour").stockage)

print("\nFonction 2 :")
voyelle(extraire("Bonjour"))

print("\nFonction 3 :")
test = File()
test.pousse(1)
test.pousse(5)
test.pousse(9)
test.pousse(6)
print(plus_grand(test))
#endregion