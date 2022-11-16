#region Import
import os
from colorama import Fore, Style
from urllib.request import urlopen
import time
import ast
import xml.dom.minidom

import random
try:
    from playsound import playsound
except:
    print(f"{Fore.RED}Nous avons remarqué que vous n'avez pas le module \"Playsound\" !\nNous allons donc vous l'installer :")
    os.system("pip install playsound")
    from playsound import playsound
    print(f"{Style.RESET_ALL}")
#endregion

#region Initialisation
class Initialisation:
    def __init__(self, dossier):
        self.dossier = dossier

    def fichier_existe(self, fichier):
        if os.path.exists(self.dossier + "\\" + fichier) == True:
            return True
        else:
            return False

    def convertir_en_liste(self, textes):
        return ast.literal_eval(textes)

    def creation_de_la_sauvegarde(self):
        afficher([
        "Bonjour et bienvenue dans le jeu !",
        "Je vois que tu es nouveau, je me suis permis de fouiller dans ton PC et je n'ai pas trouvé de sauvegarde du jeu.",
        "Enfin bref, moi c'est M.Mathieu ancien prof d'NSI au lycée Thierry Maulnier et actuel professeur de NSI dans le Nord et fier d'y être parce que j'en pouvais plus de ces fous de 1G03."], 0.05, "normal")
        fichier = open(self.dossier + "\sauvegarde.xml", "a")
        fichier.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<sauvegarde>\n</sauvegarde>")
        fichier.close()

    def creation_de_joueur(self, joueur):
        Texte_de_Mathieu()
        afficher(["Parle moi un peu de toi que je te crée un personnage pour que tu joues :"], 0.05, "normal")
        joueur.nom = input("Comment t'appelles-tu ? ")
        self.sauvegarder(joueur)

    def afficher_les_joueurs(self, fichier):
        print("Un fichier de sauvegarde a été trouvé !")
        print("Plusieurs options s'offrent donc à toi, elle sont les suivantes :")
        print("0 - Créer un nouveau joueur")
        fichier_xml_de_sauvegarde = xml.dom.minidom.parse(self.dossier + fichier)
        liste_des_joueurs = fichier_xml_de_sauvegarde.documentElement.getElementsByTagName("joueur")
        numéro_joueur = 1
        try:
            for nom in liste_des_joueurs:
                print(str(numéro_joueur) + " - Jouer avec " + nom.childNodes[0].nodeValue)
                numéro_joueur = numéro_joueur + 1
        except:
            print(f"{Fore.RED}Malheuresement, nous n'avons pas réussi à charger de joueurs.{Fore.RESET}")
        if numéro_joueur == 1:
            print(f"{Fore.RED}Malheuresement, nous n'avons pas réussi à charger de joueurs.{Fore.RESET}")

    def chargement_du_joueur(self, fichier, joueur, numéro_du_joueur):
        if numéro_du_joueur == 0:
            self.creation_de_joueur(joueur)
            saut_de_lignes()
        else:
            fichier_xml_de_sauvegarde = xml.dom.minidom.parse(self.dossier + fichier)
            liste_des_joueurs = fichier_xml_de_sauvegarde.documentElement.getElementsByTagName("joueur")
            joueur.nom = liste_des_joueurs[numéro_du_joueur - 1].childNodes[0].nodeValue
            joueur.vie = int(liste_des_joueurs[numéro_du_joueur - 1].getAttribute("vie"))
            joueur.vie_maximal = int(liste_des_joueurs[numéro_du_joueur - 1].getAttribute("vie_maximal"))
            joueur.argent = int(liste_des_joueurs[numéro_du_joueur - 1].getAttribute("argent"))
            joueur.argent_banque = int(liste_des_joueurs[numéro_du_joueur - 1].getAttribute("argent_banque"))
            joueur.expérience = int(liste_des_joueurs[numéro_du_joueur - 1].getAttribute("experience"))
            joueur.niveau = int(liste_des_joueurs[numéro_du_joueur - 1].getAttribute("niveau"))
            joueur.objet_en_main = int(liste_des_joueurs[numéro_du_joueur - 1].getAttribute("objet_en_main"))
            joueur.sac = self.convertir_en_liste(liste_des_joueurs[numéro_du_joueur - 1].getAttribute("sac"))
            joueur.langage_débloqué = int(liste_des_joueurs[numéro_du_joueur - 1].getAttribute("langage_debloque"))
            joueur.vitesse_du_texte = float(liste_des_joueurs[numéro_du_joueur - 1].getAttribute("vitesse_du_texte"))
            joueur.dossier_du_jeu = liste_des_joueurs[numéro_du_joueur - 1].getAttribute("dossier_du_jeu")
            joueur.fichier_de_sauvegarde = liste_des_joueurs[numéro_du_joueur - 1].getAttribute("fichier_de_sauvegarde")

    def sauvegarder(self, joueur):
        fichier_xml_de_sauvegarde = xml.dom.minidom.parse(joueur.dossier_du_jeu + joueur.fichier_de_sauvegarde)
        liste_des_joueurs = fichier_xml_de_sauvegarde.documentElement.getElementsByTagName("joueur")
        for nom in liste_des_joueurs:
            if nom.childNodes[0].nodeValue == joueur.nom:
                nom.setAttribute("vie", str(joueur.vie))
                nom.setAttribute("vie_maximal", str(joueur.vie_maximal))
                nom.setAttribute("argent", str(joueur.argent))
                nom.setAttribute("argent_banque", str(joueur.argent_banque))
                nom.setAttribute("experience", str(joueur.expérience))
                nom.setAttribute("niveau", str(joueur.niveau))
                nom.setAttribute("objet_en_main", str(joueur.objet_en_main))
                nom.setAttribute("sac", str(joueur.sac))
                nom.setAttribute("langage_debloque", str(joueur.langage_débloqué))
                nom.setAttribute("vitesse_du_texte", str(joueur.vitesse_du_texte))
                nom.setAttribute("dossier_du_jeu", joueur.dossier_du_jeu)
                nom.setAttribute("fichier_de_sauvegarde", joueur.fichier_de_sauvegarde)
                fichier_xml_de_sauvegarde.writexml(open(joueur.dossier_du_jeu  + joueur.fichier_de_sauvegarde, "w"))
                return None 
        nouveau_joueur = fichier_xml_de_sauvegarde.createElement("joueur")
        nouveau_joueur.appendChild(fichier_xml_de_sauvegarde.createTextNode(joueur.nom))
        nouveau_joueur.setAttribute("vie", str(joueur.vie))
        nouveau_joueur.setAttribute("vie_maximal", str(joueur.vie_maximal))
        nouveau_joueur.setAttribute("argent", str(joueur.argent))
        nouveau_joueur.setAttribute("argent_banque", str(joueur.argent_banque))
        nouveau_joueur.setAttribute("experience", str(joueur.expérience))
        nouveau_joueur.setAttribute("niveau", str(joueur.niveau))
        nouveau_joueur.setAttribute("objet_en_main", str(joueur.objet_en_main))
        nouveau_joueur.setAttribute("sac", str(joueur.sac))
        nouveau_joueur.setAttribute("langage_debloque", str(joueur.langage_débloqué))
        nouveau_joueur.setAttribute("vitesse_du_texte", str(joueur.vitesse_du_texte))
        nouveau_joueur.setAttribute("dossier_du_jeu", joueur.dossier_du_jeu)
        nouveau_joueur.setAttribute("fichier_de_sauvegarde", joueur.fichier_de_sauvegarde)
        fichier_xml_de_sauvegarde.documentElement.appendChild(nouveau_joueur)
        with open(joueur.dossier_du_jeu  + joueur.fichier_de_sauvegarde, "w") as fichier_xml:
            fichier_xml.write(fichier_xml_de_sauvegarde.toprettyxml())

