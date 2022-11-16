#region Import modules
import os
from colorama import Fore, Style

try:
    from playsound import playsound
except:
    print(f"{Fore.RED}Nous avons remarqué que vous n'avez pas le module \"Playsound\" !\nNous allons donc vous l'installer :")
    os.system("pip install playsound")
    from playsound import playsound
    print(f"{Style.RESET_ALL}")

import initialisation
import joueur
import langages
import village
#endregion

langage = langages.Langages(True)
village_utilisé = village.Village(True, True, True, True, True)
joueur_actuel = joueur.Joueur("", 100, 100, 0, 0, 0, 1, 0, [["print", 1]], 1, 0.05, os.path.dirname(os.path.realpath(__file__)), "\sauvegarde.xml")

#region Séléction du joueur
jeu = initialisation.Initialisation(joueur_actuel.dossier_du_jeu) #Créer jeu, un objet de la class initailisation qui prend comme attribut le dossier "attaque-des-langages"
if jeu.fichier_existe("sauvegarde.xml") == False: #Si il n'y a pas de sauvegarde
    jeu.creation_de_la_sauvegarde()
    initialisation.saut_de_lignes()
    jeu.creation_de_joueur(joueur_actuel)
    initialisation.saut_de_lignes()
    initialisation.scenario(joueur_actuel)
    initialisation.saut_de_lignes()
    initialisation.demande_tutoriel()
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
initialisation.saut_de_lignes()
joueur_actuel.afficher_les_caracteristiques()
#endregion

#region Jeu
jeu_en_cours = True
while jeu_en_cours == True:
    village_utilisé.village(joueur_actuel, langage)
    jeu.sauvegarder(joueur_actuel)
#endregion