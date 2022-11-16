import time
import os
#os.chdir("F:/TERMINALE/NSI/Chapitre 7")     #A modifier selon l'emplacement du dossier de "structures.py" (en caché
import structures
from PIL import Image
from PIL import ImageDraw


def crea_arbre_recherche_opti_BADLONG(liste):
    liste.sort() #tri la liste
    md=len(liste)//2 #md est la medianne de la liste
    arbre_sortie=structures.Arbre_Binaire(liste[md]) #on creer un arbre dont la racine est md
    file=structures.File()
    file.push(liste[:md])
    file.push(liste[md+1:])
    while file.nonvide():
        a=file.pop()
        if a==[]:
            pass
        if len(a)==1:
            structures.ajout_valeur(arbre_sortie,a[0])
        elif len(a)==2:
            structures.ajout_valeur(arbre_sortie,a[0])
            structures.ajout_valeur(arbre_sortie,a[1])
        else:
            md=len(a)//2
            structures.ajout_valeur(arbre_sortie,a[md])
            file.push(a[:md])
            file.push(a[md+1:])
    return arbre_sortie


import random
liste_nb=[]
for i in range(100000):
    liste_nb.append(random.randint(1,1000000000))



arbre_nbalea=crea_arbre_recherche_opti_BADLONG(liste_nb)


arbre1=structures.Arbre_Binaire('Toto')
#
#
arbre1.ajout_gauche('Tantan')
#
arbre1.gauche.ajout_gauche('Titi')
arbre1.gauche.gauche.ajout_gauche('Tata')
arbre1.gauche.gauche.ajout_droit('Tonton')
#
arbre1.gauche.ajout_droit('Tutu')
arbre1.gauche.droit.ajout_gauche('Tiktik')
arbre1.gauche.droit.ajout_droit('Tiktok')
#
#
arbre1.ajout_droit('Tintin')
#
arbre1.droit.ajout_gauche('Furfur')
arbre1.droit.gauche.ajout_gauche('Tictac')
arbre1.droit.gauche.ajout_droit('tactic')
#
arbre1.droit.ajout_droit('Teitei')
arbre1.droit.droit.ajout_gauche('Tojtoj')
arbre1.droit.droit.ajout_droit('Tete')

p=structures.Pile()

f=structures.File()

