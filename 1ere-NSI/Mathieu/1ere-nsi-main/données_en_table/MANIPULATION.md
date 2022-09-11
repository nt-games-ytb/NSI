## Operation sur les tables



> Une fois que l'on dispose de données en table, nous pouvons alors manipuler ces données et effectuer des recherches ou des tris.

### Le programme 

![bo_2](assets/bo_2.png)



### Interrogation de table

Il arrive fréquemment que l'on souhaite accéder à différentes informations contenues dans une table de données, selon différents critères.

On suppose que la table en question est une *liste de dictionnaires* - comme vu précédemment - et que cette table sera appelée ***table*** dans la suite de ce cours.

Chaque ligne est donc un dictionnaire et chaque clé correspondra au nom d'une colonne.

✏ *Avant de commencer* ✏

> Pour comparer et vérifier différents critères, nous utiliserons les **opérateurs booléns habituels**
>
> Nous aurons donc <, >, <=, >=, ==, !=, in, not, and, or, is... 

*Quand on interroge une table, on en construit une nouvelle contenant uniquement les lignes satisfaisant une condition donnée sous la forme d'une **fonction booléenne***.

#### Selection de lignes

Pour selectionner des lignes, on peut simplifier l'instruction à :

```python
[ligne for ligne in table if (condition)]
```

Cette instruction va donc générer une liste de dictionnaires verifiant la condition.



#### Selection de colonnes

Selectionner certaines colonnes revient à selectionner certaines clés dans les dictionnaires.

L'instruction ressemblera donc à :

```python
[{clé:ligne[clé] for clé in ligne if (condition sur clé)} for ligne in table]
```



--------------

### Exemples 

Suivant le tableau vu précédemment

| Prénom       | DS1  | DS2  | Projet |
| ------------ | ---- | ---- | ------ |
| Michelangelo | 12   | 14   | B      |
| Leonardo     | 15   | 16   | A      |
| Raphael      | 10   | 12   | C      |
| Donatello    | 13   | 15   | B      |

On peut écrire une fonction qui va selectionner les personnes selon un critère précis :

```python
def select(table, critere):
  def test(ligne):
    return eval(critere)
  return [ligne for ligne in table if test(ligne)] 
```

On peut donc tester cela en selctionnant les élèves ayant obtenu plus de 15 au DS n°2 :

- la fonction *eval* permet d'évaluer l'expression contenue dans la cellule *ligne* sous forme d'une chaine de caractères dans un entier.
- il est necessaire de bien le préciser dans l'appel de la fonction *select*

```python
>> select(table, "eval(ligne['DS2']) > 15")
```

Quel est le résultat obtenu ?

----

Quand on selectionne une ou plusieurs colonnes - attributs - d'une table, on appelle cela une ***projection***.
On va donc recréer une table qui ne contiendra que les attributs selectionnés :

```python
def projection (table, liste_attributs):
  return [{clé:ligne[clé] for clé in ligne if clé in liste_attributs} for ligne in table]
```

Admettons que l'on souhaite ne retenir uniquement que les groupes de projet ainsi que les prénoms des élèves.

Afin de faire la recherche, on peut écrire l'instruction suivante:

```python
projection (Notes, ['Prénom', 'Projet'])
```

-------

### Manipulation de tables

#### Tri de table

On peut trier une liste avec la fonction ***sorted*** qui possède un argument ***key*** précisant le critère de tri et un argument ***reverse***, un booléen qui permet de choisir un tri croissant (par défaut ) ou décroissant (en précisant reverse = True).

On peut donc créer une fonction *tri* qui va trier n'importer quelle table en donnant l'attribut choisir pour le tri et en précisant si l'on veut obtenir le tri dans l'ordre décroissant.

```python
def tri (table, attribut, decroit = False):
  def critere (ligne):
    return ligne[attribut]
  return sorted(table, key = critere, reverse =decroit)
```

Exemple : Pour trier dans l'ordre décroissant la table Notes selon les notes du DS n°1, on peut écrire :

```python
>> tri (Notes, 'DS1', True)
```

Quel est le résultat affiché ?



---------

Auteur : Florian Mathieu

Licence CC BY NC

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Licence Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a> <br />Ce cours est mis à disposition selon les termes de la <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Licence Creative Commons Attribution - Pas d’Utilisation Commerciale - Partage dans les Mêmes Conditions 4.0 International</a>.

