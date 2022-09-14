#Chapitre 3 - Exercice 7

#region Class
class File:
    def __init__(self):
        self.tablo = []

    def pousse(self, data):
        self.tablo = [data] + self.tablo
        #ou self.tablo.insert(0, data)

    def extraire(self):
        return self.tablo.pop()

    def vide(self):
        if self.tablo==[]:
            return True
        else:
            return False
        #ou return self.tablo==[]
            
    def nonvide(self):
        if self.tablo!=[]:
            return True
        else:
            return False
        #ou return self.tablo!=[]
#endregion