# Type Booléen en Python

## Valeur et Type

En Python, les booléens sont `True` et `False`, ils sont du type `bool`

```python
>>> True
True
>>> print(type(True))
<class 'bool'>
>>> False
False
>>> print(type(False))
<class 'bool'>
```

## Comparaison

Les opérateurs de comparaison courants sont identiques à ceux des mathématiques mais ATTENTION, il ne faut pas confondre l’égalité et l’affectation

Python

```python
>>> variable = 5    # une affectation
>>> 5 == 8          # une égalité (qui est fausse)
False
```

**Le résultat d’une comparaison est toujours un booléen**

## Comparaisons des nombres

| Comparaison       | Symbole | Exemple       | Résultat |
| ----------------- | ------- | ------------- | -------- |
| Égalité           | `==`    | `1 + 2 == 3`  | `True`   |
| Différence        | `!=`    | `1 + 2 != 3`  | `False`  |
| Supérieur         | `>`     | `4 > 3`       | `True`   |
| Inférieur         | `<`     | `2.2 < 2 * 3` | `True`   |
| Supérieur ou égal | `>=`    | `5 >= 6`      | `False`  |
| Inférieur ou égal | `<=`    | `8 <= 3`      | `False`  |

## Appartenance à une structure

On peut tester qu’un élément appartient à une structure avec le mot clé `in`

```python
>>> "a"		in "bonjour"        # False
False
>>> "bon"	in "bonjour"        # True
True
>>> 1     in [2, 3, 4]        # False
False
```

# Opérations sur les booléens

Les opérateurs sur les booléens sont de deux types :

- opérateur unaire : prend *un* booléen et en renvoie *un*.
- opérateur binaire : prend *deux* booléens et en renvoie *un*.

## Opérateur unaire : la négation

### La négation: `not`

C’est le seul opérateur *unaire*, il donne le contraire de ce qu’on lui passe.

```python
>>> not True    # s'évalue à False
False
>>> not False   # s'évalue à True
True
```

## Opérateur binaire : le OU, noté `or`

**Il est vrai si l’un des deux booléens est vrai.**

```python
>>> False or False
False
>>> False or True
True
>>> True or False
True
>>> True or True
True
```

## Opérateur binaire : le ET, noté `and`

**Il est vrai si les deux booléens sont vrais.**

```python
>>> False and False
False
>>> False and True
False
>>> True and False
False
>>> True and True
True
```

## Opérateur binaire : le XOR noté `^`

**Il est vrai si EXACTEMENT un des deux booléens est vrai**

```python
>>> False ^ False
False
>>> False ^ True
True
>>> True ^ False
True
>>> True ^ True
False
```

## Python et les booléens

Python permet de comparer n’importe quoi à un booleen.

Par exemple, une chaîne de caractère vide est évaluée à `False`.`

```python
>>> bool(1)
True
>>> bool(0)
False
>>> bool("")
False
>>> bool("abc")
True
>>> bool([])
False
>>> bool([1, 2])
True
```

- 0 est faux, les autres entiers sont vrais,
- une structure vide est fausse, les autres sont vraies.

## Complément : `None` et l’identité `is`

Python propose la valeur `None` (rien) qui est fréquement utilisé pour représenter l’absence d’une valeur.

Étant le seul objet du type `NoneType`, on peut tester son *identité* avec `is` :

```python
>>> 1 is None
False
>>> "abc" is None
False
>>> None is None
True
>>> a = 5
>>> a is None
False
```

On verra plus tard qu’une _fonction_  qui ne se termine par `return ...` renvoie néanmoins `None`.