# Représentation des entiers relatifs

## Attendus

| Contenus | Capacités attendues |
| :--: | :-- |
| Représentation binaire d’un entier relatif | Évaluer le nombre de bits nécessaires à l’écriture en base 2 d’un entier, de la somme ou du produit de deux nombres entiers. <br />Utiliser le complément à 2 |

## Contexte

Pour comprendre le fonctionnement du binaire, nous allons nous intéresser dans le un premier temps à la représentation des entiers positifs en base 10.
Quelque soit la base utilisée, le fonctionnement est identique et les méthodes de conversion sont similaires.

## Pré-requis

### La valeur absolue d'un nombre

La valeur absolue d'un nombre réel est sa valeur numérique sans tenir compte de son signe. Elle est notée $`|n|`$.

- Si $`n > 0`$, alors $`|n| = n`$
- Si $`n < 0`$, alors $`|n| = `$ opposé de $`n`$

###  Les bits significatifs

### L'addition binaire

Les opérations ci dessous manipulent des nombres représentés en binaire, codés sur un (1) bit.

```math
\begin{align*}
0 + 0 &= 0 \\
1 + 0 &= 1 \\
0 + 1 &= 1 \\
1 + 1 &= 0 \rightarrow \textit{Mais on reporte la retenue sur le bit de poids supérieur}
\end{align*}
```

### La soustraction

Les opérations ci dessous manipulent des nombres représentés en binaire, codés sur quatre (4) bit.

```math
\begin{align*}
0110 - 0011 &= 0011 \\
1011 - 10 &= 1001 \\
10 - 101 &= ? \\
\end{align*}
```

**_À votre avis, que donne cette dernière opération ?_**

## 1. La représentation binaire signée

La première méthode utilisée pour représenter des entiers négatifs est de réserver un bit qui déterminera le signe. Il restera donc p - 1 bits pour la représentation de la valeur absolue.

Le bit de signe choisi est le bit le poids fort. Par convention, on définira : ·

- $`1`$ pour représenter un nombre négatif
- $`0`$ pour représenter un nombre positif

Avant de représenter un entier, il faut aussi définir le nombre de bits qui seront utilisés, souvent 4, 8, 16, 32 ou 64 bits.

Prenons un exemple avec l'entier $`5`$ sur 8 bits :

```math
\begin{align*}
5_{10} & = 0000\ 0101_2 \\
-5_{10} & = 1000\ 0101_{2}
\end{align*}
```

Cependant cette méthode possède un inconvénient majeur :

Les opérations "classiques" avec 2 nombres binaires ne fonctionnent plus ! C'est pour ces raisons que nous allons utiliser une nouvelle méthode : **le complément à deux**.

Par ailleurs, on peut observer qu'il existe dorénavant deux manières de notation du nombre zéro (0) :

- $`0000\ 0000 = +0`$
- $`1000\ 0000 = -0`$

## 2. Le complément à 2

Le **complément à 2** est la méthode de représentation d'un entier négatif.

Cette méthode se décompose en quatre (4) étapes :

1. Représenter la valeur absolue de l'entier relatif sur $`p`$ bits
2. Inverser tous les bits (les 1 deviennent des 0 et vice versa)
3. Ajouter un (1) au nombre obtenu à l'étape précédente
4. Le résultat de cette dernière opération est donc la représentation sur $`p`$ bits de l'entier relatif.

**Travail à faire**

> Calculer l'entier -5 en appliquant le complément à 2 sur 8 bits.

Vérifions que la représentation par le complément à 2 satisfait la règle vue précédemment.

Exemple avec les entiers 13 et -13 :

```math
\begin{align}
&  & \: 0 \: 0 \: 0 \: 0 \: 1 \: 1 \: 0 \: 1 \\
+ &  & \: 1 \: 1 \: 1 \: 1 \: 0 \: 0 \: 1 \: 1 \\
\hline
= &  & 1 \: 0 \: 0 \: 0 \: 0 \: 0 \: 0 \: 0 \: 0
\end{align}
```

Dans l'opération ci-dessus, nous avons un 1 pour le 9ième bit, mais comme notre représentation se limite à 8 bits, il nous reste bien $`(00000000)_2`$.

> 1. Représenter sur 8 bits l'entier 4 puis représenter, toujours sur 8 bits, l'entier -5.
> 2. Additionner ces 2 nombres, vérifier que vous obtenez bien -1.

**Question pour vous**

- Quel est le plus petit entier négatif que l'on peut représenter sur huit (8) bits ?
- Et quel est le le plus grand ?

# ✎ Remarque ✎ :

Plus généralement, nous pouvons dire que pour une représentation sur $`n`$ bits, il sera possible de coder des valeurs comprises entre $`-2^{n-1}`$ et $`+2^{n-1} - 1`$ .

Sachant que dans le langage C, les entiers signés sont codés sur 32 bits, dont un (1) pour le signe, quelles sont les valeurs minimale et maximale des entiers que l'on peut représenter ?

En Python, la taille des entiers est arbitraire (donc non fixe), ainsi les valeurs minimale et maximale des entiers ne dépend que de la quantité de mémoire disponible sur votre machine.

Néanmoins, on dispose de la bibliothèque _numpy_ qui permet de forcer une représentation sur 8 bits, par exemple, à l'aide de la fonction *int8*

