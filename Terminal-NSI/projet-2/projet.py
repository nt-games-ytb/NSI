# Copyright © by Sergio BIOLAY-SEGURA and Nicolas TORO

#region Import
from PIL import Image
from PIL import ImageDraw, ImageFont
import os
#Sergio : os.chdir("D:/NSI/Terminale NSI/Chapitre 7")
#Nicolas : os.chdir("H:/NSI/Terminal-NSI/projet-2")
import structures
#endregion

#region Couleur
r_fond = 255
v_fond = 255
b_fond = 255

r_ligne_gauche = 255
v_ligne_gauche = 0
b_ligne_gauche = 0

r_ligne_droite = 0
v_ligne_droite = 0
b_ligne_droite = 255
#endregion

#region Fonctions
def milieu_texte(texte):
    '''Une fonction qui prend comme argument un texte et qui renvoie en fonctionne du nombre de caractère, un integer qui aura pour but de centrer le texte.'''
    return len(texte) * 5 / 2

def creation_arbre(arbre):
    '''Une fonction qui prend comme argument un arbre binaire et qui va déssiner les noeuds et les lignes des qui relient chaque noeuds de l'arbres sur une image.'''
    #Les commentaires sont les noeuds établit en fonction de "arbre_test"

    police = ImageFont.truetype(nom_de_la_police, size=12)

    #toto
    imgdessin.text((400 - milieu_texte(arbre.valeur), 40), str(arbre.valeur), fill=(0,0,0), font=police)

    if arbre.gauche != None:#tata
        imgdessin.line((400, 60, 200, 160), fill=(r_ligne_gauche, v_ligne_gauche, b_ligne_gauche))
        imgdessin.text((200 - milieu_texte(arbre.gauche.valeur), 160), str(arbre.gauche.valeur), fill=(0,0,0), font=police)

        if arbre.gauche.gauche != None:#titi
            imgdessin.line((200, 175, 100, 325), fill=(r_ligne_gauche, v_ligne_gauche, b_ligne_gauche))
            imgdessin.text((100 - milieu_texte(arbre.gauche.gauche.valeur), 325), str(arbre.gauche.gauche.valeur), fill=(0,0,0), font=police)

            if arbre.gauche.gauche.gauche != None:#teitei
                imgdessin.line((100, 340, 50, 490), fill=(r_ligne_gauche, v_ligne_gauche, b_ligne_gauche))
                imgdessin.text((50 - milieu_texte(arbre.gauche.gauche.gauche.valeur), 490), str(arbre.gauche.gauche.gauche.valeur), fill=(0,0,0), font=police)

                if arbre.gauche.gauche.gauche.gauche != None:#tritri
                    imgdessin.line((50, 505, 25, 655), fill=(r_ligne_gauche, v_ligne_gauche, b_ligne_gauche))
                    imgdessin.text((25 - milieu_texte(arbre.gauche.gauche.gauche.gauche.valeur), 655), str(arbre.gauche.gauche.gauche.gauche.valeur), fill=(0,0,0), font=police)

                if arbre.gauche.gauche.gauche.droit != None:#totop
                    imgdessin.line((50, 505, 75, 655), fill=(r_ligne_droite, v_ligne_droite, b_ligne_droite))
                    imgdessin.text((75 - milieu_texte(arbre.gauche.gauche.gauche.droit.valeur), 655), str(arbre.gauche.gauche.gauche.droit.valeur), fill=(0,0,0), font=police)

            if arbre.gauche.gauche.droit != None:#tojtoj
                imgdessin.line((100, 340, 150, 490), fill=(r_ligne_droite, v_ligne_droite, b_ligne_droite))
                imgdessin.text((150 - milieu_texte(arbre.gauche.gauche.droit.valeur), 490), str(arbre.gauche.gauche.droit.valeur), fill=(0,0,0), font=police)

                if arbre.gauche.gauche.droit.gauche != None:#terter
                    imgdessin.line((150, 505, 125, 655), fill=(r_ligne_gauche, v_ligne_gauche, b_ligne_gauche))
                    imgdessin.text((125 - milieu_texte(arbre.gauche.gauche.droit.gauche.valeur), 655), str(arbre.gauche.gauche.droit.gauche.valeur), fill=(0,0,0), font=police)

                if arbre.gauche.gauche.droit.droit != None:#tetez
                    imgdessin.line((150, 505, 175, 655), fill=(r_ligne_droite, v_ligne_droite, b_ligne_droite))
                    imgdessin.text((175 - milieu_texte(arbre.gauche.gauche.droit.droit.valeur), 655), str(arbre.gauche.gauche.droit.droit.valeur), fill=(0,0,0), font=police)

        if arbre.gauche.droit != None:#toto
            imgdessin.line((200, 175, 300, 325), fill=(r_ligne_droite, v_ligne_droite, b_ligne_droite))
            imgdessin.text((300 - milieu_texte(arbre.gauche.droit.valeur), 325), str(arbre.gauche.droit.valeur), fill=(0,0,0), font=police)

            if arbre.gauche.droit.gauche != None:#tyty
                imgdessin.line((300, 340, 250, 490), fill=(r_ligne_gauche, v_ligne_gauche, b_ligne_gauche))
                imgdessin.text((250 - milieu_texte(arbre.gauche.droit.gauche.valeur), 490), str(arbre.gauche.droit.gauche.valeur), fill=(0,0,0), font=police)

                if arbre.gauche.droit.gauche.gauche != None:#tihtih
                    imgdessin.line((250, 505, 225, 655), fill=(r_ligne_gauche, v_ligne_gauche, b_ligne_gauche))
                    imgdessin.text((225 - milieu_texte(arbre.gauche.droit.gauche.gauche.valeur), 655), str(arbre.gauche.droit.gauche.gauche.valeur), fill=(0,0,0), font=police)

                if arbre.gauche.droit.gauche.droit != None:#toutou
                    imgdessin.line((250, 505, 275, 655), fill=(r_ligne_droite, v_ligne_droite, b_ligne_droite))
                    imgdessin.text((275 - milieu_texte(arbre.gauche.droit.gauche.droit.valeur), 655), str(arbre.gauche.droit.gauche.droit.valeur), fill=(0,0,0), font=police)

            if arbre.gauche.droit.droit != None:#trotro
                imgdessin.line((300, 340, 350, 490), fill=(r_ligne_droite, v_ligne_droite, b_ligne_droite))
                imgdessin.text((350 - milieu_texte(arbre.gauche.droit.droit.valeur), 490), str(arbre.gauche.droit.droit.valeur), fill=(0,0,0), font=police)

                if arbre.gauche.droit.droit.gauche != None:#turtur
                    imgdessin.line((350, 505, 325, 655), fill=(r_ligne_gauche, v_ligne_gauche, b_ligne_gauche))
                    imgdessin.text((325 - milieu_texte(arbre.gauche.droit.droit.gauche.valeur), 655), str(arbre.gauche.droit.droit.gauche.valeur), fill=(0,0,0), font=police)

                if arbre.gauche.droit.droit.droit != None:#topto
                    imgdessin.line((350, 505, 375, 655), fill=(r_ligne_droite, v_ligne_droite, b_ligne_droite))
                    imgdessin.text((375 - milieu_texte(arbre.gauche.droit.droit.droit.valeur), 655), str(arbre.gauche.droit.droit.droit.valeur), fill=(0,0,0), font=police)

    if arbre.droit != None:#tantan
        imgdessin.line((400, 60, 600, 160),fill=(r_ligne_droite, v_ligne_droite, b_ligne_droite))
        imgdessin.text((600 - milieu_texte(arbre.droit.valeur), 160), str(arbre.droit.valeur), fill=(0,0,0), font=police)

        if arbre.droit.gauche != None:#tintin
            imgdessin.line((600, 175, 500, 325),fill=(r_ligne_gauche, v_ligne_gauche, b_ligne_gauche))
            imgdessin.text((500 - milieu_texte(arbre.droit.gauche.valeur), 325), str(arbre.droit.gauche.valeur), fill=(0,0,0), font=police)

            if arbre.droit.gauche.gauche != None:#tiftif
                imgdessin.line((500, 340, 450, 490), fill=(r_ligne_gauche, v_ligne_gauche, b_ligne_gauche))
                imgdessin.text((450 - milieu_texte(arbre.droit.gauche.gauche.valeur), 490), str(arbre.droit.gauche.gauche.valeur), fill=(0,0,0), font=police)

                if arbre.droit.gauche.gauche.gauche != None:#tamtam
                    imgdessin.line((450, 505, 425, 655), fill=(r_ligne_gauche, v_ligne_gauche, b_ligne_gauche))
                    imgdessin.text((425 - milieu_texte(arbre.droit.gauche.gauche.gauche.valeur), 655), str(arbre.droit.gauche.gauche.gauche.valeur), fill=(0,0,0), font=police)

                if arbre.droit.gauche.gauche.droit != None:#toumtoum
                    imgdessin.line((450, 505, 475, 655), fill=(r_ligne_droite, v_ligne_droite, b_ligne_droite))
                    imgdessin.text((475 - milieu_texte(arbre.droit.gauche.gauche.droit.valeur), 655), str(arbre.droit.gauche.gauche.droit.valeur), fill=(0,0,0), font=police)

            if arbre.droit.gauche.droit != None:#touftouf
                imgdessin.line((500, 340, 550, 490), fill=(r_ligne_droite, v_ligne_droite, b_ligne_droite))
                imgdessin.text((550 - milieu_texte(arbre.droit.gauche.droit.valeur), 490), str(arbre.droit.gauche.droit.valeur), fill=(0,0,0), font=police)

                if arbre.droit.gauche.droit.gauche != None:#totol
                    imgdessin.line((550, 505, 525, 655), fill=(r_ligne_gauche, v_ligne_gauche, b_ligne_gauche))
                    imgdessin.text((525 - milieu_texte(arbre.droit.gauche.droit.gauche.valeur), 655), str(arbre.droit.gauche.droit.gauche.valeur), fill=(0,0,0), font=police)

                if arbre.droit.gauche.droit.droit != None:#tytyl
                    imgdessin.line((550, 505, 575, 655), fill=(r_ligne_droite, v_ligne_droite, b_ligne_droite))
                    imgdessin.text((575 - milieu_texte(arbre.droit.gauche.droit.droit.valeur), 655), str(arbre.droit.gauche.droit.droit.valeur), fill=(0,0,0), font=police)

        if arbre.droit.droit != None:#tutu
            imgdessin.line((600, 175, 700, 325),fill=(r_ligne_droite, v_ligne_droite, b_ligne_droite))
            imgdessin.text((700 - milieu_texte(arbre.droit.droit.valeur), 325), str(arbre.droit.droit.valeur), fill=(0,0,0), font=police)

            if arbre.droit.droit.gauche != None:#tortor
                imgdessin.line((700, 340, 650, 490), fill=(r_ligne_gauche, v_ligne_gauche, b_ligne_gauche))
                imgdessin.text((650 - milieu_texte(arbre.droit.droit.gauche.valeur), 490), str(arbre.droit.droit.gauche.valeur), fill=(0,0,0), font=police)

                if arbre.droit.droit.gauche.gauche != None:#a
                    imgdessin.line((650, 505, 625, 655), fill=(r_ligne_gauche, v_ligne_gauche, b_ligne_gauche))
                    imgdessin.text((625 - milieu_texte(arbre.droit.droit.gauche.gauche.valeur), 655), str(arbre.droit.droit.gauche.gauche.valeur), fill=(0,0,0), font=police)

                if arbre.droit.droit.gauche.droit != None:#b
                    imgdessin.line((650, 505, 675, 655), fill=(r_ligne_droite, v_ligne_droite, b_ligne_droite))
                    imgdessin.text((675 - milieu_texte(arbre.droit.droit.gauche.droit.valeur), 655), str(arbre.droit.droit.gauche.droit.valeur), fill=(0,0,0), font=police)

            if arbre.droit.droit.droit != None:#tirtir
                imgdessin.line((700, 340, 750, 490), fill=(r_ligne_droite, v_ligne_droite, b_ligne_droite))
                imgdessin.text((750 - milieu_texte(arbre.droit.droit.droit.valeur), 490), str(arbre.droit.droit.droit.valeur), fill=(0,0,0), font=police)

                if arbre.droit.droit.droit.gauche != None:#c
                    imgdessin.line((750, 505, 725, 655), fill=(r_ligne_gauche, v_ligne_gauche, b_ligne_gauche))
                    imgdessin.text((725 - milieu_texte(arbre.droit.droit.droit.gauche.valeur), 655), str(arbre.droit.droit.droit.gauche.valeur), fill=(0,0,0), font=police)

                if arbre.droit.droit.droit.droit != None:#d
                    imgdessin.line((750, 505, 775, 655), fill=(r_ligne_droite, v_ligne_droite, b_ligne_droite))
                    imgdessin.text((775 - milieu_texte(arbre.droit.droit.droit.droit.valeur), 655), str(arbre.droit.droit.droit.droit.valeur), fill=(0,0,0), font=police)

