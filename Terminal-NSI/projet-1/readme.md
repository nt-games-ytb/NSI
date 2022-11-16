Ceci est la version donné au professeur. La dernière version ce trouve ici : https://github.com/nt-games-ytb/language-attack.    

# Projet de NSI n°1 - TORO Nicolas TG09 :
# L'attaque des langages

## Consignes
- Créer un programme Python faisant intervenir les classes
- Groupe de 1 ou 2 élèves
- Le reste du projet est libre

## But du pojet
Créer un jeu en python utilisant différentes classes. Ce jeu est un RPG consistant à vaincre les bugs (ou zombies) des différents langages de programmation classés du plus récent au plus ancien pour à la fin les réparer.

## Scènario
Grâce aux cours de M.Duranton et de M.Maurice, les élèves de terminal du lycée Thierry Maulnier apprennent le python mais bien sur cela ne se passe pas comme prévu. Certains élèves sont perdus, d'autres n'écoutent pas ou utilisent leur téléphone portable et même certains ont mis 2 semaines pour arriver en cours... Heureusement, vous, vous arrivez à remonter le niveau de cette classe désastreuse. C'est alors qu'un beau jour, à force d'une utilisation déplorable de Python avec EduPython qui crashait toutes les 2 minutes, qu'une faille se créa. Cette faille permit l'entrer à de nombreux bugs dans les différents langages de programmation existants. Etant le seul capable de faire un script python dans votre classe, vous allez essayer de faire disparaitre et de supprimer ces bugs. Cela ne va pas être si simple mais M.Mathieu (ancien professeur de NSI au lycée Thierry Maulnier) sera là pour vous épauler et pour aider à détruire ces bugs. Alors, pourrez-vous exterminer tous ces bugs et ainsi réparer les divers langages de programmation ? 

## Objectifs
*Les commentaires sont en italic*    
*Les mots en gras représentent des noms de fonctions ou de variables*    
*Les mots et phrases barré sont les choses abandonnées (soit parce que ce n'est pas possible avec le materiel du lycée ou soit pour d'autres raisons)*    

### Général et jeu :
- [ ] Faire que le jeu soit joueable    
- [X] Utiliser **Colorama**. Comme les ordinnateurs du lycée ne sont pas perfommant, possèdent peu de librairy pré-installé et comme on ne peut pas en installer d'autres, alors j'ai choisis d'utiliser **Colorama**. C'est l'une des plus populaire et elle fonctionne parfaitement avec les ordinateurs du lycée.    
- [X] Lors du lancement du jeu si le fichier "sauvegarde.xml" existe lancer la fonction **afficher_les_joueurs** sinon lancer la fonction **creation_de_la_sauvegarde**.    
- [ ] Dès qu'un joueur finit le jeu alors un Rick Roll avec les crédits se lance puis le jeu finit par s'arrêter.    
- [X] Faire une boucle (un while de préfèrence) pour le jeu ne s'arrête jamais.    
- [ ] Faire une fonction publique nommé **"tutoriel"** qui sera très simplifier et qui n'utilisera pas les fonctions déjà créer pour ne pas altérer sur le jeu. Les bugs (ou zombies) seront 5 bugs en python.    
- [X] Faire une fonction publique nommé **"afficher"** qui prend comme paramètre **"textes"** (une liste ou un tuple où chaque élément est une phrase), **"temps"** (un integer qui sera généralement la **vitesse_du_texte** du joueur) et **"couleur"** (un string qui sera une couleur). Elle affichera sur la même ligne *(end="")* les caractères de chaque phrase de **textes** un par un avec une pause de durée **temps** entre chaqué caractère. Le script devra activer la couleur au début de la fonction, puis, devra la reset à la fin. Emettre un son à chaque écriture de cractère.    

