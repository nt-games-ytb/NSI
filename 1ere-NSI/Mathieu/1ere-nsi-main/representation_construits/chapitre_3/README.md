# Structures imbriquées et compréhensions

> Il est possible de combiner listes, tuples, et dictionnaires. Avec la syntaxe des compréhensions, l'écriture des listes et dictionnaires semble plus élègante.

--------

## Les structures imbriquées

On peut imbriquer des listes, des tuples et des dictionnaires. Par contre, les clés de dictionnaire ne peuvent pas muter.

De ce fait, nous pouvons construire des listes de listes, des listes de tuples, des listes de dictionnaires, des tuples de listes, des dictionnaires de tuples...

```python
lst = [(4,5), (-1, 0), (2.5, 1)]
len (lst)
lst[1]
```

Ici, on crée une liste de trois tuples.

Que peuvent représenter ces trois tuples ?

On peut vérifier qu'il s'agut bien d'un tuple :

```python
t = lst[1]
type(t)
```

On peut également accéder directement à l'abscisse ou à l'ordonnée d'un point :

```python
lst[2][1]
```

Ici, on accède donc à la première valeur du tuple n°2.

--------

## Parcours

Soit une liste de dictionnaires

```python
persos = [{"prenom" : "Bilbo", "nom" : "Baggins", "age" : 111},
        {"prenom" : "Frodo", "nom": "Baggins", "age" : 33},
         {"prenom" : "Sam", "nom": "Gamgee", "age" : 21}]
```

On peut parcourir cette liste en séparant chaque dictionnaire :

```python
for p in persos:
  print ("----------")
  for k, v in p.items():
    print (k, ' : ', v)
```

Que fait la première boucle ?

La seconde ?

--------------------

## Les compréhensions

> La notation en compréhension permet de créer une liste ou un dictionnaire sans en lister les élèments de manière explicite.

Par exemple, pour créer une liste comportant les entiers de 2 à 10 inclus :

```python
[i for i in range (2, 11)]
```

On peut aussi appliquer des fonctions à chaque élément :

```python
[i ** 2 for i in range (2, 11)]
```

Enfin, il est possible d'appliquer des conditions dans votre déclaration de structures:

```python
[i ** 2 for i in range (2, 51) if (i ** 2) % 10 == 9]
```

Que fait cette instruction ?

Pour les dictionnaires : la syntaxe est la même, il faut juste préciser la clé et la valeur de chaque élèment :

```python
{k: k ** 3 for k in range (2, 11)}
```

Cela va créer un dictionnaire donc chaque clé sera un nombre entre 2 et 11 non compris, et où la valeur de chaque clé sera le cube de la clé associée.



