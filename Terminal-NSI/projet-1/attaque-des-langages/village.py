import os
from colorama import Fore, Style
from playsound import playsound
import initialisation

#Mathieu = rouge
#Texte = normal
#Banquier = jaune
#Infirmière joelle = mangeta
#Vendeur = noir


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
            initialisation.Texte_de_Mathieu()
            initialisation.afficher(["Je te présente le village, c'est ici que tu habites.",
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
        initialisation.saut_de_lignes()
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
            initialisation.afficher(["Bienvenue à l'hopital, je suis l'infirmière Joelle et je suis là pour vous soigner !"], joueur.vitesse_du_texte, "normal")
            self.première_fois_hopital = False
        else:
            print(f"{Fore.MAGENTA}Infirmière Joelle:{Style.RESET_ALL} ", end="")
            initialisation.afficher(["Bonjour !"], joueur.vitesse_du_texte, "normal")
        initialisation.afficher(["Voulez-vous être soigné ?"], joueur.vitesse_du_texte, "normal")
        print("1 - Oui | 2 - Non")
        réponse_hopital = input()
        if réponse_hopital == "1":
            self.soin(joueur, joueur.vie_maximal)
        elif réponse_hopital == "2":
            initialisation.afficher(["D'accord, alors j'espère vous revoir bientôt !"], joueur.vitesse_du_texte, "normal")
        else:
            initialisation.afficher(["Désolé mais je n'ai pas compris votre demande...", "Je vous laisse retourner au village, j'espère vous revoir bientôt !"], joueur.vitesse_du_texte, "normal")
        initialisation.saut_de_lignes()
    
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
            initialisation.afficher(["Bienvenue à la banque, je suis votre banquier et c'est moi qui vais gérer votre argent !"], joueur.vitesse_du_texte, "normal")
            self.première_fois_banque = False
        else:
            print(f"{Fore.YELLOW}Banquier:{Style.RESET_ALL} ", end="")
            initialisation.afficher(["Bonjour !"], joueur.vitesse_du_texte, "normal")
        initialisation.afficher(["Que voulez-vous faire ?"], joueur.vitesse_du_texte, "normal")
        print("1 - Déposer de l'argent\n2 - Retirer de l'argent\n3 - Retourner au village")
        réponse_banque = input()
        if réponse_banque == "1":
            self.__deposer_argent(joueur, int(input("Combien d'argent voulez-vous déposer ? ")))
        elif réponse_banque == "2":
            self.__retirer_argent(joueur, int(input("Combien d'argent voulez-vous retirer ? ")))
        elif réponse_banque == "3":
            initialisation.afficher(["D'accord, alors j'espère vous revoir bientôt !"], joueur.vitesse_du_texte, "normal")
        else:
            initialisation.afficher(["Désolé mais je n'ai pas compris votre demande...", "Je vous laisse retourner au village, j'espère vous revoir bientôt !"], joueur.vitesse_du_texte, "normal")
        initialisation.saut_de_lignes()
        
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
            initialisation.afficher(["Bienvenue au shop, je suis le vendeur du village, si vous voulez acheter quelque chose c'est ici qu'il faut venir !"], joueur.vitesse_du_texte, "normal")
            self.première_fois_shop = False
        else:
            print(f"{Fore.BLACK}Vendeur:{Style.RESET_ALL} ", end="")
            initialisation.afficher(["Bonjour !"], joueur.vitesse_du_texte, "normal")
        self.__afficher_le_shop(joueur, items_du_shop)
        initialisation.afficher(["Que voulez-vous faire ?"], joueur.vitesse_du_texte, "normal")
        print("(Indiquer le numéro de l'item à acheter ou mettez 0 pour retourner au village)")
        réponse_shop = int(input())
        if réponse_shop == 0:
            initialisation.afficher(["D'accord, alors j'espère vous revoir bientôt !"], joueur.vitesse_du_texte, "normal")
        else:
            if réponse_shop > len(items_du_shop):
                initialisation.afficher(["Désolé mais je n'ai pas cet item...", "Je vous laisse retourner au village, j'espère vous revoir bientôt !"], joueur.vitesse_du_texte, "normal")
            else: 
                self.__acheter_au_shop(joueur, réponse_shop)
        initialisation.saut_de_lignes()
        
    def __afficher_le_shop(self, joueur, liste_des_items_du_shop):
        initialisation.afficher(["Voici ce que vous pouvez acheter :"], joueur.vitesse_du_texte, "normal")
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