def options_suppplementaire(arbre):
    '''Une fonction qui prend comme argument un arbre et qui permet de déssiner sur une image la taille, la hauteur et le nombre de feuille de l'arbre.'''

    police = ImageFont.truetype(nom_de_la_police, size=25)
    imgdessin.text((50, 775), "Taille : " + str(structures.taille(arbre)), fill=(0,0,0), font=police)
    imgdessin.text((50, 800), "Hauteur : " + str(structures.hauteur(arbre)), fill=(0,0,0), font=police)
    imgdessin.text((50, 825), "Nombre de feuille : " + str(structures.nb_feuille(arbre)), fill=(0,0,0), font=police)

def liste_prefixe(liste, arbre):
    '''Une fonction qui prend comme argument un arbre binaire et une liste qu'il va remplir avec tous les noeuds d'un tableau dans l'odre préfixe.'''

    if arbre == None:
        pass
    else:
        liste.append(arbre.valeur)
        liste_prefixe(liste, arbre.gauche)
        liste_prefixe(liste, arbre.droit)

def supprime_noeud(arbre, numéro_de_valeur):
    '''Une fonction qui prend comme argument un arbre binaire et un integer (numéro_de_valeur), qui va suppimé la valeur indiquer en fonction de numéro_de_valeur et qui va renvoyer la valeur supprimé.'''

    #assert type(arbre) != int, "Votre réponse doit être un chiffre !"
    #assert numéro_de_valeur > 0, "Votre réponse doit être positif !"
    #assert numéro_de_valeur <= structures.taille(arbre), "Votre réponse ne doit pas être plus grand que la taille de l'arbre !"

    if numéro_de_valeur == 0:
        print("La racine de l'arbre va être supprimé, donc l'abre sera supprimé, êtes-vous sur de faire cela ?")
        print("1 - Oui | 2 - Non")
        choix_supprime_arbre = input()
        if choix_supprime_arbre == "1":
            arbre = None
            return "L'abre"

        if choix_supprime_arbre == "1":
            return "Aucun noeuds"

        else:
            print("Choix inconnu !")
            return "Aucun noeuds"

    else:
        numéro = 1
        if arbre.gauche != None:#tata
            if numéro == numéro_de_valeur:
                valeur_supprimé = arbre.gauche.valeur
                arbre.gauche = None
                return valeur_supprimé
            else:
                numéro = numéro + 1

            if arbre.gauche.gauche != None:#titi
                if numéro == numéro_de_valeur:
                    valeur_supprimé = arbre.gauche.gauche.valeur
                    arbre.gauche.gauche = None
                    return valeur_supprimé
                else:
                    numéro = numéro + 1

                if arbre.gauche.gauche.gauche != None:#teitei
                    if numéro == numéro_de_valeur:
                        valeur_supprimé = arbre.gauche.gauche.gauche.valeur
                        arbre.gauche.gauche.gauche = None
                        return valeur_supprimé
                    else:
                        numéro = numéro + 1

                    if arbre.gauche.gauche.gauche.gauche != None:#tritri
                        if numéro == numéro_de_valeur:
                            valeur_supprimé = arbre.gauche.gauche.gauche.gauche.valeur
                            arbre.gauche.gauche.gauche.gauche = None
                            return valeur_supprimé
                        else:
                            numéro = numéro + 1

                    if arbre.gauche.gauche.gauche.droit != None:#totop
                        if numéro == numéro_de_valeur:
                            valeur_supprimé = arbre.gauche.gauche.gauche.droit.valeur
                            arbre.gauche.gauche.gauche.droit = None
                            return valeur_supprimé
                        else:
                            numéro = numéro + 1

                if arbre.gauche.gauche.droit != None:#tojtoj
                    if numéro == numéro_de_valeur:
                        valeur_supprimé = arbre.gauche.gauche.droit.valeur
                        arbre.gauche.gauche.droit = None
                        return valeur_supprimé
                    else:
                        numéro = numéro + 1

                    if arbre.gauche.gauche.droit.gauche != None:#terter
                        if numéro == numéro_de_valeur:
                            valeur_supprimé = arbre.gauche.gauche.droit.gauche.valeur
                            arbre.gauche.gauche.droit.gauche  = None
                            return valeur_supprimé
                        else:
                            numéro = numéro + 1

                    if arbre.gauche.gauche.droit.droit != None:#tetez
                        if numéro == numéro_de_valeur:
                            valeur_supprimé = arbre.gauche.gauche.droit.droit.valeur
                            arbre.gauche.gauche.droit.droit = None
                            return valeur_supprimé
                        else:
                            numéro = numéro + 1

            if arbre.gauche.droit != None:#toto
                if numéro == numéro_de_valeur:
                    valeur_supprimé = arbre.gauche.droit.valeur
                    arbre.gauche.droit = None
                    return valeur_supprimé
                else:
                    numéro = numéro + 1

                if arbre.gauche.droit.gauche != None:#tyty
                    if numéro == numéro_de_valeur:
                        valeur_supprimé = arbre.gauche.droit.gauche.valeur
                        arbre.gauche.droit.gauche = None
                        return valeur_supprimé
                    else:
                        numéro = numéro + 1

                    if arbre.gauche.droit.gauche.gauche != None:#tihtih
                        if numéro == numéro_de_valeur:
                            valeur_supprimé = arbre.gauche.droit.gauche.gauche.valeur
                            arbre.gauche.droit.gauche.gauche = None
                            return valeur_supprimé
                        else:
                            numéro = numéro + 1

                    if arbre.gauche.droit.gauche.droit != None:#toutou
                        if numéro == numéro_de_valeur:
                            valeur_supprimé = arbre.gauche.droit.gauche.droit.valeur
                            arbre.gauche.droit.gauche.droit = None
                            return valeur_supprimé
                        else:
                            numéro = numéro + 1

                if arbre.gauche.droit.droit != None:#trotro
                    if numéro == numéro_de_valeur:
                        valeur_supprimé = arbre.gauche.droit.droit.valeur
                        arbre.gauche.droit.droit = None
                        return valeur_supprimé
                    else:
                        numéro = numéro + 1

                    if arbre.gauche.droit.droit.gauche != None:#turtur
                        if numéro == numéro_de_valeur:
                            valeur_supprimé = arbre.gauche.droit.droit.gauche.valeur
                            arbre.gauche.droit.droit.gauche = None
                            return valeur_supprimé
                        else:
                            numéro = numéro + 1

                    if arbre.gauche.droit.droit.droit != None:#topto
                        if numéro == numéro_de_valeur:
                            valeur_supprimé = arbre.gauche.droit.droit.droit.valeur
                            arbre.gauche.droit.droit.droit = None
                            return valeur_supprimé
                        else:
                            numéro = numéro + 1

        if arbre.droit != None:#tantan
            if numéro == numéro_de_valeur:
                valeur_supprimé = arbre.droit.valeur
                arbre.droit = None
                return valeur_supprimé
            else:
                numéro = numéro + 1

            if arbre.droit.gauche != None:#tintin
                if numéro == numéro_de_valeur:
                    valeur_supprimé = arbre.droit.gauche.valeur
                    arbre.droit.gauche = None
                    return valeur_supprimé
                else:
                    numéro = numéro + 1

                if arbre.droit.gauche.gauche != None:#tiftif
                    if numéro == numéro_de_valeur:
                        valeur_supprimé = arbre.droit.gauche.gauche.valeur
                        arbre.droit.gauche.gauche = None
                        return valeur_supprimé
                    else:
                        numéro = numéro + 1

                    if arbre.droit.gauche.gauche.gauche != None:#tamtam
                        if numéro == numéro_de_valeur:
                            valeur_supprimé = arbre.droit.gauche.gauche.gauche.valeur
                            arbre.droit.gauche.gauche.gauche = None
                            return valeur_supprimé
                        else:
                            numéro = numéro + 1

                    if arbre.droit.gauche.gauche.droit != None:#toumtoum
                        if numéro == numéro_de_valeur:
                            valeur_supprimé = arbre.droit.gauche.gauche.droit.valeur
                            arbre.droit.gauche.gauche.droit = None
                            return valeur_supprimé
                        else:
                            numéro = numéro + 1

                if arbre.droit.gauche.droit != None:#touftouf
                    if numéro == numéro_de_valeur:
                        valeur_supprimé = arbre.droit.gauche.droit.valeur
                        arbre.droit.gauche.droit = None
                        return valeur_supprimé
                    else:
                            numéro = numéro + 1

                    if arbre.droit.gauche.droit.gauche != None:#totol
                        if numéro == numéro_de_valeur:
                            valeur_supprimé = arbre.droit.gauche.droit.gauche.valeur
                            arbre.droit.gauche.droit.gauche = None
                            return valeur_supprimé
                        else:
                            numéro = numéro + 1

                    if arbre.droit.gauche.droit.droit != None:#tytyl
                        if numéro == numéro_de_valeur:
                            valeur_supprimé = arbre.droit.gauche.droit.droit.valeur
                            arbre.droit.gauche.droit.droit = None
                            return valeur_supprimé
                        else:
                            numéro = numéro + 1

            if arbre.droit.droit != None:#tutu
                if numéro == numéro_de_valeur:
                    valeur_supprimé = arbre.droit.droit.valeur
                    arbre.droit.droit = None
                    return valeur_supprimé
                else:
                    numéro = numéro + 1

                if arbre.droit.droit.gauche != None:#tortor
                    if numéro == numéro_de_valeur:
                        valeur_supprimé = arbre.droit.droit.valeur
                        arbre.droit.droit.gauche = None
                        return valeur_supprimé
                    else:
                        numéro = numéro + 1

                    if arbre.droit.droit.gauche.gauche != None:#a
                        if numéro == numéro_de_valeur:
                            valeur_supprimé = arbre.droit.droit.gauche.gauche.valeur
                            arbre.droit.droit.gauche.gauche = None
                            return valeur_supprimé
                        else:
                            numéro = numéro + 1

                    if arbre.droit.droit.gauche.droit != None:#b
                        if numéro == numéro_de_valeur:
                            valeur_supprimé = arbre.droit.droit.gauche.droit.valeur
                            arbre.droit.droit.gauche.droit = None
                            return valeur_supprimé
                        else:
                            numéro = numéro + 1

                if arbre.droit.droit.droit != None:#tirtir
                    if numéro == numéro_de_valeur:
                        valeur_supprimé = arbre.droit.droit.droit.valeur
                        arbre.droit.droit.droit = None
                        return valeur_supprimé
                    else:
                        numéro = numéro + 1

                    if arbre.droit.droit.droit.gauche != None:#c
                        if numéro == numéro_de_valeur:
                            valeur_supprimé = arbre.droit.droit.droit.gauche.valeur
                            arbre.droit.droit.droit.gauche = None
                            return valeur_supprimé
                        else:
                            numéro = numéro + 1

                    if arbre.droit.droit.droit.droit != None:#d
                        if numéro == numéro_de_valeur:
                            valeur_supprimé = arbre.droit.droit.droit.droit.valeur
                            arbre.droit.droit.droit.droit = None
                            return valeur_supprimé
                        else:
                            numéro = numéro + 1

