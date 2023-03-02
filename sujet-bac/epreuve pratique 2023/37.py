#Exercice 1
def recherche(elt, tab):
    indice = -1
    for i in range(len(tab)):
        if tab[i] == elt:
            indice = i
    return indice

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
        self.adresse = adresse
   
    def liste_octet(self):
        """renvoie une liste de nombres entiers,
           la liste des octets de l'adresse IP"""
        return [int(i) for i in self.adresse.split(".")] 
        
    def est_reservee(self):
        """renvoie True si l'adresse IP est une adresse
           reservee, False sinon"""
        return self.adresse == "192.168.0.0" or self.adresse == "192.168.0.255"
             
    def adresse_suivante(self):
        """renvoie un objet de AdresseIP avec l'adresse 
           IP qui suit l'adresse self
           si elle existe et False sinon"""
        if self.liste_octet()[-1] < 254:
            octet_nouveau = self.liste_octet()[-1] + 1
            return AdresseIP('192.168.0.' + str(octet_nouveau))
        else:
            return False

print("Exemple exercice 2 :")
adresse1, adresse2, adresse3 = AdresseIP('192.168.0.1'), AdresseIP('192.168.0.2'), AdresseIP('192.168.0.0')
print(adresse1.est_reservee())
print(adresse3.est_reservee())
print(adresse2.adresse_suivante().adresse)