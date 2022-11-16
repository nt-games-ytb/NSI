from colorama import Fore, Style
import random
import initialisation

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
        initialisation.Texte_de_Mathieu()
        initialisation.afficher([
        "Tu as débloqué " + str(joueur.langage_débloqué) + " langages sur 30, c'est pas mal, bravo !",
        "Le dernier langage que tu as débloqué est le " + liste_des_langages[joueur.langage_débloqué - 1] + ".",
        description_de_langage[joueur.langage_débloqué - 1],
        "Bref, je me perds dans ce que je dis.",
        "En tout cas, continue comme ça, tu as bientôt finis de le réparer, je crois en toi.",
        "Reviens me voir quand tu veux !"],
        joueur.vitesse_du_texte, "normal")
        initialisation.saut_de_lignes()

    def choix_de_langage(self, joueur):
        if self.première_fois_langage == True:
            initialisation.Texte_de_Mathieu()
            initialisation.afficher([
            "Te voila maintenant à l'intersection.",
            "C'est ici que tu vas choisir un langage à réparer en exertminant les bugs de ce langage.",
            "Tu peux réparer autant de fois que tu veux un langage mais il suffit de réparer seulement une fois un langage pour débloquer le suivant et ainsi de suite."],
            joueur.vitesse_du_texte, "normal")
            self.première_fois_langage = False
        else:
            initialisation.Texte_de_Mathieu()
            initialisation.afficher(["Bonjour !"], joueur.vitesse_du_texte, "normal")
        initialisation.afficher(["Que veux-tu faire ?"], joueur.vitesse_du_texte, "normal")
        print("0 - Retourner au village")
        self.__afficher_les_langages(joueur, liste_des_langages)
        réponse_langage = int(input())
        if réponse_langage == 0:
            initialisation.afficher(["D'accord, alors j'espère te revoir bientôt !"], joueur.vitesse_du_texte, "normal")
        else:
            self.__entrer_dans_une_zone(joueur, réponse_langage)
        initialisation.saut_de_lignes()

    def __afficher_les_langages(self, joueur, liste_langages):
        for numéro_de_langages in range(joueur.langage_débloqué):
            print(str(numéro_de_langages + 1) + " - Réparer le " + liste_langages[numéro_de_langages])

    def __entrer_dans_une_zone(self, joueur, numéro_du_langage):
        if numéro_du_langage > 30:
            print(f"{Fore.RED}Le langage que vous avez demandé n'existe pas !{Style.RESET_ALL}")
            initialisation.saut_de_lignes()
            self.choix_de_langage(joueur)
        else:
            if numéro_du_langage > joueur.langage_débloqué:
                print(f"{Fore.RED}Vous n'avez pas encore débloqué ce langage !{Style.RESET_ALL}")
                initialisation.saut_de_lignes()
                self.choix_de_langage(joueur)
            else:
                zone_choisis = Zone(liste_des_langages[numéro_du_langage - 1], numéro_du_langage - 1, random.randint(5 * numéro_du_langage, 12 * numéro_du_langage), 15 * numéro_du_langage, 3 * numéro_du_langage, 6 * numéro_du_langage, 0)
                initialisation.afficher([
                "Très bien, tu vas donc t'occuper du " + liste_des_langages[numéro_du_langage - 1] + ".",
                "Pour le réparer, il faudra que tu fixes " + str(zone_choisis.nombre_de_bugs) + " bugs.",
                "Bonne chance !"], joueur.vitesse_du_texte, "normal")
                initialisation.saut_de_lignes()
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
            initialisation.Texte_de_Mathieu()
            initialisation.afficher([
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
                initialisation.saut_de_lignes()
                self.__combat(joueur)
            elif réponse_bugs_langage_réparé == "2":
                initialisation.afficher(["D'accord, alors j'espère te revoir bientôt !"], joueur.vitesse_du_texte, "normal")
            else:
                initialisation.afficher(["Désolé mais je n'ai pas compris ta demande...", "Je te laisse retourner au village, j'espère te revoir bientôt !"], joueur.vitesse_du_texte, "normal")
        else:
            initialisation.Texte_de_Mathieu()
            initialisation.afficher(["Veux-tu combattre un bugs ? "], joueur.vitesse_du_texte, "normal")
            print("1 - Oui (combattre un bugs) | 2 - Non (retourner au village)")
            réponse_bugs = input()
            if réponse_bugs == "1":
                initialisation.saut_de_lignes()
                self.__combat(joueur)
            elif réponse_bugs == "2":
                print(f"{Fore.RED}ATTENTION: Votre avencement sur ce langage sera perdu mais l'argent et l'expérience acquises resteront !{Style.RESET_ALL}")
                print("Etes-vous sur de votre choix ?\n1 - Oui | 2 - Non")
                réponse_bugs_abandon = input()
                if réponse_bugs_abandon == "1":
                    initialisation.afficher(["D'accord, alors j'espère te revoir bientôt !"], joueur.vitesse_du_texte, "normal")
                else:
                    initialisation.saut_de_lignes()
                    self.demande_de_combat(joueur)
            else:
                initialisation.afficher(["Désolé mais je n'ai pas compris votre demande..."], joueur.vitesse_du_texte, "normal")
                initialisation.saut_de_lignes()
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
            initialisation.saut_de_lignes()
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

            jeu = initialisation.Initialisation(joueur.dossier_du_jeu)
            jeu.sauvegarder(joueur)

            initialisation.saut_de_lignes()
            self.demande_de_combat(joueur)
        else:
            print("Vous êtes mort !")
            joueur.argent = 0
            joueur.vie = joueur.vie_maximal
            print("Vous avez perdu l'argent que vous avez et vous allez être soigné.")