def enfant_possible(arbre):
    '''Une fonction qui prend comme argument un arbre binaire et qui va renvoyer la liste de noeuds ajoutable dans l'arbre (avec un maximum de 5 de hauteur).'''
    liste = []

    #region sous-arbre gauche
    if arbre.gauche == None:
        liste.append("gauche")

    else:
        if arbre.gauche.gauche == None:
            liste.append("gauche.gauche")

        else:
            if arbre.gauche.gauche.gauche == None:
                liste.append("gauche.gauche.gauche")

            else:
                if arbre.gauche.gauche.gauche.gauche == None:
                    liste.append("gauche.gauche.gauche.gauche")

                if arbre.gauche.gauche.gauche.droit == None:
                    liste.append("gauche.gauche.gauche.droit")

            if arbre.gauche.gauche.droit == None:
                liste.append("gauche.gauche.droit")

            else:
                if arbre.gauche.gauche.droit.gauche == None:
                    liste.append("gauche.gauche.droit.gauche")

                if arbre.gauche.gauche.droit.droit == None:
                    liste.append("gauche.gauche.droit.droit")

        if arbre.gauche.droit == None:
            liste.append("gauche.droit")

        else:
            if arbre.gauche.droit.gauche == None:
                liste.append("gauche.droit.gauche")

            else:
                if arbre.gauche.droit.gauche.gauche == None:
                    liste.append("gauche.droit.gauche.gauche")

                if arbre.gauche.droit.gauche.droit == None:
                    liste.append("gauche.droit.gauche.droit")

            if arbre.gauche.droit.droit == None:
                liste.append("gauche.droit.droit")

            else:
                if arbre.gauche.droit.droit.gauche == None:
                    liste.append("gauche.droit.droit.gauche")

                if arbre.gauche.droit.droit.droit == None:
                    liste.append("gauche.droit.droit.droit")
    #endregion

    #region sous-arbre droit
    if arbre.droit == None:
        liste.append("droit")

    else:
        if arbre.droit.gauche == None:
            liste.append("droit.gauche")

        else:
            if arbre.droit.gauche.gauche == None:
                liste.append("droit.gauche.gauche")

            else:
                if arbre.droit.gauche.gauche.gauche == None:
                    liste.append("droit.gauche.gauche.gauche")

                if arbre.droit.gauche.gauche.droit == None:
                    liste.append("droit.gauche.gauche.droit")

            if arbre.droit.gauche.droit == None:
                liste.append("droit.gauche.droit")

            else:
                if arbre.droit.gauche.droit.gauche == None:
                    liste.append("droit.gauche.droit.gauche")

                if arbre.droit.gauche.droit.droit == None:
                    liste.append("droit.gauche.droit.droit")

        if arbre.droit.droit == None:
            liste.append("droit.droit")

        else:
            if arbre.droit.droit.gauche == None:
                liste.append("droit.droit.gauche")

            else:
                if arbre.droit.droit.gauche.gauche == None:
                    liste.append("droit.droit.gauche.gauche")

                if arbre.droit.droit.gauche.droit == None:
                    liste.append("droit.droit.gauche.droit")

            if arbre.droit.droit.droit == None:
                liste.append("droit.droit.droit")

            else:
                if arbre.droit.droit.droit.gauche == None:
                    liste.append("droit.droit.droit.gauch")

                if arbre.droit.droit.droit.droit == None:
                    liste.append("droit.droit.droit.droit")
    #endregion

    return liste
