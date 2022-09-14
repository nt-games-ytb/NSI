#Chapitre 3 - Exercice 10

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