#region Affichage
def afficher(textes, temps, couleur):
    assert type(textes) == list
    for phrase in range(len(textes)):
        for caractère in range(len(textes[phrase])):
            #region Couleur
            if couleur == "rouge":
                print(f"{Fore.RED}", end="")
            elif couleur == "jaune":
                print(f"{Fore.YELLOW}", end="")
            elif couleur == "vert":
                print(f"{Fore.GREEN}", end="")
            elif couleur == "cyan":
                print(f"{Fore.CYAN}", end="")
            elif couleur == "bleu":
                print(f"{Fore.BLUE}", end="")
            elif couleur == "magenta":
                print(f"{Fore.MAGENTA}", end="")
            elif couleur == "blanc":
                print(f"{Fore.WHITE}", end="")
            elif couleur == "normal":
                print(f"{Fore.RESET}", end="")
            else:
                print("Couleur inconnue !")
                pass
            #endregion

            print(textes[phrase][caractère], end="")
            #playsound(dossier + "\\afficher.mp3") #Désactiver car trop lent
            time.sleep(temps)
        if phrase != len(textes) - 1:
            print()
    print(f"{Style.RESET_ALL}") #Remettre le texte normal

def saut_de_lignes():
    print()

def Texte_de_Mathieu():
    print(f"{Fore.RED}M.Mathieu: {Style.RESET_ALL}", end="")
#endregion

#region Tutoriel
def scenario(joueur):
    #print("Voici le scènario...")
    Texte_de_Mathieu()
    afficher(["Donc tu es " + joueur.nom + ".",
    "Je suppose que tu te demandes pourquoi je suis là ?",
    "Et bien en fait, on m'a averti des problèmes et des difficultés avec la classe de Terminal NSI du lycée et comme M.Duranton et M.Maurice sont au bord du burn out, je suis venu à la rescousse.",
    "Tes professeurs m'ont donc averti de tout ce que vous avez fait toi et tes camarades de classe et c'est pas beau à voir...",
    "A force de faire n'importe quoi en cours, vous avez créé une faille dans 30 langages de programmation différents !",
    "Cette faille a créé pleins de bugs qu'il va falloir réparer.",
    "C'est pour cela que vous êtes ici, dans ce petit RPG créé par Nicolas TORO, pour combattre les différents bugs de chaque langage afin de les rendre ré-utilisable."], 0.05, "normal")

def demande_tutoriel():
    print("Veux-tu lancer le tutoriel ?\n1 - Oui | 2 - Non")
    réponse_tutoriel = input()
    if réponse_tutoriel == "1":
        print("D'accord, on lance le tutoriel !")
        saut_de_lignes()
        tutoriel()
    elif réponse_tutoriel == "2":
        print("D'accord, on passe le tutoriel !")
    else:
        print("Je vais prendre cette réponse pour un non, donc on passe le tutoriel !")

