# Exercices : Représentation des nombres naturels



## Manipulation

__Question 1 :__ Écrire une fonction `est_valide(binaire)` qui retourne :

* **True** si le nombre est valide 
* **False** si le nombre est invalide. 
Le paramètre de la fonction sera une chaîne de caractères représentant un nombre écrit en base 2.

``` python
>>> est_valide("100010101")
True
>>> est_valide("1010401034")
False
```



__Question 2 :__ Écrire une fonction ``est_pair(binaire)`` qui retourne :

* **True** si le nombre passé en paramètre est pair  
* **False** si le nombre passé en paramètre est impair. 
Le paramètre de la fonction sera une chaîne de caractères représentant un nombre écrit en base 2.

```python
>>> est_paire('1001')
False
>>> est_paire('1010')
True
```



## Conversion Binaire - Décimal

__Question 3 :__ Écrire une fonction ``deux_puissance(rang)`` qui retourne la puissance de 2 associée au rang passé en paramètre. Vous n'utiliserez pas les fonctions Python déjà existantes.

``` python
>>> deux_puissance(0)
1
>>> deux_puissance(1)
2
>>> deux_puissance(2)
4
```



__Question 4 :__ A l'aide des fonctions précédentes, écrire une fonction ``binaire_en_decimal(binaire)`` qui retourne la valeur décimale du nombre passé en paramètre. Le paramètre sera une chaîne de caractères représentant un nombre binaire. On vérifiera que ce nombre binaire est valide.

``` python
>>> binaire_en_decimal("1")
1
>>> binaire_en_decimal("1010")
10
>>> binaire_en_decimal("1001")
9
```



## Conversion Décimal - Binaire

__Question 5 :__ Écrire une fonction ``division_euclidienne(nombre, diviseur)`` qui retourne le quotient et le reste obtenu lorsque l'on divise le paramètre *nombre* par le paramètre *diviseur*.

``` python 
>>> division_euclidienne(6,3)
(2,0)
>>> division_euclidienne(10,4)
(2,2)
>>> reste(6, 0)
None
```



__Question 6 :__ A l'aide de l'algorithme de la division euclidienne et des fonctions précédentes, écrire une fonction ``decimal_en_binaire(*decimal*)`` qui retourne une chaîne de caractères correspondant à la représentation binaire du nombre passé en paramètre.


``` python
>>> decimal_en_binaire(16)
"10000"
>>> decimal_en_binaire(31)
"11111"
```



## Conversion Décimal - Hexadécimal

__Question 7 :__ Écrire une fonction ``symbole_hexa(decimal)`` qui retourne le symbole correspondant au paramètre dans la base 16.

```python
>>> symbole_hexa(1)
"1"
>>> symbole_hexa(10)
"A"
```



__Question 8 :__ En s'inspirant des questions précédentes, écrire une fonction ``decimal_en_hexa(decimal)`` qui retourne une chaîne de caractères correspondant à la représentation en base 16 du nombre passé en paramètre.

``` python
>>> decimal_en_hexa(21)
"15"
>>> decimal_en_hexa(2019)
"7E3"
```



## Conversion Hexadécimal - Décimal

__Question 9 :__ écrire une fonction ``hexa_en_decimal(hexa)`` qui retourne le nombre correspondant à la représentation en base 10 du nombre passé en paramètre.

```python
>>> hexa_en_decimal("A")
10
>>> decimal_en_hexa("E10F")
57615
```



## Conversion en base $$n$$

__Question 10 :__ En s'inspirant des fonctions 8 et 10, écrire une fonction ``decimal_en_base_n(decimal, base)`` qui retourne une chaîne de caractères correspondant à la représentation en base *n* du nombre passé en paramètre.

```python
>>> decimal_en_base_n(10,2)
"1010"
>>> decimal_en_base_n(10,16)
"A"
>>> decimal_en_base_n(10,5)
"20"
```
