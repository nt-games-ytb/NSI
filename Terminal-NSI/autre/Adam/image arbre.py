from PIL import Image
from PIL import ImageDraw
import structures

img=Image.new("RGB",(800,900))

imgdessin=ImageDraw.Draw(img)

for x in range(800):
    for y in range(900) :
        img.putpixel((x,y),(255,255,255))

def afficher_arbre(arbre):
    imgdessin.text((400,50), arbre.valeur, fill=(0,0,0))#premiere racine

    if arbre.gauche != None:
        imgdessin.line((400,50,200,150),fill=(0,0,0))#premier trait vers la gauche
        imgdessin.text((200,150),arbre.gauche.valeur, fill=(0,0,0))#racine gauche

        if arbre.gauche.gauche != None:
            imgdessin.line((200,150,100,300),fill=(0,0,0))#enfant gauche(vers la gauche)
            imgdessin.text((100,300),arbre.gauche.gauche.valeur, fill=(0,0,0))#racine enfant gauche

        if arbre.gauche.droit != None:
            imgdessin.line((200,150,250,300),fill=(0,0,0))#enfant gauche (vers la droite)
            imgdessin.text((250,300),arbre.gauche.droit.valeur, fill=(0,0,0))#racine enfant droit

    if arbre.droit != None:
        imgdessin.line((400,50,600,150),fill=(0,0,0))#premier trait droit
        imgdessin.text((600,150),arbre.droit.valeur, fill=(0,0,0))#racine droit

        if arbre.droit.gauche != None:
            imgdessin.line((600,150,700,300),fill=(0,0,0))#enfant droit (vers la gauche)
            imgdessin.text((550,300),arbre.droit.gauche.valeur, fill=(0,0,0))#racine enfant gauche

        if arbre.droit.droit != None:
            imgdessin.line((600,150,550,300),fill=(0,0,0))#enfant droit (vers la droite)
            imgdessin.text((700,300),arbre.droit.droit.valeur, fill=(0,0,0))#racine enfant droit
    
    img.show()

arbre_de_test = structures.ArbreBinaire("toto")

arbre_de_test.ajoutgauche("tata")
arbre_de_test.gauche.ajoutgauche("tantan")
arbre_de_test.gauche.ajoutdroit("furfur")

arbre_de_test.ajoutdroit("teitei")
arbre_de_test.droit.ajoutgauche("tete")
arbre_de_test.droit.ajoutdroit("tutur")

afficher_arbre(arbre_de_test)