def tutoriel():
    print("Désolé, le tutoriel arrivera dans une prochaine mise à jour !")
#endregion
#endregion

#region Joueur
class Joueur:
    def __init__(self, nom, vie, vie_maximal, argent, argent_banque, expérience, niveau, objet_en_main, sac,  langage_débloqué, vitesse_du_texte, dossier_du_jeu, fichier_de_sauvegarde):
        self.nom = nom
        self.vie = vie
        self.vie_maximal = vie_maximal
        self.argent = argent
        self.argent_banque = argent_banque
        self.expérience = expérience
        self.niveau = niveau
        self.objet_en_main = objet_en_main
        self.sac = sac
        self.langage_débloqué = langage_débloqué
        self.vitesse_du_texte = vitesse_du_texte
        self.dossier_du_jeu = dossier_du_jeu
        self.fichier_de_sauvegarde = fichier_de_sauvegarde
        
    def afficher_les_caracteristiques(self):
        print("Voici tes caractèrisitques :")
        print("Nom: " + self.nom)
        print("PV: " + str(self.vie) + "/" + str(self.vie_maximal))
        print("Bitcoin: " + str(self.argent) + " | Bitcoin dans la banque: " + str(self.argent_banque))
        print("Niveau: " + str(self.niveau) + " | Expérience: " + str(self.expérience) + "/" + str(self.niveau * 150))
        print("Vous tenez en main l'objet: " + self.sac[self.objet_en_main][0])
        print("Votre sac contient: ")
        for objet in self.sac:
            print("- " + objet[0] + " | Dégats: " + str(objet[1]))
        print("Vous avez débloqué: " + str(self.langage_débloqué) + " langages/30 langages")#Le "s" à langages -> faire un if
        print("Vitesse du jeu: " + str(self.vitesse_du_texte))
        print("Dossier du jeu: " + self.dossier_du_jeu)
        print("Fichier de sauvegarde: " + self.dossier_du_jeu + self.fichier_de_sauvegarde)
        print()

    def regarde_experience(self):
        if self.expérience >= self.niveau * 150:
            self.__monte_de_niveau()
        else:
            print("Vous êtes à " + str(self.expérience) + " xp/" + str(self.niveau * 150) + " xp.")

    def __monte_de_niveau(self):
        self.expérience = self.expérience - self.niveau * 150
        self.niveau = self.niveau + 1
        self.vie_maximal = self.vie_maximal + 10
        self.vie = self.vie + 10
        print("Vous êtes désormais niveau " + str(self.niveau) + ", votre vie maximal passe à " + str(self.vie_maximal) + " PV.")
        self.regarde_experience()

    def parametre(self):
        print("PARAMETRES :")
        print("Voulez-vous changer la vitesse du texte ?")
        print("1 - Oui | 2 - Non")
        réponse_vitesse_du_texte = input()
        if réponse_vitesse_du_texte == "1":
            print("Quelle sera la nouvelle valeur (en secondes) ?\n(la valeur actuelle est de " + str(self.vitesse_du_texte) + "s)")
            self.vitesse_du_texte = float(input())
        saut_de_lignes()

    def changer_objet_en_main(self):
        print("Que voulez-vous prendre en main ?")
        numéro_objet = 1
        for objet in self.sac:
            print(str(numéro_objet) + " - " + objet[0] + " | Dégats: " + str(objet[1]))
            numéro_objet = numéro_objet + 1
        réponse_objet = int(input())
        if réponse_objet > len(self.sac):
            print(f"{Fore.RED}L'objet demandé est inconnu !{Style.RESET_ALL}")
        else:
            self.objet_en_main = réponse_objet - 1
            print("Vous tenez en main l'objet: " + self.sac[self.objet_en_main][0])
        saut_de_lignes()
#endregion

#region Village
items_du_shop = [
["def", 200, 2],
["return", 300, 3],
["pass", 400, 4],
["class", 500, 5],
["import", 600, 6],
["from", 700, 7],
["if", 800, 8],
["elif", 900, 9],
["else", 1000, 10],
["for", 1100, 11],
["while", 1200, 12],
["try", 1300, 13],
["exept", 1400, 14],
["finally", 1500, 15],
["catch", 1600, 16]]