#### Initialisation et XML :
- [X] Faire une fonction privée nommé **"creation_de_sauvegarde"** qui créera un fichier nommé "sauvegarde.xml" (dans le dossier "attaque-des-langages") et qui contiendra les bases.    
- [X] Faire une fonction privée nommé **"creation_de_joueur"** qui demandera un nom de joueur, qui créera **"joueur_actuel"** avec la classe **joueur** et qui sauvegardera ce joueur dans le fichier "sauvegarde.xml". Si le nom choisis existe déjà alors demander un autre nom jusqu'à ce l'utilisateur trouve un nom qui n'existe pas dans le fichier. Enfin quand on est bon, le jeu demande si il veut lancer le tutoriel. Si oui alors il lance la fonction **tutoriel**.    
- [x] Faire une fonction privée nommé **"afficher_les_joueurs"** qui lira les joueurs sauvegardé dans le fichier "sauvegarde.xml" et qui les affichera un par un (avec une numérotation).    
- [X] Faire qu'après avoir afficher les joueurs (grâce à la fonction **afficher_les_joueurs**), le script nous demande le numéro du joueur et lancera ensuite **chargement_du_joueur**.    
- [X] Faire une fonction privée nommé **"chargement_du_joueur"** qui prend comme paramètre **"numéro_du_joueur"** (un integer), qui lira données du joueur choisis (grâce au **numéro_du_joueur**) et qui avec, créera **"joueur_actuel"** avec la classe **joueur**.    
- [X] Faire une fonction public nommé **"sauvegarder"** qui prend comme paramètre **"joueur"** (un integer), soit le **joueur_actuel** au quelle ses données seront sauvegarder dans le fichier "sauvegarde.xml". Elle sera utilisé souvent pour ne pas avoir de problème si le jeu plante où si un problème apparait.    

