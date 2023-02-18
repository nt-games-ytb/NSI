#Exercice 1

print("Exemple exercice 1 :")
print(recherche(1,[2,3,4]))
print(recherche(1,[10,12,1,56]))
print(recherche(1, [1, 0, 42, 7]))
print(recherche(1,[1,50,1]))
print(recherche(1,[8,1,10,1,7,1,8]))
print()



#Exerice 2
class AdresseIP:

    def __init__(self, adresse):
        self.adresse = ...
   
    def liste_octet(self):
        """renvoie une liste de nombres entiers,
           la liste des octets de l'adresse IP"""
        return [int(i) for i in self.adresse.split(".")] 
        
    def est_reservee(self):
        """renvoie True si l'adresse IP est une adresse
           reservee, False sinon"""
        return ... or ...
             
    def adresse_suivante(self):
        """renvoie un objet de AdresseIP avec l'adresse 
           IP qui suit l'adresse self
           si elle existe et False sinon"""
        if ... < 254:
            octet_nouveau = ... + ...
            return AdresseIP('192.168.0.' + ...)
        else:
            return False

print("Exemple exercice 2 :")
adresse1, adresse2, adresse3 = '192.168.0.1', '192.168.0.2', '192.168.0.0'
print(adresse1.est_reservee())
print(adresse3.est_reservee())
print(adresse2.adresse_suivante().adresse)