from colorama import Fore, Style
import initialisation

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
        initialisation.saut_de_lignes()

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
        initialisation.saut_de_lignes()
        