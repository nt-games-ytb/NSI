import os
import time
from colorama import Fore, Style
import ast
import xml.dom.minidom

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
                #Faut que sa les changes
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
        #fichier_xml_de_sauvegarde.writexml(open(joueur.dossier_du_jeu  + joueur.fichier_de_sauvegarde, "w"))
        with open(joueur.dossier_du_jeu  + joueur.fichier_de_sauvegarde, "w") as fichier_xml:
            fichier_xml.write(fichier_xml_de_sauvegarde.toprettyxml()) #Meilleur rendu

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