class Village:
    def __init__(self, première_fois_village, première_fois_hopital, première_fois_banque, première_fois_shop, son):
        self.première_fois_village = première_fois_village
        self.première_fois_hopital = première_fois_hopital
        self.première_fois_banque = première_fois_banque
        self.première_fois_shop = première_fois_shop
        self.son = son

    def vérifié_le_dossier_son(self, dossier):
        if os.path.exists(dossier + "\\son") == True:
            self.son = True
        else:
            self.son = False
        
    def village(self, joueur, langage):
        if self.première_fois_village == True:
            Texte_de_Mathieu()
            afficher(["Je te présente le village, c'est ici que tu habites.",
            "On y trouve un hopîtal pour se soigner, une banque pour stocker ton argent et un shop pour acheter des armes.",
            "Tu peux aussi partir dans une zone pour aller battre les différents langages."], joueur.vitesse_du_texte, "normal")
            self.première_fois_village = False
        print("Que veux-tu faire ?")
        print("1 - Parler à M.Mathieu")
        print("2 - Aller à l'hopîtal")
        print("3 - Aller à la banque")
        print("4 - Aller au shop")
        print("5 - Aller combattre des bugs")
        print("6 - Afficher les caractèristiques")
        print("7 - Changer d'objet en main")
        print("8 - Paramètres")
        réponse_village = input()
        saut_de_lignes()
        if réponse_village == "1":
            langage.parler_a_mathieu(joueur)
        elif réponse_village == "2":
            self.__hopital(joueur)
        elif réponse_village == "3":
            self.__banque(joueur)
        elif réponse_village == "4":
            self.__shop(joueur)
        elif réponse_village == "5":
            langage.choix_de_langage(joueur)
        elif réponse_village == "6":
            joueur.afficher_les_caracteristiques()
        elif réponse_village == "7":
            joueur.changer_objet_en_main()
        elif réponse_village == "8":
            joueur.parametre()
        else:
            print("Choix inconnu !")
        
    def decouvert(self):
        lieux_pas_encore_découvert = []
        if self.première_fois_hopital == True:
            lieux_pas_encore_découvert.append("Hopital")
        if self.première_fois_banque == True:
            lieux_pas_encore_découvert.append("Banque")
        if self.première_fois_shop == True:
            lieux_pas_encore_découvert.append("Shop")
        if lieux_pas_encore_découvert != [] :
            print(lieux_pas_encore_découvert)
            print("Vous n'avez pas encore découvert : ", end="")
            for lieux in range(len(lieux_pas_encore_découvert)):
                print(lieux_pas_encore_découvert[lieux] + " ", end="")
        print()
        
    #region Hopital
    def __hopital(self, joueur):
        if self.première_fois_hopital == True:
            print(f"{Fore.MAGENTA}Infirmière Joelle:{Style.RESET_ALL} ", end="")
            afficher(["Bienvenue à l'hopital, je suis l'infirmière Joelle et je suis là pour vous soigner !"], joueur.vitesse_du_texte, "normal")
            self.première_fois_hopital = False
        else:
            print(f"{Fore.MAGENTA}Infirmière Joelle:{Style.RESET_ALL} ", end="")
            afficher(["Bonjour !"], joueur.vitesse_du_texte, "normal")
        afficher(["Voulez-vous être soigné ?"], joueur.vitesse_du_texte, "normal")
        print("1 - Oui | 2 - Non")
        réponse_hopital = input()
        if réponse_hopital == "1":
            self.soin(joueur, joueur.vie_maximal)
        elif réponse_hopital == "2":
            afficher(["D'accord, alors j'espère vous revoir bientôt !"], joueur.vitesse_du_texte, "normal")
        else:
            afficher(["Désolé mais je n'ai pas compris votre demande...", "Je vous laisse retourner au village, j'espère vous revoir bientôt !"], joueur.vitesse_du_texte, "normal")
        saut_de_lignes()
    
    def soin(self, joueur, point_de_vie):
        joueur.vie = joueur.vie + point_de_vie
        if joueur.vie > joueur.vie_maximal:
            joueur.vie = joueur.vie_maximal
        if self.son == True:
            try:
                playsound(joueur.dossier_du_jeu + "\\son\\soin.mp3")
            except:
                print(f"{Fore.RED}Pour une raison inconnu le son n'a pas pu être joué !{Style.RESET_ALL}")
        print("Vous avez êtez soigné de " + str(point_de_vie) + " PV, vous êtes maintenant à " + str(joueur.vie) + " PV.")
    #endregion
        
    #region Banque    
    def __banque(self, joueur):
        if self.première_fois_banque == True:
            print(f"{Fore.YELLOW}Banquier:{Style.RESET_ALL} ", end="")
            afficher(["Bienvenue à la banque, je suis votre banquier et c'est moi qui vais gérer votre argent !"], joueur.vitesse_du_texte, "normal")
            self.première_fois_banque = False
        else:
            print(f"{Fore.YELLOW}Banquier:{Style.RESET_ALL} ", end="")
            afficher(["Bonjour !"], joueur.vitesse_du_texte, "normal")
        afficher(["Que voulez-vous faire ?"], joueur.vitesse_du_texte, "normal")
        print("1 - Déposer de l'argent\n2 - Retirer de l'argent\n3 - Retourner au village")
        réponse_banque = input()
        if réponse_banque == "1":
            self.__deposer_argent(joueur, int(input("Combien d'argent voulez-vous déposer ? ")))
        elif réponse_banque == "2":
            self.__retirer_argent(joueur, int(input("Combien d'argent voulez-vous retirer ? ")))
        elif réponse_banque == "3":
            afficher(["D'accord, alors j'espère vous revoir bientôt !"], joueur.vitesse_du_texte, "normal")
        else:
            afficher(["Désolé mais je n'ai pas compris votre demande...", "Je vous laisse retourner au village, j'espère vous revoir bientôt !"], joueur.vitesse_du_texte, "normal")
        saut_de_lignes()
        
    def __deposer_argent(self, joueur, argent_à_déposer):
        if argent_à_déposer > joueur.argent:
            argent_à_déposer = joueur.argent
        joueur.argent_banque = joueur.argent_banque + argent_à_déposer
        joueur.argent = joueur.argent - argent_à_déposer
        if self.son == True:
            try:
                playsound(joueur.dossier_du_jeu + "\\son\\banque.mp3")
            except:
                print(f"{Fore.RED}Pour une raison inconnu le son n'a pas pu être joué !{Style.RESET_ALL}")
        print("Vous avez déposé " + str(argent_à_déposer) + " bitcoin dans votre banque, vous êtes maintenant à " + str(joueur.argent) + " bitcoin avec en plus de cela " + str(joueur.argent_banque) + " bitcoin dans votre banque.")
        
    def __retirer_argent(self, joueur, argent_à_retirer):
        if argent_à_retirer > joueur.argent_banque:
            argent_à_retirer = joueur.argent_banque
        joueur.argent = joueur.argent + argent_à_retirer
        joueur.argent_banque = joueur.argent_banque - argent_à_retirer
        if self.son == True:
            try:
                playsound(joueur.dossier_du_jeu + "\\son\\banque.mp3")
            except:
                print(f"{Fore.RED}Pour une raison inconnu le son n'a pas pu être joué !{Style.RESET_ALL}")
        print("Vous avez retiré " + str(argent_à_retirer) + " bitcoin dans votre banque, vous êtes maintenant à " + str(joueur.argent) + " bitcoin avec en plus de cela " + str(joueur.argent_banque) + " bitcoin dans votre banque.")
    #endregion
        
    #region Shop
    def __shop(self, joueur):
        if self.première_fois_shop == True:
            print(f"{Fore.BLACK}Vendeur:{Style.RESET_ALL} ", end="")
            afficher(["Bienvenue au shop, je suis le vendeur du village, si vous voulez acheter quelque chose c'est ici qu'il faut venir !"], joueur.vitesse_du_texte, "normal")
            self.première_fois_shop = False
        else:
            print(f"{Fore.BLACK}Vendeur:{Style.RESET_ALL} ", end="")
            afficher(["Bonjour !"], joueur.vitesse_du_texte, "normal")
        self.__afficher_le_shop(joueur, items_du_shop)
        afficher(["Que voulez-vous faire ?"], joueur.vitesse_du_texte, "normal")
        print("(Indiquer le numéro de l'item à acheter ou mettez 0 pour retourner au village)")
        réponse_shop = int(input())
        if réponse_shop == 0:
            afficher(["D'accord, alors j'espère vous revoir bientôt !"], joueur.vitesse_du_texte, "normal")
        else:
            if réponse_shop > len(items_du_shop):
                afficher(["Désolé mais je n'ai pas cet item...", "Je vous laisse retourner au village, j'espère vous revoir bientôt !"], joueur.vitesse_du_texte, "normal")
            else: 
                self.__acheter_au_shop(joueur, réponse_shop)
        saut_de_lignes()
        
    def __afficher_le_shop(self, joueur, liste_des_items_du_shop):
        afficher(["Voici ce que vous pouvez acheter :"], joueur.vitesse_du_texte, "normal")
        numéro_item = 1
        for items in liste_des_items_du_shop:
            print(str(numéro_item) + " - " + items[0])
            print("Prix: " + str(items[1]) + " bitcoins | Dégats: " + str(items[2]))
            numéro_item = numéro_item + 1
        
    def __acheter_au_shop(self, joueur, numéro_item_choisis):
        for element in joueur.sac:
            if element == items_du_shop[numéro_item_choisis - 1]:
                print(f"{Fore.RED}Vous avez déjà acheter cette objet !{Style.RESET_ALL}")
                pass
        if joueur.argent <= items_du_shop[numéro_item_choisis - 1][1]:
            print(f"{Fore.RED}Vous n'avez pas assez d'argent sur vous !{Style.RESET_ALL}")
        else:
            joueur.sac.append([items_du_shop[numéro_item_choisis - 1][0],items_du_shop[numéro_item_choisis - 1][2]])
            joueur.argent = joueur.argent - items_du_shop[numéro_item_choisis - 1][1]
            if self.son == True:
                try:
                    playsound(joueur.dossier_du_jeu + "\\son\\shop1.mp3")
                except:
                    print(f"{Fore.RED}Pour une raison inconnu le son n'a pas pu être joué !{Style.RESET_ALL}")
            print("Vous venez d'acheter : " + items_du_shop[numéro_item_choisis - 1][0] + " !")
            print("Voulez-vous le tenir en main ? 1 - Oui | 2 - Non") 
            réponse_main = input()
            if réponse_main == "1":
                joueur.objet_en_main = len(joueur.sac) - 1
                print("Vous tenez en main l'objet: " + joueur.sac[joueur.objet_en_main][0])
    #endregion
