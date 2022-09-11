#region Plan
'''Comment jouer :
- Divisez les 54 cartes en deux (Jokers inclut)
- Retournez une carte de chaque paquets
- Celui qui as la plus forte remporte la carte de l'autre et met les carte dans son paquets de "cartes gagner"
(Si c'est la même carte il y a une bataille, on retourne une carte face caché et encore une autre et ainsi de suite)
- On continue jusqu'à ce que plus personne ait de cartes
- Quand plus personne n'a de carte on demande si ils veulent continuer et si il veulent on continue avec le paquets de "cartes gagner"
- C'est celui qui as le plus de cartes qui as gagner
'''

'''A faire :
[ ] Faire un dictionnaire paquets avec keys (carreaux, tréfles, coeurs, piques et jokers) et values (2,3,4,5,6,7,8,9,10,Valets,Dame,Rois et As)
[ ] Faire la distibution
    [ ] Faire une boucle qui s'arrête quand carte distribuer est à 54
    [ ] Faire une sous boucle qui s'arrête à la moitier du paquets (27)
    [ ] Un nombre random qui prend une keys (entre 1 et 5) en les listant
    [ ] Un nombre random qui prend une values (entre 1 et 3)
    [ ] Check si la valeur ne vaut pas " "
    [ ] Sinon :
        [ ] Ajouter 1 à carte distribuer
        [ ] On ajoute juste la valeur de la carte ou un tableau de la valeur et du type de la carte dans le tableau joueur1 et joueur2
        [ ] On remplace la valeur par " "
[ ] Faire une boucle jusqu'à ce que les tableaux soit vides
    [ ] Chaque paquets met sa première carte 
    [ ] Si s'est la même alors faire une boucle qui s'arrête quznd c'est bon et mettre une carte sans comparer et dire les noms puis mettre une autre et recomparer et si s'est pas bon la boucle recommence
    [ ] Sinon ajouter la carte à paquets_gagnant_joueur puis supprimer la carte du paquet du joueur
[ ] Quand s'est finis demander de recommencer et si oui demande si à partir du paquets obtenue (+ verif si y'a pas zéro carte dans un paquets) sinon recommencer du début et sinon exit
Bonus :
[ ] Faire un design avec PyQT
[ ] Faire un menu 
    [ ] Faire une partie paramètres
    [ ] Faire une partie crédits/règles du jeu
[ ] Faire un speedmode
[ ] Faire des plus grosses parties (9,6,3,etc) 
'''
#endregion

#region Module
import sys
import os
import colorama #Couleur: https://pypi.org/project/colorama/
from pathlib import Path
from configparser import ConfigParser
import random
#endregion

#region Variables
text_color = {
    "Noir": "\u001b[30m",
    "Rouge": "\u001b[31m",
    "Vert": "\u001b[32m",
    "Jaune": "\u001b[33m",
    "Bleu": "\u001b[34m",
    "Magenta": "\u001b[35m",
    "Cyan": "\u001b[36m",
    "Blanc": "\u001b[37m",
    "Normal": "\u001b[0m"
}

background_color = {
    "Noir": "\u001b[40m",
    "Rouge": "\u001b[41m",
    "Vert": "\u001b[42m",
    "Jaune": "\u001b[43m",
    "Bleu": "\u001b[44m",
    "Magenta": "\u001b[45m",
    "Cyan": "\u001b[46m",
    "Blanc": "\u001b[47m",
    "Normal": "\u001b[0m"
}

settings = {
    "joueurs" : 2,
    "paquet" : "paquet_simple",
    "jokers" : True,
    "text_color" : "Normal",
    "background_color" : "Normal",
    "text_speed" : 30
}

#region Paquets
paquet_joueur = {}

paquet_simple = {
    "carreaux" : ["2", "3" , "4", "5", "6", "7", "8" ,"9" , "10", "valet", "dame" , "roi", "as"],
    "cœurs" : ["2", "3" , "4", "5", "6", "7", "8" ,"9" , "10", "valet", "dame" , "roi", "as"],
    "piques" : ["2", "3" , "4", "5", "6", "7", "8" ,"9" , "10", "valet", "dame" , "roi", "as"],
    "trèfles" : ["2", "3" , "4", "5", "6", "7", "8" ,"9" , "10", "valet", "dame" , "roi", "as"],
    "jokers" : ["jokers1", "jokers2"]
}

