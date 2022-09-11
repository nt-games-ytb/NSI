# Exercices : Représentation des nombres relatifs



## Complément à deux

__Question 1 :__ Écrire une fonction ``valeur_absolue(nombre)`` qui retourne la valeur absolue du nombre passé en paramètre.

```python
>>> valeur_absolue(7)
7
>>> valeur_absolue(-6)
6
```



__Question 2 :__ Écrire une fonction ``inverse(binaire)`` qui retourne une nouvelle chaîne de caractères qui correspond à l'inverse de la chaîne passée en paramètre. 

Le paramètre de la fonction sera une chaîne de caractères représentant un nombre écrit en base 2. 

``` python
>>> inverse("1010")
"0101"
>>> inverse("10110011")
"01001100"
```



__Question 12 :__ Écrire une fonction ``addition_binaire(binaire1,binaire2)`` qui additionne et retourne le résultat des 2 nombres représentés en base 2. Vous vous aiderez de la table d'addition vu dans le cours.

```python
>>> addition_binaire("1001","0001")
"1010"
>>> addition_binaire("0001","0001")
"0010"
```



__Question 13 :__ En utilisant les fonctions précédentes, écrire une fonction ``complement_a_2(decimal, nombre_bit)`` qui retourne la représentation en complément à 2 du nombre donné en paramètre.

``` python
>>> complement_a_deux(-12, 8)
"11110100"
>>>> complement_a_deux(7,8)
"00000111"
```


__Question 14 :__ En utilisant le principe inverse, écrire une fonction ``complement_a_2_vers_decimal(binaire)`` qui retourne la valeur du nombre représenté en complément à 2 passé en paramètre. Vous aurez besoin d'écrire une fonction qui effectue la soustraction de 2 nombres binaires.

``` python
>>> complement_a_2_vers_decimal("1111")
-1
>>>> complement_a_2_vers_decimal('0111")
7
```