#endregion

#region Langages
liste_des_langages = [
"Q#",
"Swift",
"Julia",
"Kotlin",
"Rust",
"Go",
"F#",
"C#",
"Objective Caml",
"JavaScript",
"PHP",
"Java",
"Delphi",
"Lua",
"Ruby",
"Brainfuck",
"SQL-2",
"Visual Basic",
"Python",
"Perl",
"Caml",
"MATLAB",
"Objective-C",
"C++",
"SQL",
"C",
"Pascal",
"BASIC",
"COBOL",
"FORTRAN"]

description_de_langage = [
"Le Q# est sortie en 2017.",
"Le Swift est sortie en 2014.",
"Le Julia est sortie en 2012.",
"Le Kotlin est sortie en 2011.",
"Le Rust est sortie en 2010.",
"Le Go est sortie en 2009.",
"Le F# est sortie en 2002.",
"Le C# est sortie en 2000.",
"Le Objective Caml est sortie en 1996.",
"Le JavaScript est sortie en 1995.",
"Le PHP est sortie en 1995.",
"Le Java est sortie en 1995.",
"Le Delphi est sortie en 1995.",
"Le Lua est sortie en 1993.",
"Le Ruby est sortie en 1993.",
"Le Brainfuck est sortie en 1993",
"Le SQL-2 est sortie en 1992.",
"Le Virtual Basic est sortie en 1991.",
"Le Python est sortie en 1991.",
"Le Perl est sortie en 1987.",
"Le Caml est sortie en 1985.",
"Le MATLAB est sortie en 1984.",
"Le Objective-C est sortie en 1983.",
"Le C++ est sortie en 1983.",
"Le SQL est sortie en 1974.",
"Le C est sortie en 1972.",
"Le Pascal est sortie en 1971.",
"Le Basic est sortie en 1964.",
"Le Cobol est sortie en 1960.",
"Le FORTAN est sortie en 1954.",
]