paquet_rapide = {
    "carreaux" : ["7", "8" ,"9" , "10", "valet", "dame" , "roi", "as"],
    "cœurs" : ["7", "8" ,"9" , "10", "valet", "dame" , "roi", "as"],
    "piques" : ["7", "8" ,"9" , "10", "valet", "dame" , "roi", "as"],
    "trèfles" : ["7", "8" ,"9" , "10", "valet", "dame" , "roi", "as"],
    "jokers" : ["jokers1", "jokers2"]
}

paquet_custom = {#Mettre les cartes dans l'ordre croissant
    "carreaux" : ["2", "3" , "4", "5", "6", "7", "8" ,"9" , "10", "valet", "dame" , "roi", "as"],
    "cœurs" : ["2", "3" , "4", "5", "6", "7", "8" ,"9" , "10", "valet", "dame" , "roi", "as"],
    "piques" : ["2", "3" , "4", "5", "6", "7", "8" ,"9" , "10", "valet", "dame" , "roi", "as"],
    "trèfles" : ["2", "3" , "4", "5", "6", "7", "8" ,"9" , "10", "valet", "dame" , "roi", "as"],
    "jokers" : ["jokers1", "jokers2"]
}
#endregion
#endregion

def keys(dico):
    return list(dico.keys())

def text_initialisation():
    print(text_color[settings["text_color"]] + background_color[settings["background_color"]])

