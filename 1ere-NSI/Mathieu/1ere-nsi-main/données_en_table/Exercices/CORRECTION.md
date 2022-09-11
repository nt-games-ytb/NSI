## Exercices



### 1. Manipulation de fichiers CSV

- On peut représenter un enregistrement par un dictionnaire.
- Une virgule (CSV : Comma Separated Values - Valeurs séparées par une virgule). Néanmoins, le format CSV autorise d'autres séparateurs.
- La table étant une liste de dictionnaires, on obtient donc le premier élèment de la liste, c'est à dire un dictionnaire, donc une ligne de la table.




----------



### 2. Opérations sur les tables



- Pour selectionner des colonnes selon un critère donné, on va utiliser la fonction projection.

```python
def projection(table, liste_attributs):
  return [{clé:ligne[clé] for clé in ligne if clé in liste_attributs} for ligne in table]
```

- La fonction *select* ici va selectionner les lignes dont une des valeurs vaut au moins 19.


- Il y a deux (2) noms qui sont communs aux tables : on aura donc deux (2) lignes. De plus, la table U rajoute ses deux (2) colonnes (âge, mail) au quatre de la table T : on aura donc 6 (six) colonnes.



---------



### 3. Determiner des fonctions basiques

- Puisqu'il s'agit de compter le nombre de lignes, donc d'enregistrement, on peut donc utiliser la fonction *len* pour obtenir la longueur de la liste de dictionnaires.

```python
def cardinalité(table):
  return len(table)
```



- La liste des attributs d'une table = 



-------------



### 4. Reconnaître une fonction

Quel est le principe de la fonction suivante :

```python
def mystère(t, cs):
  t_p = []
  for l in t :
    nvlle_l = {}
    for c in l:
      if c in cs:
        nvelle_l[c] = l[c]
    t_p.append(nvelle_l)
  return t_p  
```



### 5. Tester la cohérence d'une table

- Determiner une fonction *coherence*(table) qui teste si chaque ligne a le même ensemble d'attributs.
- Determiner une fonction *doublons*(table, attribut) qui vérifie si un attribut de référerence apparaît deux fois avec la même valeur dans une table.

### 6. Lier tableur, fichier CSV et liste de dictionnaires

On dispose d'une liste de dictionnaires suivante :

```python
PlanningTwitch =[{'NomStream' : 'AntoineDaniel', 'Genre' : 'M', 'Jeu' : 'Fall_Guys','Numéro' : '1'},{'NomStream' : 'MV', 'Genre' : 'M', 'Jeu' : 'Isaac','Numéro' : '2'}, {'NomStream' : 'AngleDroit', 'Genre' : 'F', 'Jeu' : 'Fall_Guys','Numéro' : '3'}, {'NomStream' : 'BagheraJones', 'Genre' : 'F', 'Jeu' : 'Fall_Guys','Numéro' : '4'}]
```

- On travaille avec le tableur LibreOffice Calc de la suite LibreOffice qui produit des fichiers au format ont (alors qu'Excel de la suite Microsoft Office produit des fichiers au format xlsx). Quelle est la première ligne de la feuille de calcul obtenue dans un tableau à partir de cette liste ?
- Quelle commande lancer pour obtenir le fichier CSV correspondant ?
- Quelle est la deuxième ligne du fichier CSV correspondant ?
- Quelle valeur trouve t-on à la cellule C8 de la feuille correspondante ?
- Par quelle commande obtient-on cette valeur ?
- Une erreur de saisie a lieu : MV joue à worms en fait. Quelle commande permet de modifier le fichier correpondant du tableur ?

### 7. Ajouter une ligne ou une colonne

On dispose de la table suivante au format CSV, dans le repertoire courant sous le nom ***'./Groupe1.csv'***

| Prénom   | Math | Anglais | NSI  |
| -------- | ---- | ------- | ---- |
| Joey     | 16   | 17      | 18   |
| Chandler | 19   | 15      | 17   |
| Ross     | 14   | 19      | 13   |

- Comment obtenir la liste de dictionnaires correspondante en utilisant une fonction déjà vue ?
- Ajouter les notes de l'élève Rachel qui a eu 17 en Maths, 18 en NSI et 19 en anglais.
- On voudrait ajouter une colonne contenant les moyennes de chaque élève afin d'obtenir le tableau suivant :

| Prénom   | Math | Anglais | NSI  | Moyenne |
| -------- | ---- | ------- | ---- | ------- |
| Joey     | 16   | 17      | 18   | 17      |
| Chandler | 19   | 15      | 17   | 17      |
| Ross     | 14   | 19      | 13   | 15,3    |
| Rachel   | 17   | 19      | 18   | 18      |

On doit envoyer une nouvelle table qui ne modifie pas la table d'origine. Pour effectuer une copie d'une liste d'objets complexes (ici une liste de dictionnaires), on peut utiliser la fonction *deepcopy* de la bibliothèque coup. La fonction à créer pourra donc avoir la structure suivante qu'il faudra compléter :

```python
from copy import deepcopy
def ajouter_moyenne(table):
  nvelle_table = deepcopy(table)
  pass

	return nvelle_table
```

Pour obtenir l'affichage d'un nombre flottant arrondi à 2 chiffres derrière la virgule, on peut utiliser la méthode *format* 

Par exemple :

```python
>> '{:.2f}'.format(314/100) #indique un flottant avec 2 chiffres après la virgule
'3,14'
```

Ajouter une ligne qui contient les moyennes par matières.

Cela devrait donner un tableau du genre :

| Prénom   | Math | Anglais | NSI  |
| -------- | ---- | ------- | ---- |
| Joey     | 16   | 17      | 18   |
| Chandler | 19   | 15      | 17   |
| Ross     | 14   | 19      | 13   |
| Rachel   | 17   | 19      | 18   |
| Moyenne  | 16,5 | 17,5    | 16,5 |



### 8. Selectionner, trier, joindre

On dispose de la table Hero suivante

| NumHero | NomHero   | VIlleHero |
| ------- | --------- | --------- |
| 0       | Sangoku   | Kyoto     |
| 1       | Naruto    | Konoha    |
| 2       | Luffy     | Fuchsia   |
| 3       | Ryo Saeba | Tokyo     |
| 4       | Saitama   | VIlle Z   |
| 5       | Onizuka   | Tokyo     |

Ainsi que celle- ci :

| NumHero | NomHero   | Arme              |
| ------- | --------- | ----------------- |
| 0       | Sangoku   | Ki                |
| 1       | Naruto    | Chakra            |
| 2       | Luffy     | Corps             |
| 3       | Ryo Saeba | Magnum            |
| 4       | Saitama   | Point             |
| 5       | Onizuka   | Tout est une arme |



- Renvoyer HeroTokyo, une table extraite de Hero ne contenant que les lignes dont l'attribut VilleHero vaut "Tokyo"

- Renvoyer HeroAlpha, une table extraite de Hero triée selon l'ordre alphabétique du nom des héros.

- Renvoyer HeroComplet, une table contenant le nom, la ville ainsi que l'arme favorite des héros.

- Renvoyer HeroVille, la table contenant le numéro ainsi que la ville des héros.

- Renvoyer HeroImpair, la table contenant le nom et la ville des hero ne venant pas de Tokyo, et dont le numéro est impair.

  

  

----------

Auteur : Florian Mathieu

Licence CC BY NC

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Licence Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a> <br />Ce cours est mis à disposition selon les termes de la <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Licence Creative Commons Attribution - Pas d’Utilisation Commerciale - Partage dans les Mêmes Conditions 4.0 International</a>.