class Langages:
    def __init__(self, première_fois_langage):
        self.première_fois_langage = première_fois_langage

    def parler_a_mathieu(self, joueur):
        Texte_de_Mathieu()
        afficher([
        "Tu as débloqué " + str(joueur.langage_débloqué) + " langages sur 30, c'est pas mal, bravo !",
        "Le dernier langage que tu as débloqué est le " + liste_des_langages[joueur.langage_débloqué - 1] + ".",
        description_de_langage[joueur.langage_débloqué - 1],
        "Bref, je me perds dans ce que je dis.",
        "En tout cas, continue comme ça, tu as bientôt finis de le réparer, je crois en toi.",
        "Reviens me voir quand tu veux !"],
        joueur.vitesse_du_texte, "normal")
        saut_de_lignes()

    def choix_de_langage(self, joueur):
        if self.première_fois_langage == True:
            Texte_de_Mathieu()
            afficher([
            "Te voila maintenant à l'intersection.",
            "C'est ici que tu vas choisir un langage à réparer en exertminant les bugs de ce langage.",
            "Tu peux réparer autant de fois que tu veux un langage mais il suffit de réparer seulement une fois un langage pour débloquer le suivant et ainsi de suite."],
            joueur.vitesse_du_texte, "normal")
            self.première_fois_langage = False
        else:
            Texte_de_Mathieu()
            afficher(["Bonjour !"], joueur.vitesse_du_texte, "normal")
        afficher(["Que veux-tu faire ?"], joueur.vitesse_du_texte, "normal")
        print("0 - Retourner au village")
        self.__afficher_les_langages(joueur, liste_des_langages)
        réponse_langage = int(input())
        if réponse_langage == 0:
            afficher(["D'accord, alors j'espère te revoir bientôt !"], joueur.vitesse_du_texte, "normal")
        else:
            self.__entrer_dans_une_zone(joueur, réponse_langage)
        saut_de_lignes()

    def __afficher_les_langages(self, joueur, liste_langages):
        for numéro_de_langages in range(joueur.langage_débloqué):
            print(str(numéro_de_langages + 1) + " - Réparer le " + liste_langages[numéro_de_langages])

    def __entrer_dans_une_zone(self, joueur, numéro_du_langage):
        if numéro_du_langage > 30:
            print(f"{Fore.RED}Le langage que vous avez demandé n'existe pas !{Style.RESET_ALL}")
            saut_de_lignes()
            self.choix_de_langage(joueur)
        else:
            if numéro_du_langage > joueur.langage_débloqué:
                print(f"{Fore.RED}Vous n'avez pas encore débloqué ce langage !{Style.RESET_ALL}")
                saut_de_lignes()
                self.choix_de_langage(joueur)
            else:
                zone_choisis = Zone(liste_des_langages[numéro_du_langage - 1], numéro_du_langage - 1, random.randint(5 * numéro_du_langage, 12 * numéro_du_langage), 15 * numéro_du_langage, 3 * numéro_du_langage, 6 * numéro_du_langage, 0)
                afficher([
                "Très bien, tu vas donc t'occuper du " + liste_des_langages[numéro_du_langage - 1] + ".",
                "Pour le réparer, il faudra que tu fixes " + str(zone_choisis.nombre_de_bugs) + " bugs.",
                "Bonne chance !"], joueur.vitesse_du_texte, "normal")
                saut_de_lignes()
                zone_choisis.demande_de_combat(joueur)