def creation():
    nouvelle_partie = open("./Bataille/partie.ini", "w")
    nouvelle_partie.close()

    print(text_color["Bleu"] + "===============================================================")
    print("|  _             ____        _        _ _ _                   |")
    print("| | |           |  _ \      | |      (_) | |                  |")
    print("| | |     __ _  | |_) | __ _| |_ __ _ _| | | ___              |")
    print("| | |    / _` | |  _ < / _` | __/ _` | | | |/ _ \             |")
    print("| | |___| (_| | | |_) | (_| | || (_| | | | |  __/             |")
    print("| |______\__,_| |____/ \__,_|\__\__,_|_|_|_|\___| by nt games |")
    print("|                                                             |")
    print("===============================================================\n" + text_color[settings["text_color"]])

    choix_effectuer = False
    while choix_effectuer == False:
        print("Que voulez-vous faire ?")
        print("1 - Créer une partie")
        print("2 - Paramètres")
        print("3 - Crédits")
        choix = int(input("Choix : "))
        print()

        #region Création de partie
        if choix == 1:
            choix_effectuer = True
            distribution(settings["paquet"])
        #endregion

        #region Paramètres
        elif choix == 2:
            #choix_effectuer = True

            #region Joueurs
            #Trop de problèmes en fonction du paquet de cartes, à régler plus tard
            #print("Nombre de joueurs : (" + settings["joueurs"] + " par defaut)")
            #settings["joueurs"] = int(input())
            #endregion

            #region Paquet
            settings_paquet = False
            while settings_paquet == False:
                print("Type de paquet : (" + settings["paquet"] + " par defaut)")
                choix_paquet = input("[Choix entre \"paquet_simple\"(52 cartes) ou \"paquet_rapide\"(32 cartes) ou \"paquet_customisé\"] ")

                if choix_paquet == "paquet_simple" or choix_paquet == "paquet_rapide" or choix_paquet == "paquet_customisé":
                    settings["paquet"] = choix_paquet
                    settings_paquet = True

                else:
                    print("Paquet inconnu !")
            #endregion

            #region Jokers
            settings_jokers = False
            while settings_jokers == False:
                print("Activation des jokers : (" + str(settings["jokers"]) + " par defaut)")
                choix_jokers = input("[\"True\" (activé) ou \"False\" (désactivé)] ")

                if choix_jokers == "True" or choix_jokers == "False":
                    settings["jokers"] = bool(choix_jokers)
                    settings_jokers = True

                else:
                    print("Choix inconnu !")
            #endregion

            #region Couleur des textes
            settings_text_color = False
            while settings_text_color == False:
                print("Couleur des textes : (" + str(settings["text_color"]) + " par defaut)")
                choix_text_color = input(text_color["Normal"] + "[\"" + text_color["Noir"] + "Noir" + text_color["Normal"] + "\" ou \"" + text_color["Rouge"] + "Rouge" + text_color["Normal"] + "\" ou \"" + text_color["Jaune"] + "Jaune" + text_color["Normal"] + "\" ou \"" + text_color["Vert"] + "Vert" + text_color["Normal"] + "\" ou \"" + text_color["Cyan"] + "Cyan" + text_color["Normal"] + "\" ou \"" + text_color["Bleu"] + "Bleu" + text_color["Normal"] + "\" ou \"" + text_color["Magenta"] + "Magenta" + text_color["Normal"] + "\" ou \"" + text_color["Blanc"] + "Blanc" + text_color["Normal"] + "\" ou \"Normal\"] ")

                if choix_text_color == "Noir" or choix_text_color == "Rouge" or choix_text_color == "Jaune" or choix_text_color == "Vert"  or choix_text_color == "Cyan" or choix_text_color == "Bleu"  or choix_text_color == "Magenta"  or choix_text_color == "Blanc" or choix_text_color == "Normal":
                    settings["text_color"] = choix_text_color
                    settings_text_color = True

                else:
                    print("Choix inconnu !")
            #endregion

            #region Couleur de fond des textes
            settings_background_color = False
            while settings_background_color == False:
                print("Couleur de fond des textes : (" + str(settings["background_color"]) + " par defaut)")
                choix_background_color = input("[\"" + background_color["Noir"] + "Noir" + background_color["Normal"] + "\" ou \"" + background_color["Rouge"] + "Rouge" + background_color["Normal"] + "\" ou \"" + background_color["Jaune"] + "Jaune" + background_color["Normal"] + "\" ou \"" + background_color["Vert"] + "Vert" + background_color["Normal"] + "\" ou \"" + background_color["Cyan"] + "Cyan" + background_color["Normal"] + "\" ou \"" + background_color["Bleu"] + "Bleu" + background_color["Normal"] + "\" ou \"" + background_color["Magenta"] + "Magenta" + background_color["Normal"] + "\" ou \"" + background_color["Blanc"] + "Blanc" + background_color["Normal"] + "\" ou \"Normal\"] ")

                if choix_background_color == "Noir" or choix_background_color == "Rouge" or choix_background_color == "Jaune" or choix_background_color == "Vert"  or choix_background_color == "Cyan" or choix_background_color == "Bleu"  or choix_background_color == "Magenta"  or choix_background_color == "Blanc" or choix_background_color == "Normal":
                    settings["background_color"] = choix_background_color
                    settings_background_color = True

                else:
                    print("Choix inconnu !")
            #endregion

            #region Vitesse du texte
            settings_text_speed = False
            while settings_text_speed == False:
                print("Vitesse du texte : (" + str(settings["text_speed"]) + " par defaut)")
                choix_text_speed = int(input("[Choix entre 1 et 300] "))

                if type(choix_text_speed) == int:
                    settings["text_speed"] = choix_text_speed
                    settings_text_speed = True

                else:
                    print("Choix inconnu !")
            #endregion

            #region Save
            #region Old
            #parametre = open("./Bataille/settings.ini", "w")
            #parametre.close()
            #endregion

            parametre = ConfigParser()
            parametre.add_section("SETTINGS")
            for keys, values in settings.items():
                parametre.set("SETTINGS", keys, str(values))
            with open("./Bataille/settings.ini", "w") as fichier:
                parametre.write(fichier)
            
            print("Paramètres sauvegarder !")
            #endregion

            #region Initialisation
            text_initialisation()
            #endregion
        #endregion

        #region Crédits
        elif choix == 3:
            #choix_effectuer = True
            print("Merci à vous de jouer et soutenir notre jeu ! [Made by nt games]")
            print(background_color["Normal"] + text_color["Rouge"] + "Youtube : https://www.youtube.com/c/nt-games-ytb")
            print(background_color["Normal"] + text_color["Noir"] + "Code source [github] : https://github.com/nt-games-ytb/NSI/blob/main/NSI%201er/Mathieu/Jeu/Bataille/Bataille.py")
            text_initialisation()
        #endregion

        else:
            print("Commande inconnu !\n")