### Village :
- [X] Faire une fonction privée nommé **"village"** qui nous eméne au village.    
Quand on est dans le villages, on doit avoir un menu qui nous demande ce qu'on veut faire, soit :    
Parler à M.Mathieu (si l'option est choisis alors M.Mathieu vous redira les dernières choses qu'il vous as précédement dite (en les affichant avec la fonction **afficher**, prenant dans la liste **texte_de_mathieu** et en les choisisant avec l'argument **mathieu** de **joueur**))    
Aller à l'hopîtal (si l'option est choisis alors lance la fonction **hopital**)    
Aller à la banque (si l'option est choisis alors lance la fonction **banque**)    
Aller au shop (si l'option est choisis alors lance la fonction **shop**)   
Aller combatre les bugs (si l'option est choisis et si le joueur a de la vie alors lance la fonction **choix_de_langage**)   
Arrêter de jouer (si l'option est choisis alors lance la fonction **sauvegarder** et arrête le programme)    


#### Hopital :
- [x] Faire une fonction privée nommé **"soin"** qui prend comme paramètre **"vie"** (un integer), soit la vie qui sera ajoutée à vos **point_de_vie**. Si votre vie dépasse ensuite votre **vie_maximale** alors votre vie sera égale à votre **vie_maximale**.    
- [X] Faire une fonction privée nommé **"hopital"** qui vous demandera si vous êtes sur de vouloir vous soigner, si oui alors lancer la fonction **soin** avec comme paramètre la **vie_maximale** sinon retour au village.    

#### Banque :
- [x] Faire une fonction privée nommé **"déposer_argent"** qui prend comme paramètre **"argent"** (un integer), soit l'argent que le script prendra de l'argument **argent**"** pour le mettre dans l'argument **argentSauvegardé**. Si le nombre est trop grand alors le jeu doit informer le joueur.    
- [X] Faire une fonction privée nommé **"retirer_argent"** qui prend comme paramètre **"argent"** (un integer), soit l'argent que le script prendra de l'argument **argentSauvegardé** pour le mettre dans l'argument **argent**. Si le nombre est trop grand alors le jeu doit informer le joueur.    
- [X] Ajouter un son spéciales pour ces deux fonctions.    
- [X] Faire une fonction privée nommé **"banque"** qui vous demandera ce vous voulez faire à la banque, selon le choix, le script lancera les fonctions **déposer_argent**, **retirer_argent** ou retounera au village.    

#### Shop : 
- [X] Faire une fonction privée nommé **"afficher_le_shop"** qui prend comme paramètre **"items_du_shop"** (une liste qui contient une liste pour chaque items) avec laquelle il va afficher chaque items du shop ainsi que ses caractèristiques *(Pour plus tard : mettre du couleur spéciale pour les items déjà changer)*.    
- [X] Faire une fonction privée nommé **"acheter_au_shop"** qui prend comme paramètre **"numéro_items"** (un integer), soit le numéro de l'items qu'il va d'abords regarder si tu le joueur le possède et si il le possède pas alors il va regarder si le joueur à assez d'argent, si il en a assez alors à ce moment là, le jeu va mettre le nouvelle item dans le **sac**. Emettre un son lorsque l'achat est effectué. *(Pour plus tard : si c'est une arme alors demander si le joueur veut prendre en main l'items)*    
- [X] Faire une fonction privée nommé **"shop"** qui lancera directement **afficher_le_shop**, puis, qui vous demandera ce vous voulez faire au shop, selon le choix, le script lancera **acheter_au_shop** (avec le **numéro_items** demandé) ou retournera au village.    

### Joueur :
*Pas encore tout fait pour cette partie*    
- [ ] L'init...    
- [ ] **"monter_de_niveau"**...    
- [ ] **"regarde_si_monté_de_niveau"**...    
- [ ] Le sac...    

### Langages :
- [ ] Faire une fonction privée nommé **"choix_de_langage"** qui lancera directement **afficher_les_langages**, puis, qui vous demandera ce que vous voulez faire, selon le choix, le script lancera la fonction **entrer_dans_une_zone** (avec le **numéro_du_langage** demandé) ou retournera au village.     
- [ ] Faire une fonction privée nommé **"afficher_les_langages"** qui prend comme paramètre **"liste_des_langages"** et qui les affiche un par un en partant de 0 jusqu'au nombre de **langage_débloqué**.    
- [ ] Faire une fonction privée nommé **"entrer_dans_une_zone"** qui prend comme paramètre **"numéro_du_langage"**, qui va créer une **"zone"** avec le **"nombre_de_bugs"** à battre (en choissant un nombre aléatoire entre 1 * **numéro_du_langage** et 10 * **numéro_du_langage**), la **"vie_des_bugs"** (soit 15 * **numéro_du_langage**, les **"dégats_des_bugs"** (soit 3 * **numéro_du_langage**) et les **"bugs_battu**. Enfin, elle va lancer **demande_de_combat**.    
- [ ] Faire une fonction privée nommé **"demande_de_combat"** qui affichera les **"bugs_battu"** sur le **"nombre_de_bugs"** à battre, qui vous demandera ce que vous voulez faire, selon le choix, le script lancera la fonction combat **combat** ou retournera au village. Si le nombre de **bugs_battu** est égale au **nombre_de_bus** alors ajouter 1 à **langage_débloqué**. *Problème à régler : on peut refaire autant de fois le même langage pour augmenter son nombre de **langage_débloqué** -> il faudrait que cette événement soit sauvegardé dans le joueur -> avec une liste de boolean spécialement pour ça*     
- [ ] Faire une fonction privée nommé **"combat"** qui ne s'arrêtera pas tant que **vie** ou **vie_du_bug** n'est pas égale à 0. Avant que cette boucle ce fasse, le jeu chossiera aléatoirement qui commencera à attaquer. Pendant cette boucle, le joueur (ou le bugs, en fonction de la personne qui commence). Quand il y en a un qui meurt, si c'est le joueur alors il est mort et retourne à l'**hopital**, sinon son **argent** augmente (en choissant un nombre aléatoire entre 1 * **numéro_du_langage** et 5 * **numéro_du_langage**), son **expérience** augmente (en choissant un nombre aléatoire entre 1 * **numéro_du_langage** et 20 * **numéro_du_langage**), elle lance **regarde_si_monté_de_niveau** et pour finir, elle lance **demande_de_combat**.    


### Pour plus tard
- [ ] ~~Adapter certaines fonctions qui demande demande des chiffres pour exercer certaines actions en button avec **Curses** (voir [exemple](https://www.youtube.com/watch?v=Db4oc8qc9RU)).~~    
- [ ] Faire différents mode jeu (choisisable lors de la création du joueur). Pour le moment, le jeu est en facile (quand on meurt, on ne perd rien) mais au futur on pourra être en : normal (quand on meurt, on perd notre argent), difficile (quand on meurt, on perd notre argent et le contenue de notre sac est remis à zéro *le joueur devra donc avoir en main l'arme __print__)* et hardcore (quand on meurt, le jeu se termine)    
- [ ] Ajouter des objets de soin avec comme nom __"+"__, __"/"__, __"="__, etc    
- [ ] Faire une fonction publique nommé **"paramètre"** qui nous permettra de modifier le **son**, la **vitesse_du_texte**, etc    
- [ ] Faire qu'on puisse mettre en pause une zone    

## Difficultées rencontrer
- Trouver l'idée du projet    
- Création du scènario
- Bugs selon les interpréteur (la console de pyzo qui n'est pas en UTF-8, Thonny et EduPython qui n'ont pas les modules de base...)     

*Afficher, init joueur, village ou langage*
- [X] Son dans afficher
- [X] problème avec afficher dans le fichier principale
~~- [ ] fond noir~~
- [X] Adapter le texte du début sur pyzo
- [ ] Faire les assert
- [ ] Faire qu'on puisse changer le dossier de sauvegarde
- [ ] Changer le texte de bienvenu car trop grand pour pizo...
- [ ] se battre contre mathieu à la fin