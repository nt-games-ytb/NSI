## Machine de Turing

Cette machine est constituée :

- D' un **ruban infini** divisé en cases consécutives. Chaque case contient un symbole d'un *alphabet*. L'alphabet contient un symbole spécial appelé « symbole  blanc », et un ou plusieurs autres  symboles. Le ruban est supposé être de longueur infinie vers la gauche  ou vers la droite, en d'autres termes la machine doit toujours avoir  assez de longueur de ruban pour son exécution. On considère que les  cases du ruban contiennent par défaut le « symbole blanc » .

- Une **tête de lecture/écriture**  (ci-dessous le **`V`**) qui peut lire et écrire les symboles sur le ruban, et se déplacer vers la gauche ou vers la droite du ruban

- Un **registre d'état** qui mémorise l'état courant de la machine  de Turing. Le nombre d'états possibles est toujours fini, et il existe  un état spécial appelé « état de départ » qui est l'état initial de la  machine avant son exécution.

- Une **table d'actions** qui indique à la machine quel symbole écrire sur le ruban, comment déplacer la tête de lecture (vers la droite ou la gauche), et quel est le nouvel état, en fonction  du symbole lu sur le ruban et de l'état courant de la machine. Si aucune action n'existe pour une combinaison donnée d'un symbole lu et d'un  état courant, la machine s'arrête.

  

**Exemple : voici l'algorithme permettant d'ajouter 1 à un nombre binaire.**

Choisissez un nombre binaire et écrivez le à droite de la tête de lecture (par exemple 101).

|      |      |      |      |      |      |      |      |      |      | V    |      |      |      |      |      |      |      |      |      |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|      |      |      |      |      |      |      |      |      |      |      | 1    | 0    | 1    |      |      |      |      |      |      |

Réalisez pas à pas l'algorithme ci-dessous :

- la machine lit chaque case de gauche à droite jusqu'à tomber sur une case vide. Il y a alors deux cas possibles:
  - Si la dernière case mémorisée dans le registre d'état est un 0 alors la machine se décale d'une case à gauche et écrit 1 puis retourne dans sa position initiale. .
  - Si la dernière case est un 1, la machine se décale d'une case à gauche et :
    - si cette case vaut 1, elle écrit 0 puis se décale à gauche et recommence le point précédent.
    - si cette case vaut 0 ou est vide, elle écrit 1 puis retourne à sa position initiale.

*Etape 1* : la machine va à droite jusqu'à la première case vide.

|      |      |      |      |      |      |      |      |      |      |      |      |      |      | V    |      |      |      |      |      |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|      |      |      |      |      |      |      |      |      |      |      | 1    | 0    | 1    |      |      |      |      |      |      |

*Etape 2*  : la dernière case lue est ... donc ...

|      |      |      |      |      |      |      |      |      |      |      |      |      | V    |      |      |      |      |      |      |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|      |      |      |      |      |      |      |      |      |      |      | 1    | 0    | 0    |      |      |      |      |      |      |

*Etape 4* : ...

|      |      |      |      |      |      |      |      |      |      |      |      | V    |      |      |      |      |      |      |      |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|      |      |      |      |      |      |      |      |      |      |      | 1    | 1    | 0    |      |      |      |      |      |      |

*Etape 5* : ...

|      |      |      |      |      |      |      |      |      |      | V    |      |      |      |      |      |      |      |      |      |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|      |      |      |      |      |      |      |      |      |      |      | 1    | 1    | 0    |      |      |      |      |      |      |

Vous trouverez [sur ce site](http://zanotti.univ-tln.fr/turing/turing.php) un simulateur d'une machin de de Turing si vous souhaitez aller plus loin.

ll faut garder à l'esprit que la machine de Turing est un modèle  universel de calcul et qu'elle peut calculer tout ce que n'importe quel  ordinateur physique peut calculer (aussi puissant soit-il).  In­ver­sement, ce qu'elle ne peut pas calculer ne peut l'être non plus  par un ordinateur. Elle résume donc de manière saisissante le concept d'*ordinateur* et constitue un support idéal pour raisonner autour de la notion d'*algorithme* de *calcul* ou de *démonstration*.  En terminale, nous étudierons plus en détail le concept de calculabilité.