def image_arbre(arbre):
    '''
    Ce programme prend comme argument un arbre et renvoie l'image de cet arbre puis enregistre cette image dans le dossier du fichier.
    '''

    img=Image.new("RGB",(800,900))              #   /
    imgdessin=ImageDraw.Draw(img)               #  (
    for x in range(800):                        # <  - On définit le format de l'image
        for y in range(900):                    #  (
            img.putpixel((x,y),(255,255,255))   #   \

    if arbre!=None:
        imgdessin.text((390,40),str(arbre.valeur).lower(),fill=(0,0,0))  #Si l'arbre n'est pas vide, on affiche sa racine

    if arbre.gauche!=None:
        imgdessin.line((400,50,250,150), fill=(0,0,0))
        imgdessin.text((230,150),str(arbre.gauche.valeur).lower(),fill=(0,0,0))  #Enfant gauche

        if arbre.gauche.gauche!=None:
            imgdessin.line((250,160,175,250), fill=(0,0,0))
            imgdessin.text((160,250),str(arbre.gauche.gauche.valeur).lower(),fill=(0,0,0)) #Enfant gauche du sous arbre gauche

            if arbre.gauche.gauche.gauche!=None:
                imgdessin.line((175,260,137.5,350), fill=(0,0,0))
                imgdessin.text((127.5,350),str(arbre.gauche.gauche.gauche.valeur).lower(),fill=(0,0,0)) #Enfant gauche du sous arbre gauche du sous arbre gauche

            if arbre.gauche.gauche.droit!=None:
                imgdessin.line((175,260,212.5,350), fill=(0,0,0))
                imgdessin.text((192.5,350),str(arbre.gauche.gauche.droit.valeur).lower(),fill=(0,0,0)) #Enfant droit du sous arbre gauche du sous arbre gauche

        if arbre.gauche.droit!=None:
            imgdessin.line((250,160,325,250), fill=(0,0,0))
            imgdessin.text((315,250),str(arbre.gauche.droit.valeur).lower(),fill=(0,0,0)) #Enfant droit du sous arbre gauche

            if arbre.gauche.droit.gauche!=None:
                imgdessin.line((327,260,289.5,350), fill=(0,0,0))
                imgdessin.text((269.5,350),str(arbre.gauche.droit.gauche.valeur).lower(),fill=(0,0,0)) #Enfant gauche du sous arbre droit du sous arbre gauche

            if arbre.gauche.droit.droit!=None:
                imgdessin.line((327,260,364.5,350), fill=(0,0,0))
                imgdessin.text((344.5,350),str(arbre.gauche.droit.droit.valeur).lower(),fill=(0,0,0)) #Enfant droit du sous arbre droit du sous arbre gauche

    if arbre.droit!=None:
        imgdessin.line((400,50,550,150), fill=(0,0,0))
        imgdessin.text((530,150),str(arbre.droit.valeur).lower(),fill=(0,0,0)) #Enfant droit

        if arbre.droit.gauche!=None:
            imgdessin.line((550,160,475,250), fill=(0,0,0))
            imgdessin.text((460,250),str(arbre.droit.gauche.valeur).lower(),fill=(0,0,0)) #Enfant gauche du sous arbre droit

            if arbre.droit.gauche.gauche!=None:
                imgdessin.line((477,260,439.5,350), fill=(0,0,0))
                imgdessin.text((419.5,350),str(arbre.droit.gauche.gauche.valeur).lower(),fill=(0,0,0)) #Enfant gauche du sous arbre gauche du sous arbre droit

            if arbre.droit.gauche.droit!=None:
                imgdessin.line((477,260,510.5,350), fill=(0,0,0))
                imgdessin.text((490.5,350),str(arbre.droit.gauche.droit.valeur).lower(),fill=(0,0,0)) #Enfant droit du sous arbre gauche du sous arbre droit

        if arbre.droit.droit!=None:
            imgdessin.line((550,160,625,250), fill=(0,0,0))
            imgdessin.text((610,250),str(arbre.droit.droit.valeur).lower(),fill=(0,0,0)) #Enfant droit du sous arbre droit

            if arbre.droit.droit.gauche!=None:
                imgdessin.line((627,260,589.5,350), fill=(0,0,0))
                imgdessin.text((569.5,350),str(arbre.droit.droit.gauche.valeur).lower(),fill=(0,0,0)) #Enfant gauche du sous arbre droit du sous arbre droit

            if arbre.droit.droit.droit!=None:
                imgdessin.line((627,260,660.5,350), fill=(0,0,0))
                imgdessin.text((650.5,350),str(arbre.droit.droit.droit.valeur).lower(),fill=(0,0,0)) #Enfant droit du sous arbre droit du sous arbre droit

    for i in range(2):      #
        for w in range(75): #
            print("")       #
        print("LOADING.")   #
        time.sleep(1)       #
        for x in range(75): #
            print("")       #   Chargement
        print("LOADING..")  #
        time.sleep(1)       #
        for y in range(75): #
            print("")       #
        print("LOADING...") #
        for z in range(75): #
            print("")       #

    img.show()              #Affiche l'image

    time.sleep(1.5)
    for i in range(3):
        print("")

    ctrl_s=input(" - Voulez-vous enregistrer l'image de l'arbre ? (OUI/NON) - ") #Question pour savoir si l'on veut enregister l'image ou non
    assert ctrl_s.lower()=="oui" or ctrl_s.lower()=="non" ,"Il s'agit d'une question fermée"
    if ctrl_s.lower()=="oui":
        for w in range(75): #
            print("")       #
        print("LOADING.")   #
        time.sleep(1)       #
        for x in range(75): #
            print("")       #   Chargement
        print("LOADING..")  #
        time.sleep(1)       #
        for y in range(75): #
            print("")       #
        print("LOADING...") #
        for z in range(75): #
            print("")       #
        for i in range(3):
            print("")
        nom=input(" - Comment voulez-vous nommer cette image ? - ") #On définit le nom qui sera utilsé pour enregistrer l'image
        time.sleep(1)
        for w in range(75): #
            print("")       #
        print("LOADING.")   #
        time.sleep(1)       #
        for x in range(75): #
            print("")       #   Chargement
        print("LOADING..")  #
        time.sleep(1)       #
        for y in range(75): #
            print("")       #
        format=input(" - Sous quel format voulez-vous que l'image soit enregistree ? (PNG/JPG/JPEG) - ") #Format utilisé pour enregistrer l'image
        for w in range(75): #
            print("")       #
        print("LOADING.")   #
        time.sleep(1)       #
        for x in range(75): #
            print("")       #   Chargement
        print("LOADING..")  #
        time.sleep(1)       #
        for y in range(75): #
            print("")       #
        print("LOADING...") #
        for z in range(75): #
            print("")       #
        for i in range(3):
            print("")
        assert format.lower()=='png' or format.lower()=='jpg' or format.lower()=='jpeg' ,'le format doit être un de ceux proposés entre parenthèses'
        img.save(nom+"."+format.lower())     #Enregistre l'image dans le dossier ciblé avec le nom définit plus tôt
        for i in range(3):
            print("")
        print("✔️ Vous avez enregistré l'image") #Tout est dit
    elif ctrl_s.lower()=="non":
        for w in range(75): #
            print("")       #
        print("LOADING.")   #
        time.sleep(1)       #
        for x in range(75): #
            print("")       #   Chargement
        print("LOADING..")  #
        time.sleep(1)       #
        for y in range(75): #
            print("")       #
        print("LOADING...") #
        for z in range(75): #
            print("")       #
        for i in range(5):
            print("")
        print("❌ Vous n'avez pas enregistré l'image") #Tout est dit



image_arbre(arbre1) #A modifier avec l'arbre que'on veut afficher