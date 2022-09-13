#Chapitre 3 - Exercice 6

#region Class
#Question 1
class Pile:
    def __init__(self):
        self.tablo = []


    def push(self, data):
        self.tablo.append(data)


    def pop(self):
        return self.tablo.pop()

    def vide(self):
        if self.tablo==[]:
            return True
        else:
            return False
            
    def nonvide(self):
        if self.tablo!=[]:
            return True
        else:
            return False
#endregion

#region Functions  
#Question 2
def caractereDansPile(texte):
    resultat = Pile()
    for i in range(len(texte)):
        resultat.push(texte[i])
    return resultat
    
#Question 3
def nbEspace(pile):
    '''
    INTERDICTION : utilise le .tablo
    '''
    resultat = 0
    #element = len(pile.tablo) - 1
    while pile.nonvide():
        #if pile.tablo[element] == " ":
        #    resultat = resultat + 1
        #element = element - 1
        #pile.pop()
        element = pile.pop()
        if element == " ":
            resulat = resultat + 1
    return resultat
#endregion

#region Execute
print("Fonction 1 :")
print(caractereDansPile("Ceci est un test").tablo)

print("\r\nFonction 2 :")
print(nbEspace(caractereDansPile("Ceci est un test")))
#endregion