class Zone:
    def __init__(self, nom_de_zone, numéro_de_zone, nombre_de_bugs, vie_des_bugs, dégats_minimal_des_bugs, dégats_maximal_des_bugs, bugs_battu):
        self.nom_de_zone = nom_de_zone
        self.numéro_de_zone = numéro_de_zone
        self.nombre_de_bugs = nombre_de_bugs
        self.vie_des_bugs = vie_des_bugs
        self.dégats_minimal_des_bugs = dégats_minimal_des_bugs
        self.dégats_maximal_des_bugs = dégats_maximal_des_bugs
        self.bugs_battu = bugs_battu

    def demande_de_combat(self, joueur):
        print("Zone " + self.nom_de_zone + " (Bugs battu: " + str(self.bugs_battu) + "/" + str(self.nombre_de_bugs) + ")")
        if self.bugs_battu == self.nombre_de_bugs:
            Texte_de_Mathieu()
            afficher([
            "Bravo, tu as réglé assez de bugs pour réparer le " + self.nom_de_zone + " !",
            "Je savais que tu pouvais le faire.",
            "Voici quelques informations à propos de ce langage :",
            description_de_langage[self.numéro_de_zone],
            "Bref, je me perds dans ce que je dis.",
            "Si tu veux tu peux continuer à battre des bugs ou retourner au village.",
            "Que décide tu ?"], joueur.vitesse_du_texte, "normal")
            print("1 - Battre un bugs | 2 - Retourner au village")
            réponse_bugs_langage_réparé = input()
            if réponse_bugs_langage_réparé == "1":
                saut_de_lignes()
                self.__combat(joueur)
            elif réponse_bugs_langage_réparé == "2":
                afficher(["D'accord, alors j'espère te revoir bientôt !"], joueur.vitesse_du_texte, "normal")
            else:
                afficher(["Désolé mais je n'ai pas compris ta demande...", "Je te laisse retourner au village, j'espère te revoir bientôt !"], joueur.vitesse_du_texte, "normal")
        else:
            Texte_de_Mathieu()
            afficher(["Veux-tu combattre un bugs ? "], joueur.vitesse_du_texte, "normal")
            print("1 - Oui (combattre un bugs) | 2 - Non (retourner au village)")
            réponse_bugs = input()
            if réponse_bugs == "1":
                saut_de_lignes()
                self.__combat(joueur)
            elif réponse_bugs == "2":
                print(f"{Fore.RED}ATTENTION: Votre avencement sur ce langage sera perdu mais l'argent et l'expérience acquises resteront !{Style.RESET_ALL}")
                print("Etes-vous sur de votre choix ?\n1 - Oui | 2 - Non")
                réponse_bugs_abandon = input()
                if réponse_bugs_abandon == "1":
                    afficher(["D'accord, alors j'espère te revoir bientôt !"], joueur.vitesse_du_texte, "normal")
                else:
                    saut_de_lignes()
                    self.demande_de_combat(joueur)
            else:
                afficher(["Désolé mais je n'ai pas compris votre demande..."], joueur.vitesse_du_texte, "normal")
                saut_de_lignes()
                self.demande_de_combat(joueur)
        

    def __combat(self, joueur):
        print("Lancement du combat contre un bugs !\n")
        bugs = self.vie_des_bugs
        tour = 1
        while not (joueur.vie == 0 or bugs == 0):
            qui_commence = random.randint(1,2)
            if qui_commence == 1:
                print("Tour " + str(tour) + " - Vous commencez à attaquer :")
                attaque = random.randint(1,5) * joueur.sac[joueur.objet_en_main][1]
                bugs = bugs - attaque
                if bugs < 0:
                    bugs = 0
                print("Vous enlevez " + str(attaque) + " PV à votre adversaire, il a désormais " + str(bugs) + " PV.")
                if bugs != 0:
                    print("Tour " + str(tour) + " - Le bugs vous attaque :")
                    attaque_bugs = random.randint(self.dégats_minimal_des_bugs,self.dégats_maximal_des_bugs)
                    joueur.vie = joueur.vie - attaque_bugs
                    if joueur.vie < 0:
                        joueur.vie = 0
                    print("Il vous enlève " + str(attaque_bugs) + " PV, vous avez désormais " + str(joueur.vie) + " PV.")
            else:
                print("Tour " + str(tour) + " - Le bugs commence à attaquer :")
                attaque_bugs = random.randint(self.dégats_minimal_des_bugs,self.dégats_maximal_des_bugs)
                joueur.vie = joueur.vie - attaque_bugs
                if joueur.vie < 0:
                    joueur.vie = 0
                print("Il vous enlève " + str(attaque_bugs) + " PV, vous avez désormais " + str(joueur.vie) + " PV.")
                if joueur.vie != 0:
                    print("Tour " + str(tour) + " - Vous attaquez le bugs :")
                    attaque = random.randint(1,5) * joueur.sac[joueur.objet_en_main][1]
                    bugs = bugs - attaque
                    if bugs < 0:
                        bugs = 0
                    print("Vous enlevez " + str(attaque) + " PV à votre adversaire, il a désormais " + str(bugs) + " PV.")
            tour = tour + 1
            saut_de_lignes()
        if bugs == 0:
            print("Vous avez battu un bugs !")

            self.bugs_battu = self.bugs_battu + 1
            argent_gagné = random.randint(2 * (self.numéro_de_zone + 1), 7 * (self.numéro_de_zone + 1))
            joueur.argent = joueur.argent + argent_gagné
            print("Vous avez gagné " + str(argent_gagné) + " bitcoins, vous êtes maintenant à " + str(joueur.argent) + " bitcoins.")

            expériences_gagné = random.randint(5 * (self.numéro_de_zone + 1), 20 * (self.numéro_de_zone + 4))
            joueur.expérience = joueur.expérience + expériences_gagné
            print("Vous avez gagné " + str(expériences_gagné) + " xp.")
            joueur.regarde_experience()

            jeu = Initialisation(joueur.dossier_du_jeu)
            jeu.sauvegarder(joueur)

            saut_de_lignes()
            self.demande_de_combat(joueur)
        else:
            print("Vous êtes mort !")
            joueur.argent = 0
            joueur.vie = joueur.vie_maximal
            print("Vous avez perdu l'argent que vous avez et vous allez être soigné.")
