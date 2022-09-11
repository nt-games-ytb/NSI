# Préliminaire

## Méthode `split` sur les chaînes de caractères

1. Supposons que la variable ``s`` a pour valeur la chaîne ``"la méthode split est parfois bien utile"``. Quelles sont les réponses
   fournies par Python pour les expressions suivantes ?

   * ``s.split(' ')``
   * ``s.split('e')``
   * ``s.split('é')``
   * ``s.split()``
   * ``s.split('')``
   * ``s.split('split')``
   
2. Déduisez-en une description précise de ce que fait la méthode ``split``.

## Méthode `join` sur les chaînes de caractères

3. Supposons que la variable ``l``  est définie par ``l = s.split()`` où ``s`` est la chaîne  ``"la méthode split est parfois bien utile"``. Quelles sont les réponses
   fournies par Python pour les expressions suivantes ?

   * ``"".join(l)``
   * ``" ".join(l)``
   * ``";".join(l)``
   * ``" tralala ".join(l)``
   * ``print ("\n".join(l))``
   * ``"".join(s)``
   * ``"!".join(s)``    
   * ``"".join()``
   * ``"".join([])``
   * ``"".join([1,2])``
     
4. Déduisez-en une description précise de ce que fait la méthode ``join``.


## Méthode `sort` sur les listes

La méthode ``sort`` sur les listes est une méthode qui permet de trier les éléments de la liste sur laquelle elle s'applique. Trier les éléments d'une liste c'est les ranger dans l'ordre.
Cette méthode de tri modifie la liste.


```python
   
   >>> l = [3, 1, 4, 1, 5]
   >>> l.sort()
   >>> l
   [1, 1, 3, 4, 5]
```

On voit sur cet exemple que la liste ``l`` a été modifiée après application de la méthode ``sort`` :
les nombres sont maintenant rangés dans l'ordre numérique croissant.

5. Appliquez cette méthode sur la liste ``l = list('timoleon')``. Qu'est devenue la liste ``l`` ?
   Même chose avec ``l = list(s)`` où ``s = "Je n'ai jamais joué de flûte."``.

   À votre avis, si ``l = list(s)`` avec ``s`` une chaîne de caractères quelconque, quel est l'ordre
   dans lequel les caractères de ``l`` sont rangés après application de la méthode ``sort`` ?

6. Appliquez cette méthode sur la liste ``l = ['a', 1]``. Expliquez la réponse.

## Une fonction `sort` sur les chaînes de caractères

Il n'y a pas de méthode ``sort`` pour les chaînes de caractères.

7. Programmez une fonction nommée ``sort̀`` qui renvoie une chaîne de caractères contenant tous
   les caractères de la chaîne passée en paramètre triés dans l'ordre lexicographique.

   ```python
   >>> sort('capes nsi')
   ' aceinpss'
   >>> sort('')
   ''
   ```
   
   Pour cela, vous pourrez utiliser avec profit la fonction de conversion ``list``,
   la méthode ``sort`` des listes et la méthode ``join`` des chaînes.
   
   
# Anagrammes

Selon le dictionnaire « Le Petit Robert », le mot anagramme a pour définition : mot obtenu par transposition des lettres d’un autre mot.

Une anagramme est donc un mot constitué des mêmes lettres qu’un autre en respectant leurs nombres d’occurrences. Par exemple orange est une anagramme du mot organe, ainsi que onagre.

Dans cette partie nous étendons la notion d’anagrammes à toute chaîne de caractères : deux chaînes de caractères sont dites anagrammatiques si elles contiennent les mêmes caractères en mêmes nombres. En particulier toute chaîne de caractère est une anagramme d’elle-même.

Vous allez écrire plusieurs versions d’un prédicat nommé `sont_anagrammes` qui prend deux chaînes de caractères et renvoie le booléen `True` si ces deux chaînes sont anagrammatiques, et le booléen `False` dans le cas contraire.



1. Réalisez une première version du prédicat `sont_anagrammes` en utilisant la fonction `sort` que vous avez réalisée dans le préliminaire.

À chaque chaîne de caractères on peut associer une table donnant le nombre d'occurrences de chacun de ses caractères. Par exemple, voici la table pour la chaîne `errance` :

|lettre | nbre occ
|--|---
|a | 1
|c | 1
|e | 2
|n | 1
|r | 2

Une telle table peut être représentée en Python par un dictionnaire. Sur notre exemple on aurait le dictionnaire

```python
{'a':1, 'c':1, 'e':2, 'n':1, 'r':2}
```

Deux mots sont anagrammes l'un de l'autre si est seulement s'ils ont la même table d'occurrences.

2. Réalisez une seconde version de ce prédicat qui construit un tel dictionnaire pour chacune des deux chaînes et les compare.

# Trouver des anagrammes
Il s'agit maintenant de trouver dans un lexique donné l'ensemble des anagrammes d'un mot donné.

Vous allez réaliser deux versions d'une fonction nommée `anagrammes` qui donne la liste des anagrammes trouvées dans le lexique d'une chaîne de caractères passée en paramètre.

Le lexique que vous allez utiliser est la liste de mots `LISTE_MOTS` définie dans le fichier [liste_7776_mots.py](../phrases_de_passe/liste_7776_mots.py).


1. Réalisez une première version de la fonction `anagrammes` qui parcourt le lexique entier et utilise l'une ou l'autre des deux versions de la fonction `sont_anagrammes` réalisée précédemment.


La deuxième méthode consiste à chercher la liste des anagrammes dans un dictionnaire d'anagrammes. Les clés d'un tel dictionnaire sont des chaînes de caractères dont les caractères sont rangés dans l'ordre alphabétique croissant, et les valeurs associées sont des listes de mots du lexique anagrammes de la clé. Voici quelques exemples d'association clé/valeur qu'on peut obtenir avec le lexique proposé ci-dessus :

```python
 'aceenrr' : ['errance', 'carener', 'cernera']
 'bemort' : ['tomber', 'trombe']
 'floru' : ['fluor']
 ...
```

Si on dispose d'un tel dictionnaire, lorsqu'on veut chercher la liste des anagrammes d'un mot donné, il suffit de calculer la clé correspondante à ce mot et de chercher la valeur associée à cette clé dans le dictionnaire. Si la clé n'est pas présente dans le dictionnaire, cela signifie que le lexique ne contient aucune anagramme du mot.

2. Construisez ce dictionnaire d'anagrammes.


3. Réalisez la seconde version de la fonction `anagrammes` en utilisant le dictionnaire que vous avez construit.
