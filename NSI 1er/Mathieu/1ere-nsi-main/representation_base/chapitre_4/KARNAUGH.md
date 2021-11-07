# Les tableaux de Karnaugh 

------

## Introduction

La réduction, pour une même expression, du nombre d'*opérateur*s ***et / ou*** du nombre de *variables*, conduit à une écriture simplifiée de cette expression.

Il existe un grand nombre de méthodes de simplification d'expression booléenne, parmi lesquelles ont peut distinguer :

- La simplification par **Tableau de Karnaugh**. On fait cela en quelques étapes :
  - On construit un tableau de la fonction à simplifier
  - On recherche les cases adjacentes qui ont pour valeur 1 
  - On regroupe ces cases par puissance de 2, en paquets les plus gros possibles.

Cette méthode s'avère la plus redoutable.

---------

## Construction du tableau de Karnaugh

- Tableau à 3 variables:
  - En haut, on regroupe deux variables ensemble (A B)
  - À gauche, on indique la troisième (C)
  - S = sortie							

| S    | 00   | 01   | 11   | 10   |
| ---- | ---- | ---- | ---- | ---- |
| 0    |      |      |      |      |
| 1    |      |      |      |      |



- Tableau à 4 variables :
  - Deux variables en haut ( A B)
  - Deux variables à gauche ( C D)

| U    | 00   | 01   | 11   | 10   |
| ---- | ---- | ---- | ---- | ---- |
| 00   |      |      |      |      |
| 01   |      |      |      |      |
| 11   |      |      |      |      |
| 10   |      |      |      |      |



-----------

## Exemples

*Simplification de l'équation logique suivante :* 

```math
S = \overline a b \overline c  \overline d + abcd + a \overline b c d + ab \overline c \overline d
```



| S    | 00   | 01   | 11   | 10   |
| ---- | ---- | ---- | ---- | ---- |
| 00   | 0    | 1    | 1    | 0    |
| 01   | 0    | 0    | 0    | 0    |
| 11   | 0    | 0    | 1    | 1    |
| 10   | 0    | 0    | 0    | 0    |

- On regroupe les 1 collés en haut : a change d'état et est éliminé. Il reste donc :

  ```math
  b \overline c \overline d
  ```

  

- On regroupe les 1 en bas : b change d'état et est éliminé, il reste :

  ```math
  acd
  ```

  

  

On a donc une équation réduite sous forme de polynôme ou canonique en ***OU***

```math
S = acd + b \overline c \overline d
```



-------



| S    | 00   | 01   | 11   | 10   |
| ---- | ---- | ---- | ---- | ---- |
| 00   | 1    | 0    | 0    | 0    |
| 01   | 1    | 0    | 0    | 0    |
| 11   | 1    | 0    | 0    | 0    |
| 10   | 1    | 0    | 0    | 0    |

```math
S = \overline a \overline b
```



-------

| S    | 00   | 01   | 11   | 10   |
| ---- | ---- | ---- | ---- | ---- |
| 00   | 1    | 0    | 0    | 1    |
| 01   | 1    | 0    | 0    | 1    |
| 11   | 1    | 0    | 0    | 1    |
| 10   | 1    | 0    | 0    | 1    |

```math
S = \overline b
```



----------

| S    | 00   | 01   | 11   | 10   |
| ---- | ---- | ---- | ---- | ---- |
| 00   | 1    | 0    | 0    | 1    |
| 01   | 0    | 0    | 0    | 0    |
| 11   | 0    | 0    | 0    | 0    |
| 10   | 1    | 0    | 0    | 1    |

```math
S = \overline b \overline d
```



---------

## Exercices 



**Simplifier à l'aide du tableau du Karnaugh l'équation logique suivante** :

```math
T = \overline a b \overline c \overline d + ab \overline c \overline d + \overline a bc \overline d + abc\overline d + \overline a \overline b  c \overline d + a \overline b c \overline d
```



| T    | 00   | 01   | 11   | 10   |
| ---- | ---- | ---- | ---- | ---- |
| 00   | 0    | 1    | 1    | 0    |
| 01   | 0    | 0    | 0    | 0    |
| 11   | 0    | 0    | 0    | 0    |
| 10   | 1    | 1    | 1    | 1    |

-------------

D'après le tableau de Karnaugh suivant, rechercher l'équation logique réduite :



| U    | 00   | 01   | 11   | 10   |
| ---- | ---- | ---- | ---- | ---- |
| 00   | 1    | 1    | 1    | 1    |
| 01   | 1    | 1    | 1    | 1    |
| 11   | 1    | 1    | 0    | 1    |
| 10   | 1    | 1    | 1    | 1    |

Indice : utiliser le théorème de **DE MORGAN**

```math
\overline U = abcd
```