#endregion

#region Arbre de test
arbre_test = structures.Arbrebinaire("toto")

arbre_test.ajoutgauche("tata")
arbre_test.gauche.ajoutgauche("titi")
arbre_test.gauche.ajoutdroit("tortor")
arbre_test.gauche.gauche.ajoutdroit("tojtoj")
arbre_test.gauche.gauche.ajoutgauche("teitei")
arbre_test.gauche.droit.ajoutgauche("tyty")
arbre_test.gauche.droit.ajoutdroit("trotro")
arbre_test.gauche.gauche.gauche.ajoutgauche("tritri")
arbre_test.gauche.gauche.gauche.ajoutdroit("totop")
arbre_test.gauche.gauche.droit.ajoutgauche("terter")
arbre_test.gauche.gauche.droit.ajoutdroit("tetez")
arbre_test.gauche.droit.gauche.ajoutgauche("tihtih")
arbre_test.gauche.droit.gauche.ajoutdroit("toutou")
arbre_test.gauche.droit.droit.ajoutgauche("turtur")
arbre_test.gauche.droit.droit.ajoutdroit("topto")

arbre_test.ajoutdroit("tantan")
arbre_test.droit.ajoutgauche("tintin")
arbre_test.droit.ajoutdroit("tutu")
arbre_test.droit.gauche.ajoutgauche("tiftif")
arbre_test.droit.gauche.ajoutdroit("touftouf")
arbre_test.droit.droit.ajoutgauche("tortor")
arbre_test.droit.droit.ajoutdroit("tirtir")
arbre_test.droit.gauche.gauche.ajoutgauche("tamtam")
arbre_test.droit.gauche.gauche.ajoutdroit("toumtoum")
arbre_test.droit.gauche.droit.ajoutgauche("totol")
arbre_test.droit.gauche.droit.ajoutdroit("tytyl")
arbre_test.droit.droit.gauche.ajoutgauche("a")
arbre_test.droit.droit.gauche.ajoutdroit("b")
arbre_test.droit.droit.droit.ajoutgauche("c")
arbre_test.droit.droit.droit.ajoutdroit("d")
#endregion