def reprendre():
    #region Partie existante
    if os.path.exists("./Bataille/partie.ini"): #"./Bataille" parce que j'execute dans le directory "Jeu"
        lancement = False
        while lancement == False:
            charger = input(text_color["Rouge"] + "Une partie existe déjà, voulez-vous la charger ? (Oui/Non) ")
            print()
            
            #region Création de nouvelle partie
            if charger == "Non" or charger == "non" or charger == "NON" or charger == "N" or charger == "n":
                lancement = True
                os.remove("./Bataille/partie.ini")
                creation()
            #endregion

            #region Chargement de l'ancienne partie
            elif charger == "Oui" or charger == "oui" or charger == "OUI" or charger == "O" or charger == "o" or charger == "Y" or charger == "y":
                lancement = True
                #reprendre

                ancienne_partie = open("./Bataille/partie.ini")
                #Load la partie
                if os.path.exists("./Bataille/settings.ini"):
                    parametre = ConfigParser()
                    parametre.read("./Bataille/settings.ini")
                    nombre_de_settings = len(parametre.items("SETTINGS"))
                    for i in range(nombre_de_settings):
                        settings[parametre.items("SETTINGS")[i][0]] = parametre.items("SETTINGS")[i][1]
                    #print(settings)
                    #Load les paramètres
            #endregion
            
            else:
                print("Réponse inconnu !\n")
    #endregion

    else:
        creation()

def distribution(paquet_utilisé):
    #region Nombre de cartes
    nombre_de_cartes_par_paquet = 0
    if settings["paquet"] == "paquet_simple":
        nombre_de_cartes_par_paquet = 52
    elif settings["paquet"] == "paquet_rapide":
        nombre_de_cartes_par_paquet = 32
    else:
        #faire le calcul du paquet
        pass

    if settings["jokers"] == True:
        nombre_de_cartes_par_paquet += 2

    nombre_de_cartes_par_joueurs = nombre_de_cartes_par_paquet / settings["joueurs"]
    nombre_de_cartes_par_joueurs = int(nombre_de_cartes_par_joueurs)
    #endregion

    #region Dstibution des cartes
    for joueur in range(settings["joueurs"]):
        paquet_joueur["joueur " + str(joueur + 1)] = [] #Création du paquet du joueur

        carte = 0
        while carte != nombre_de_cartes_par_joueurs:
            nombre_random_de_la_famille_de_carte = random.randint(0, len(keys(globals()[settings["paquet"]])) - 1) #Choix d'une famille random selon le paquet choisis
            famille_de_la_carte = keys(globals()[settings["paquet"]])[nombre_random_de_la_famille_de_carte] #Conversion de la position en nom de la famille de la carte dans le paquet du joueur

            nombre_random_du_chiffre_de_la_carte = random.randint(0, len(globals()[settings["paquet"]][famille_de_la_carte]) - 1) #Choix d'une carte random selon le paquet et la famille choisis
            chiffre_de_la_carte = globals()[settings["paquet"]][famille_de_la_carte][nombre_random_du_chiffre_de_la_carte] #Conversion de la position en nom du chiffre de la carte dans le paquet du joueur

            if globals()[settings["paquet"]][famille_de_la_carte][nombre_random_du_chiffre_de_la_carte] != "": #Vérifie si la carte est toujours dans le paquet de carte #Si oui :
                paquet_joueur["joueur " + str(joueur + 1)].append((famille_de_la_carte, chiffre_de_la_carte)) #Ajoute dans la carte dans le paquet du joueur
                globals()[settings["paquet"]][famille_de_la_carte][nombre_random_du_chiffre_de_la_carte] = "" #Supprime la carte du paquet de carte
                carte += 1
    #endregion
    
    #print(paquet_joueur)
    partie()

def partie():
    pass

#region Execution
reprendre()
#endregion