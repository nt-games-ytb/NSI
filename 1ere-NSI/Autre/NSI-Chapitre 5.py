voyelles=("a","e","i","o","u","y")

def compteVoyelle(texte):
    nbvoyelles=0
    for i in texte:
        if i.lower() in voyelles:
            nbvoyelles+=1
    return nbvoyelles

cartes={2:"2",3:"3",4:"4",5:"5",6:"6",9:"9",10:"10",11:"Valet",12:"Dame",13:"Roi",14:"As"}

dico={}

for i in range(2,11):
    dico[i]=str(i)

dico[11]="Valet"
dico[12]="Dame"
dico[13]="Roi"
dico[14]="As"

def batailles(nb1,nb2):
    print("Le joueur 1 a la carte",dico[nb1],".")
    print("Le joueur 2 a la carte",dico[nb2],".")
    if nb1==nb2:
        print("Égalité ! Les deux joueurs ont tous les deux la carte",dico[nb1],"!")
    elif nb1>nb2:
        print("Le joueurs 1 écrase l'adversaire' avec la carte",dico[nb1],"!")
    else:
        print("Le joueurs 2 domine avec la carte",dico[nb2],"!")
    
    