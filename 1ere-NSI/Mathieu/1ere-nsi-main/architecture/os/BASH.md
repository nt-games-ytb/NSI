> Les systèmes d'exploitations Linux étant notamment dans le domaine des serveurs informatique - en opposition aux machines dites "clients" - il est courant de n'utiliser qu'un seul outil pour les contrôler : Bash, l'interprète de commande.

Contrairement aux systèmes "user-friendly", comprendre, simple d'utilisation, les machines sous Linux ont la réputation d'être réservées aux utilisateurs et utilisatrices qui maîtrisent leur sujet.

Heureusement pour nous, ça n'est pas aussi compliqué que cela en a l'air. Dans [l'activité Terminus](terminus.ipynb) que nous avions faite, nous avons appris certaines commandes linux, dans le but de progresser dans le jeu. Ici, cela sera pareil, l'interface de jeu en moins évidemment ;) 

### Un peu de culture

Sous windows, macOS ou GNU/Linux, chaque système propose son propre interpreteur de commande :

- BASH (Bourne Again Shell)
  - principalement sous linux et macOS , mais disponible sous windows.
  
- SHELL
  - Le premier interpreteur, qui date de [1971](https://fr.wikipedia.org/wiki/Shell_Unix) 
  - il a évidemment été amélioré au fur et à mesure des versions.
  
- Chaque version utilise son propre langage pour utiliser les commandes systèmes, mais en général, vous pouvez vous y retrouver d'un OS à un autre, avec les bonnes bases.

  ------------

  

### Commandes de bases

| Commande | Description                                                  |
| -------- | ------------------------------------------------------------ |
| ls       | Liste le contenu du répertoire courant dans lequel vous vous situez. |
| cp       | Copie des fichiers ou des dossiers.                          |
| mv       | Déplace ou renomme des fichiers ou des dossiers.             |
| rm       | Supprime un ou plusieurs fichiers.                           |
| cd       | Se déplace dans l'arborescence (Change de dossier courant)   |
| cat      | Affiche le contenu d'un fichier.                             |
| touch    | Crée un fichier vide.                                        |
| mkdir    | Crée un dossier vide                                         |
| rmdir    | Supprime un dossier.                                         |



---------------

### Introduction au script. 

### Pourquoi le bash ?

Il existe autant de langage de programmation qu’il existe de besoins. Aucun d’entre eux n’est meilleur qu’un autre, il n'y a que des langages plus efficaces que d’autres selon les situations.

Dans notre cas, afin d’être capable d’opérer une administration des systèmes efficace, le langage **Shell** est un must have.

 La syntaxe de **Shell**, à la fois simple et efficace, permet à n’importe qui de pouvoir « *programmer* » de cette manière. La plupart des fonctions et opérations propres au **Shell** sont faciles à retenir, de plus, les scripts fonctionneront souvent du premier coup si vous maitrisez un tant soit peu le langage.

### Définition

 

>  Le **Shell** est un interpréteur de commandes, ainsi qu’un langage de programmation puissant.

Un programme **Shell**, que l’on peut appeler également un **script**, est un outil facile à prendre en main afin de construire des applications en « regroupant » des appels système, outils, utilitaires et binaires compilés. 

Un **script Shell** permet, en théorie, d’accéder à l’entièreté des commandes **UNIX**, des utilitaires et des outils systèmes. 

Le Shell est particulièrement efficace lorsque l’on effectue de l’administration système mais aussi pour d’autres routines répétitives ne nécessitant pas des utilisations aussi poussées qu’avec un langage de programmation plus complet.

-------------------



### Comment ?

Dans le cas le plus simple, un **script** n'est rien de plus qu'une liste de commandes système enregistrées dans un fichier, ligne par ligne.  Cela évite l'effort de retaper cette séquence particulière de commandes à chaque fois qu'elle doit être appelée.

Par exemple, pour se déplacer dans un répertoire puis créer un dossier, on utilise le **bash** (ou un autre interpréteur de commande **UNIX**) :

```
cd Documents/
mkdir test
```

Eh bien si l’on souhaite faire la même chose avec un **script**, il suffira d’écrire ces deux lignes à la suite dans un fichier, c’est tout simple.

Evidemment, placer ces commandes dans un fichier **script** n’a pas uniquement comme intérêt de ne pas avoir à les recopier chaque fois que l’on en a besoin.  Le **script** est un outil de travail et peut facilement être modifié ou personnalisé pour une application particulière.

En réalité, il manque juste une chose afin de pouvoir utiliser ces lignes dans un **script**.

Votre fichier script doit comporter **un sha-bang (#!).**

**Le *sha-bang* (#!)** doit se placer en tête du script afin d’indiquer à votre système que ce fichier est un ensemble de commandes à interpréter. 

Les caractères **#!** correspondent en fait à un ***nombre magique***, un marqueur spécial qui désigne un type de fichier, ou dans ce cas, **un script Shell** exécutable.

Ensuite, après le **sha-bang,** se trouve un *chemin*, qui mène au programme sensé interpréter les commandes de votre fichier script, selon le langage que vous utilisez.

Enfin, cet interpréteur de commande exécute les commandes de votre **script**, en commençant après le sha-bang, et en ignorant les commentaires.

Vu qu’ici, nous utilisons l’interpréteur bash, voici la ligne correspondante :

```
#!/bin/bash
```

-------------



### Appeler son script

###  

Après la création de votre premier script, vous souhaiterez l’exécuter (on parle ici d’un appel ) afin de vous assurer de son bon fonctionnement.

> Un code de retour zéro du script indique un succès au **Shell**.

 

Dans cette optique, plusieurs solutions s’offrent à vous :

-  Dans un terminal, la commande **sh** <nom du script> 

-  Dans un terminal, la commande **bash** <nom du script>

-  Rendre d’abord exécutable ce fichier 

 

- **chmod 555** <nom du script>(donne les droits de lecture/exécution à tout le monde) 

- **chmod +rx** <nom du script> (donne les droits de lecture et d'exécution à tout le monde)

- **chmod u+rx** <nom du script>(donne les droits de lecture et d'exécution seulement à son propriétaire)

 

 Puis l’exécuter :

 

```
./nomdufichier
```

*Note : si vous placez votre script fonctionnel dans le répertoire /usr/local/bin alors vous serez en mesure de l’appeler simplement en tapant son nom puis entrée dans un terminal.*

> Auteur : Florian Mathieu
>
> Licence CC BY NC
>
> <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Licence Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a> <br />Ce cours est mis à disposition selon les termes de la <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Licence Creative Commons Attribution - Pas d’Utilisation Commerciale - Partage dans les Mêmes Conditions 4.0 International</a>.