#endregion

#region Jeu
print('\n'*100)  #Clear la console (si la ligne d'après ne marche pas)
os.system('cls') #Clear la console

print(f"{Fore.GREEN}==================================================================================================================================================================================================")
print("Bienvenue sur :")
print("")
print(" /$$ /$$               /$$     /$$                                                         /$$                           /$$                                                                      ")
print("| $$| $/              | $$    | $$                                                        | $$                          | $$                                                                      ")
print("| $$|_/     /$$$$$$  /$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$         /$$$$$$$  /$$$$$$   /$$$$$$$      | $$  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$$")
print("| $$       |____  $$|_  $$_/|_  $$_/   |____  $$ /$$__  $$| $$  | $$ /$$__  $$       /$$__  $$ /$$__  $$ /$$_____/      | $$ |____  $$| $$__  $$ /$$__  $$ |____  $$ /$$__  $$ /$$__  $$ /$$_____/")
print("| $$        /$$$$$$$  | $$    | $$      /$$$$$$$| $$  \ $$| $$  | $$| $$$$$$$$      | $$  | $$| $$$$$$$$|  $$$$$$       | $$  /$$$$$$$| $$  \ $$| $$  \ $$  /$$$$$$$| $$  \ $$| $$$$$$$$|  $$$$$$ ")
print("| $$       /$$__  $$  | $$ /$$| $$ /$$ /$$__  $$| $$  | $$| $$  | $$| $$_____/      | $$  | $$| $$_____/ \____  $$      | $$ /$$__  $$| $$  | $$| $$  | $$ /$$__  $$| $$  | $$| $$_____/ \____  $$")
print("| $$$$$$$$|  $$$$$$$  |  $$$$/|  $$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$/|  $$$$$$$      |  $$$$$$$|  $$$$$$$ /$$$$$$$/      | $$|  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$|  $$$$$$$ /$$$$$$$/")
print("|________/ \_______/   \___/   \___/   \_______/ \____  $$ \______/  \_______/       \_______/ \_______/|_______/       |__/ \_______/|__/  |__/ \____  $$ \_______/ \____  $$ \_______/|_______/ ")
print("                                                      | $$                                                                                       /$$  \ $$           /$$  \ $$                    ")
print("                                                      | $$                                                                                      |  $$$$$$/          |  $$$$$$/                    ")
print("                                                      |__/                                                                                       \______/            \______/                     ")
print("Créer par : TORO Nicolas TG09 | Version : 1.0")
print(f"=================================================================================================================================================================================================={Style.RESET_ALL}")
print("(Si le texte est mal affiché, alors veuillez agrandir la fenêtre ou la dézoomer)\n")

with urlopen("https://pastebin.com/raw/GzQzU2kU") as file:
    version = file.read().decode()
if version != "1.0":
    print(f"{Fore.RED}Une mise à jour est disponible ! Téléchargez-la ici : https://github.com/nt-games-ytb/language-attack/releases/tag/" + version + f"{Style.RESET_ALL}\n")

langage = Langages(True)
village_utilisé = Village(True, True, True, True, True)
joueur_actuel = Joueur("", 100, 100, 0, 0, 0, 1, 0, [["print", 1]], 1, 0.05, os.path.dirname(os.path.realpath(__file__)), "\sauvegarde.xml")

#region Séléction du joueur
jeu = Initialisation(joueur_actuel.dossier_du_jeu)
if jeu.fichier_existe("sauvegarde.xml") == False:
    jeu.creation_de_la_sauvegarde()
    saut_de_lignes()
    jeu.creation_de_joueur(joueur_actuel)
    saut_de_lignes()
    scenario(joueur_actuel)
    saut_de_lignes()
    demande_tutoriel()
else:
    jeu.afficher_les_joueurs("\sauvegarde.xml")
    jeu.chargement_du_joueur("\sauvegarde.xml", joueur_actuel, int(input("Quelle option choisis-tu ? ")))
    village_utilisé.première_fois_village = False
    village_utilisé.première_fois_hopital = False
    village_utilisé.première_fois_banque = False
    village_utilisé.première_fois_shop = False
    langage.première_fois_langage = False
jeu.sauvegarder(joueur_actuel)
village_utilisé.vérifié_le_dossier_son(joueur_actuel.dossier_du_jeu)
saut_de_lignes()
joueur_actuel.afficher_les_caracteristiques()
#endregion

jeu_en_cours = True
while jeu_en_cours == True:
    village_utilisé.village(joueur_actuel, langage)
    jeu.sauvegarder(joueur_actuel)
#endregion