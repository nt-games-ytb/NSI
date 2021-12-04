## Exercice

### Itérer sur les éléments d'un dictionnaire

Au zoo de Beauval, il y a 5 éléphants d'Asie, 17 écureuils d'Asie, 7 hippopotames d'Afrique...

On représente cet inventaire à l'aide d'un dictionnaire, de la façon suivante:

```python
zoo_Beauval = {
'elephant' : ('Asie', 5),
'ecureuil' : ('Asie', 17),
'panda' : ('Asie', 2),
'hippopotame' : ('Afrique', 7),
'girafe' : ('Afrique', 4)
}
```

De la même manière, on peut représenter le zoo de La Flèche :

```python
zoo_LaFleche = {
  'ours' : ('Europe', 4),
  'tigre' : ('Asie', 7),
  'girafe' : ('Afrique', 11),
  'hippopotame' : ('Afrique', 3)
  }
```



#### Question n°1

On souhaite créer une fonction *plus_grand_nombre* ( ) qui prend un zoo en paramètre et renvoie le nom de l'animal le plus présent au sein du zoo.

Exemples :

```python
>> plus_grand_nombre(zoo_LaFleche)
>> 'girafe'
```

```python
>> plus_grand_nombre(zoo_Beauval)
>> 'ecureuil'
```

On aura besoin d'une boucle utilisant 

```python
for (cle, valeur) in dico.items()
```

À votre avis, pourquoi ?



Écrire la fonction :

```python
def plus_grand_nombre(zoo):
  """
  :param: zoo est un dictionnaire dont les clés sont des str (noms des animaux) 
  :param: les valeurs de ces clés sont des tuples (origine, nombre) avec origine : str et nombre : int
  :return: le nom de l'animal le plus représenté dans le zoo, sous la forme d'une chaîne de caractères
  """
  
  pass
```



#### Question n°2

On souhaite se doter d'une fonction *nombre_total* ( ) qui prend un zoo ainsi que le nom d'un continent en paramètre, et qui renvoie le nombre d'animaux originaires de ce continent dans le zoo.

Exemples :

```python
>> nombre_total(zoo_LaFleche, 'Afrique')
>> 14
```

```python
>> nombre_total(zoo_Beauval, 'Asie')
>> 24
```

On utilisera une boucle 

```python
for valeur in dico.values()
```

Pourquoi ?



Écrire la fonction :

```python
def nombre_total(zoo, continent):
  """
  :param: zoo est un dictionnaire dont les clés sont des chaines, correspondantes aux noms des animaux
  :param: et dont les valeurs sont des tuples (origine, nombre), origine étant une chaine, nombre un int
  :param: continent est une chaine comprenant le nom d'un continent d'où sont originaires les animaux
  :return: la fonction renvoie le nombre d'animaux originaires de 'continent' dans ce zoo
  """
  
  pass
```



#### Question n°3

Enfin, on souhaite écrire une fonction nombre, qui prendun zoo ainsi qu'un nom d'animal en paramètre, et qui renvoie le nombre de représentants de cet animal dans le zoo.

Exemples :

````python
>> nombre(zoo_LaFleche, 'panda')
>> 0
````

```python
>> nombre(zoo_Beauval, 'panda')
>> 2
```



Quel type de boucle va t-on utiliser ici ?

Écrire la fonction

```python
def nombre(zoo, animal):
  """
  :param: zoo est un dictionnaire dont les clés sont des chaines, correspondantes aux noms des animaux
  :param: et dont les valeurs sont des tuples (origine, nombre), origine étant une chaine, nombre un int
  :param: animal est une chaine comprenant le nom d'un animal
  :return: la fonction renvoie le nombre de représentants du paramètre 'animal' dans ce zoo
  """
  
  pass
```