print("Bienvenue sur l'afficheur d'arbre binaire de Sergio BIOLAY-SEGURA et Nicolas TORO !\n")
activé = True
while activé == True:
    print("Que voulez-vous faire ?")
    print("1 - Créer un arbre")
    print("2 - Modifier un arbre")
    print("3 - Afficher un arbre")
    print("4 - Paramètres couleur")
    print("5 - Sortir")
    choix = input()
    print()

    if choix == "1":
        nom_arbre = input("Veuillez indiquer le nom de votre arbre : ")
        racine = input("Quelle est la racine de votre arbre ? ")
        globals()[nom_arbre] = structures.Arbrebinaire(racine)
        print("Votre arbre nommé " + nom_arbre + " avec comme racine " + racine + " a été créé !")
        print("Vous pouvez lui attribuer un sous-arbre gauche et un sous-arbre droit grâce à l'option \"Ajouter un noeud\" dans \"Modifier un arbre\".")

    elif choix == "2":
        arbre = input("Merci d'indiquer l'arbre à modifier : ")
        try:
            if type(globals()[arbre]) == structures.Arbrebinaire:
                continuer = True

        #region Si problème
        except:
            print(arbre + " n'est pas un arbre binaire ou le programme n'a pas réussi à charger l'arbre !")
        #endregion

        if continuer == True:
            print("Que voulez-vous modifier ?")
            print("1 - Ajouter un noeud")
            print("2 - Supprimer un noeud")
            choix_2 = input()

            if choix_2 == "1":
                print()
                print("Voici les noeuds ajoutable dans l'arbre dans l'ordre préfixe :")
                liste_enfant_possible = enfant_possible(globals()[arbre])
                for i in range(len(liste_enfant_possible)):
                    print(str(i + 1) + " - " + str(liste_enfant_possible[i]))
                numéro_du_noeud_choisis = int(input("Numéro du noeuds à ajouter : "))
                nom_du_noeud = input("Comment s'appelle votre noeud ? ")
                exec(arbre + "." + liste_enfant_possible[numéro_du_noeud_choisis - 1] + " = structures.Arbrebinaire(nom_du_noeud)")
                print("Le noeud " + nom_du_noeud + " a été ajouté à la place : " + liste_enfant_possible[numéro_du_noeud_choisis - 1])

            elif choix_2 == "2":
                print()
                print("Voici les noeuds de l'abre dans l'ordre préfixe :")
                liste_des_valeurs = []
                liste_prefixe(liste_des_valeurs, globals()[arbre])
                for i in range(len(liste_des_valeurs)):
                    print(str(i) + " - " + liste_des_valeurs[i])
                try:
                    numéro_de_la_valeur_choisis = int(input("Numéro du noeuds à supprimer : "))
                    if numéro_de_la_valeur_choisis >= 0 and numéro_de_la_valeur_choisis < structures.taille(globals()[arbre]):
                        print(supprime_noeud(globals()[arbre], numéro_de_la_valeur_choisis) + " a été supprimé !")
                    else:
                        print("Choix inconnu !")
                except:
                    print("Choix inconnu !")

            else:
                print("Choix inconnu !")



    elif choix == "3":
        #region Création de l'image
        img=Image.new("RGB",(800, 900))

        imgdessin=ImageDraw.Draw(img)

        for x in range(800):
            for y in range(900):
                img.putpixel((x,y),(r_fond, v_fond, b_fond))

        nom_de_la_police = "arial.ttf"
        #endregion

        #region Désinage de l'image
        arbre = input("Merci d'indiquer l'arbre à afficher : ")
        try:
            creation_arbre(globals()[arbre])
            options_suppplementaire(globals()[arbre])
            imgdessin.text((500, 875), "Copyright © by Sergio BIOLAY-SEGURA and Nicolas TORO", fill=(0,0,0), font=ImageFont.truetype(nom_de_la_police, size=10))
            img.show()
        #endregion

        #region Enregistrer l'image
            print("Voulez-vous enregister l'image ?")
            print("1 - Oui | 2 - Non")
            choix_enregistrer = input()
            if choix_enregistrer == "1":
                nom_du_fichier = input("Merci d'indiquer le nom du fichier : ")
                img.save(nom_du_fichier + ".png")
                print("Image sauvegardé !")
        #endregion

        #region Si problème
        except:
            print(arbre + " n'est pas un arbre binaire ou le programme n'a pas réussi à afficher l'arbre !")
        #endregion

    elif choix == "4":
        print("Quelle paramètres veux-tu changer ?")
        print("1 - Changer la couleur du fond")
        print("2 - Changer la couleur des lignes de gauche")
        print("3 - Changer la couleur des lignes de droite")
        choix_paramètre = input()

        if choix_paramètre == "1":
            print("Quelle couleur veux-tu ? (Blanc par défaut)")
            print("1 - Bleu")
            print("2 - Jaune")
            print("3 - Rouge")
            print("4 - Vert")
            print("5 - Violet")
            print("6 - Marron")
            print("7 - Orange")
            print("8 - Blanc")
            couleur_fond = input()

            if couleur_fond == "1":
                r_fond = 0
                v_fond = 255
                b_fond = 255
                print("Le fond de l'image est maintenant bleu !")
            elif couleur_fond == "2":
                r_fond = 255
                v_fond = 255
                b_fond = 127
                print("Le fond de l'image est maintenant jaune !")
            elif couleur_fond == "3":
                r_fond = 255
                v_fond = 63
                b_fond = 0
                print("Le fond de l'image est maintenant rouge !")
            elif couleur_fond == "4":
                r_fond = 0
                v_fond = 255
                b_fond = 127
                print("Le fond de l'image est maintenant vert !")
            elif couleur_fond == "5":
                r_fond = 127
                v_fond = 0
                b_fond = 255
                print("Le fond de l'image est maintenant violet !")
            elif couleur_fond == "6":
                r_fond = 163
                v_fond = 90
                b_fond = 63
                print("Le fond de l'image est maintenant marron !")
            elif couleur_fond == "7":
                r_fond = 255
                v_fond = 127
                b_fond = 0
                print("Le fond de l'image est maintenant orange !")
            elif couleur_fond == "8":
                r_fond = 255
                v_fond = 255
                b_fond = 255
                print("Le fond de l'image est maintenant blanc !")
            else:
                print("Choix inconnu !")

        elif choix_paramètre == "2":
            print("Quelle couleur veux-tu ? (Rouge par défaut)")
            print("1 - Bleu")
            print("2 - Jaune")
            print("3 - Rouge")
            print("4 - Vert")
            print("5 - Violet")
            print("6 - Marron")
            print("7 - Orange")
            print("8 - Noir")
            couleur_Lgauche = input()

            if couleur_Lgauche == "1":
                r_ligne_gauche = 0
                v_ligne_gauche = 0
                b_ligne_gauche = 255
                print("Les lignes de gauches sont maintenant bleu !")
            elif couleur_Lgauche == "2":
                r_ligne_gauche = 255
                v_ligne_gauche = 255
                b_ligne_gauche = 0
                print("Les lignes de gauches sont maintenant jaune !")
            elif couleur_Lgauche == "3":
                r_ligne_gauche = 255
                v_ligne_gauche = 0
                b_ligne_gauche = 0
                print("Les lignes de gauches sont maintenant rouge !")
            elif couleur_Lgauche == "4":
                r_ligne_gauche = 0
                v_ligne_gauche = 255
                b_ligne_gauche = 0
                print("Les lignes de gauches sont maintenant vert !")
            elif couleur_Lgauche == "5":
                r_ligne_gauche = 200
                v_ligne_gauche = 0
                b_ligne_gauche = 255
                print("Les lignes de gauches sont maintenant violet !")
            elif couleur_Lgauche == "6":
                r_ligne_gauche = 255
                v_ligne_gauche = 127
                b_ligne_gauche = 63
                print("Les lignes de gauches sont maintenant marron !")
            elif couleur_Lgauche == "7":
                r_ligne_gauche = 127
                v_ligne_gauche = 127
                b_ligne_gauche = 0
                print("Les lignes de gauches sont maintenant orange !")
            elif couleur_Lgauche == "8":
                r_ligne_gauche = 0
                v_ligne_gauche = 0
                b_ligne_gauche = 0
                print("Les lignes de gauches sont maintenant noir !")
            else:
                print("Choix inconnu !")

        elif choix_paramètre == "3":
            print("Quelle couleur veux-tu ? (Bleu par défaut)")
            print("1 - Bleu")
            print("2 - Jaune")
            print("3 - Rouge")
            print("4 - Vert")
            print("5 - Violet")
            print("6 - Marron")
            print("7 - Orange")
            print("8 - Noir")
            couleur_Ldroite = input()

            if couleur_Ldroite == "1":
                r_ligne_droite = 0
                v_ligne_droite = 0
                b_ligne_droite = 255
                print("Les lignes de droites sont maintenant bleu !")
            elif couleur_Ldroite == "2":
                r_ligne_droite = 255
                v_ligne_droite = 255
                b_ligne_droite = 0
                print("Les lignes de droites sont maintenant jaune !")
            elif couleur_Ldroite == "3":
                r_ligne_droite = 255
                v_ligne_droite = 0
                b_ligne_droite = 0
                print("Les lignes de droites sont maintenant rouge !")
            elif couleur_Ldroite == "4":
                r_ligne_droite = 0
                v_ligne_droite = 255
                b_ligne_droite = 0
                print("Les lignes de droites sont maintenant vert !")
            elif couleur_Ldroite == "5":
                r_ligne_droite = 255
                v_ligne_droite = 0
                b_ligne_droite = 255
                print("Les lignes de droites sont maintenant violet !")
            elif couleur_Ldroite == "6":
                r_ligne_droite = 255
                v_ligne_droite = 127
                b_ligne_droite = 63
                print("Les lignes de droites sont maintenant marron !")
            elif couleur_Ldroite == "7":
                r_ligne_droite = 127
                v_ligne_droite = 127
                b_ligne_droite = 0
                print("Les lignes de droites sont maintenant orange !")
            elif couleur_Ldroite == "8":
                r_ligne_droite = 0
                v_ligne_droite = 0
                b_ligne_droite = 0
                print("Les lignes de droites sont maintenant noir !")
            else:
                print("Choix inconnu !")

        else:
            print("Choix inconnu !")

    elif choix == "5":
        exit()

    else:
        print("Choix inconnu !")

    print()
# Merci d'avoir pris le temps de lire tout mon programme :)