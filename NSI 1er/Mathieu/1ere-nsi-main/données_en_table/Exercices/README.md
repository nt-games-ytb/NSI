## Exercices



### 1. Manipulation de fichiers CSV

- Par quoi peut-on représenter un enregistrement en Python ?

- Dans un fichier CSV, quel élément sépare les différents attributs ?

- On dispose d'une table de données *Table* représentée par une liste de dictionnaires. Qu'obtient-on en entrant :

  ```python
  Table[0]
  ```

  

### 2. Opérations sur les tables

On dispose de la table T représentant les notes d'élèves dans trois matières :

| Prénom   | Math | Anglais | NSI  |
| -------- | ---- | ------- | ---- |
| Joey     | 16   | 17      | 18   |
| Chandler | 19   | 15      | 17   |
| Ross     | 14   | 19      | 13   |



- Pour selectionner des colonnes selon un critère donné, laquelle de ces deux fonctions peut-on utiliser ?

```python
def select(table, critère):
  def test(ligne):
    return eval(critère)
 return [ligne for ligne in table if test(ligne)] 
```

```python
def projection(table, liste_attributs):
  return [{clé:ligne[clé] for clé in ligne if clé in liste_attributs} for ligne in table]
```

- La fonction *select* vu au dessus peut-être utilisée comme ceci :

  ```python
  select(T,"'17' in ligne.values()")
  ```

  Que renvoie cet appel de fonction ?



- Soit U la table suivante :

| Prénom   | Âge  | Mail                   |
| -------- | ---- | ---------------------- |
| Joey     | 29   | howyoudoin@friends.com |
| Chandler | 31   | joke@friends.com       |

En réutilisant la fonction fusion suivante:  

```python
from copy import deepcopy
def fusion(table_1, table_2, cle_1, cle_2=None):
  if cle_2 is None:
    cle_2 = cle_1
  table_finale = []
  for ligne_1 in table_1:
    for ligne_2 in table_2:
      if ligne_1[cle_1] == ligne_2[cle_2]:
        ligne_finale = deepcopy(ligne_1)
        for cle in ligne_2:
          if cle != cle_2:
            ligne_finale[cle] = ligne_2[cle]
        table_finale.append(ligne_finale)
  return table_finale      
```

donnez le nombre de  lignes et de colonnes renvoyées par :

```python
fusion(T,U, 'Prénom')
```



### 3. Determiner des fonctions basiques

- Determiner une fonction qui calcule la **cardinalité** d'une table, c'est à dire son nombre de lignes.
- Determiner une fonction qui renvoie la liste des attributs d'une table.



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

  

  
