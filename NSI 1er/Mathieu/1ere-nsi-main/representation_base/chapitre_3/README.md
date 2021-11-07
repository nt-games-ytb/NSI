# Représentation des décimaux : les flottants

## 1. Attendus

| Contenus | Capacités attendues |
| :--: | :-- |
| Représentation approximative des nombres réels : notion de nombre flottant | Calculer sur quelques exemples la représentation de nombres réels : 0.1, 0.25 ou 1/3. |

## 2. Contexte 

Nous avons appris à encoder des nombres entiers naturels, et relatifs, et nous avons vu que les limites physiques des machines imposaient des limites sur l'étendue des valeurs. Par exemple, sur un octet on dispose de $`2^8 = 256`$ valeurs distinctes qui permettent d'encoder:

- des nombres entiers naturels entre 0 et 255.
- des nombres entiers relatifs entre -128 et 127.

Maintenant que nous allons tenter de coder les réels, les limites de notre machine vont encore entraîner des limites sur l'étendue des valeurs, mais également sur la __précision des valeurs__.

### 2.1. À Faire

1. effectuez le calcul $`0.2 + 0.1`$ en Python :

```python
>>> 0.2 + 0.1
???
```

2. testez l'égalité suivante : 

```python
>>> 0.2 + 0.1 == 0.3
???
```

> **Il n'est pas possible de coder un nombre décimal en valeur exacte en base 2**.
>
> **On obtient une approximation du nombre décimal, et non le nombre en lui même.**
>
> **Cette approximation est appelée _nombre en virgule flottante_ et correspond au type _float_ en Python.**

Ainsi, un calcul avec des nombres à virgule ne peut-être qu'__approximatif__. Cependant plus on augmente la taille du registre du processeur et plus nous pourrons représenter de valeurs, et plus nos calculs gagneront en précision.

## 3. Codage de la virgule

Il existe deux façons de coder les nombres réels, en virgule fixe ou virgule flottante.

### 3.1. Virgule fixe

Le codage en __virgule fixe__ consiste à garder __un nombre fixe de chiffes après la virgule__.

Pour une représentation sur $`n`$ bits, on fixe $`e`$ bits pour la partie entière et $`v`$ bits pour la partie décimale où $`e + v = n`$.

__Exemple__ : Sur un octet, on peut utiliser 4 bits pour la partie entière et 4 bits pour la partie décimale.

Ainsi, `0101 1011` a pour valeur : $`2^2 +  2^0 + 2^{-1} + 2^{-3} + 2^{-4} = 4 + 1 + 0.5 + 0.125 + 0.0625 = 5.6875`$   

C’est extrêmement simple. Cette manière de faire s’appelle virgule fixe, car la position de la virgule est connue d’avance. 

L’inconvénient de cette méthode est que, pour un nombre avec peu de chiffres après la virgule, on perd un espace de stockage significatif. Si le nombre en question est `0110 1000`, on perd trois bits “inutilement”.

#### 3.1.1. À Faire

Représenter les valeurs suivants sur 8 bits, en virgule fixe :

1. 7,75
2. 0,1

### 3.2. Virgule flottante

#### 3.2.1. Notation scientifique

Cette écriture se base sur la notation scientifique des nombres : $`\pm a \times 10^n`$ où $`1 \le a \lt 10`$ et $`n \in \mathbb{Z}^*`$ 

Par exemple :

- 12 s'écrit : $`1,2 \times 10^1`$
- -85 s'écrit : $`-8,5 \times 10^1`$
- 0,0123 s'écrit : $`1,23 \times 10^{-2}`$

Le terme __exposant__ correspond à la puissance de 10, et le terme __mantisse__ correspond à la partie décimale. Ainsi, dans « 1,23 × 10−2 » :

- la mantisse (ou significande) est « 1,23 » ;
- l'exposant est « -2 ».

##### 3.2.1.1. À Faire

Exprimez les nombres suivants en notation scientifique :

- La distance $`d`$ entre la Lune et la Terre est de 384 400km
- Le poids $`p`$ du moustique Tigre est d'environ 0, 000 001 07kg.

#### 3.2.2. Notation scientifique binaire

Un nombre binaire à virgule de quatre chiffres $`n_1n_0,n_{-1}n_{-2}`$ correspond au nombre décimal $`n_1 \times 2^1 + n_0 \times 2^0 + n_{-1} \times 2^{-1} + n_{-2} \times 2^{-2}`$.

On peut ainsi avoir une notation scientifique binaire : $`n_1n_0,n_{-1}n_{-2}`$ en binaire peut se noter $`n_1,n_0n_{-1}n_{-2} \times 2^1`$.

Par exemple : 

- $`11_2 = 1,1_2 \times 2^1`$
- $`0,11_2 = 1,1_2 \times 2^{-1}`$

_N.B : Dans le cas de la notation scientifique binaire, le nombre avant la virgule doit être compris entre $`1_2`$ inclus et $`10_2`$ exclus (c'est-à-dire 2 exclus), c'est-à-dire que sa partie entière est nécessairement 1._

#### 3.2.3. Principe du codage en virgule flottante

Un nombre flottant est formé de trois éléments : la mantisse, l'exposant et le signe. 

$$
\begin{aligned}
s.m \times 2^e
\end{aligned}
$$

![](./assets/virgule_flottante.svg)

- Le bit de poids fort $`s`$ est le bit de __signe__ : si ce bit est à 1, le nombre est négatif, et s’il est à 0, le nombre est positif. 
- Les $`e`$ bits suivants représentent l'__exposant biaisé__ (sauf valeur spéciale),
- Les $`m`$ bits suivants ($`m`$ bits de poids faible) représentent la __mantisse__.

__Exemple__ :

Supposons un nombre flottant codé sur un octet utilisant 1 bit de signe, 3 bits pour l'exposant et 4 bits pour la mantisse: `1 101 1011`

- $`s`$ est le signe représenté par le bit de poids fort. Notre codage représente donc un nombre négatif.
- $`e`$ est l'exposant biaisé, représenté par un entier relatif décalé et non en complément à 2.
  - Ce décalage est de $`2^{|e|-1} - 1`$ ($`|e|`$ représente le nombre de bits utilisé pour coder l'exposant). 
  - L'exposant a pour valeur $`101`$ codé sur 3 bits. Il doit être décalé de $`2^2 - 1 = 3`$. 
  - Ainsi, puisque $`101_2 = 5_{10}`$, l'exposant $`101`$ correspond à un exposant de $`5 - 3 = 2`$.
- $`m`$ est la mantisse, elle représente en binaire uniquement les chiffres après la virgule.
	- Dans notre exemple, la mantisse est $`1011`$,
	- Soit $`m = 1 + 1 \times 2^{-1} + 1 \times 2^{-3} + 1 \times 2^{-4} = 1 + \frac{1}{2} + \frac{1}{8} + \frac{1}{16} = 1,6875`$  

Le code `1 101 1011` sur un octet utilisant 1 bit de signe, 3 bits pour l'exposant et 4 bits pour la mantisse représente donc: $`-1,6875 \times 2^2 = -6,75`$

## 4. La norme IEEE 754

> L'__IEEE 754__ est une norme pour la représentation des nombres à virgule flottante en binaire. Elle est la norme la plus employée actuellement pour le calcul des nombres à virgule flottante dans le domaine informatique.

Cette norme définit notamment 2 formats pour représenter des nombres à virgule flottante:

- _simple précision_ (32 bits : 1 bit de signe, 8 bits d'exposant (-126 à 127), 23 bits de mantisse),

![](./assets/ieee_754_simple.svg)

- _double précision_ (64 bits : 1 bit de signe, 11 bits d'exposant (-1022 à 1023), 52 bits de mantisse)

![](./assets/ieee_754_double.svg)

### 4.1. Valeurs remarquables

Chaque norme défini aussi des valeurs spéciales, par exemple en double précision:

- le zéro positif: +0 = `0 00000000000 0000000000000000000000000000000000000000000000000000`,
- le zéro négatif: -0 = `1 00000000000 0000000000000000000000000000000000000000000000000000`,
- l'infini positif: +∞ = `0 11111111111 0000000000000000000000000000000000000000000000000000`,
- l'infini négatif: +∞ = `1 11111111111 0000000000000000000000000000000000000000000000000000`

### 4.2. Impossibilité de coder tous les nombres réels

Voici l’écriture binaire en format double précision de deux flottants.

| Nombre flottant | Représentation format double précision (mantisse sur 23 bits) |
| :--: | :--: |
| $`2.0^{(1)}`$ | `0 10000000 00000000000000000000000` |
| $`2.000000238418579^{(2)}`$ | `0 10000000 00000000000000000000001` |

Calcul de (1) :

```math
\begin{aligned}
n & = s.m \times 2^e \\
e & = e_{biaisé} - décalage \\
e_{biaisé} & = 10000000_2 = 2^7 \\
décalage & = 2^{8 - 1} - 1 \\
e & = 2^7 - (2^7 - 1) \\
m & = 1 + 0 \\
n & = 1 \times 2^1 = 2.0
\end{aligned}
```

Calcul de (2) :

```math
\begin{aligned}
n & = s.m \times 2^e \\
e & = e_{biaisé} - décalage \\
e_{biaisé} & = 10000000_2 = 2^7 \\
décalage & = 2^{8 - 1} - 1 \\
e & = 2^7 - (2^7 - 1) \\
m & = 1 + 2^{-23} \\
n & = (1 + 2^{-23})\times 2^1 = 2 + 2^{-22} = 2.000000238418579
\end{aligned}
```

On comprend aisément qu’il n’y a pas de flottant entre 2.0 et 2.000000238418579.
Le flottant 2.000000238418579 est donc représenté comme le suivant de 2.0.
La précision possible avec une mantisse sur 23 bits se situe au niveau dernier bit qui vaut
$`2^{-23}`$ . On ne peut pas trouver un flottant compris entre les deux.

### 4.3. Conclusion

Les nombres flottants sont une représentation approximative des nombres réels dans un ordinateur. En particulier, il n’est pas possible de représenter de manière exacte en machine tous les nombres réels. La manipulation de nombres réels par un langage informatique est donc à prendre avec précaution car elle peut engendrer des résultats surprenants, en particulier il ne faut jamais tester l’égalité entre deux flottants.

## 5. Exercices

### 5.1. Exercice

On considère des nombres flottants encodés sur un octet avec dans l'ordre:

- 1 bit de signe,
- 3 bits d'exposant,
- 4 bits de mantisse.

1. Trouver les nombres à virgule représentés par les mots binaires suivant:
	- `0111 1000`
	- `1001 0001`
2. Donner les représentations binaires des nombres flottants suivants:
	- 2,5 (qui est égal à $`1,25 \times 2`$).
	- -1,125.
3. Avec cet encodage à 8 bits:
	- Quel est le plus grand nombre à virgules que l'on peut représenter ?
	- Quel est le plus petit nombre à virgule, donc négatif ?
	- Quel est le plus petit nombre à virgule strictement positif que l'on peut représenter ?

### 5.2. Exercice

1. Quelles sont les valeurs attendues des instructions suivantes ?

  ```python
  >>> # Cas 1
  >>> from math import sqrt
  >>> sqrt(2.0)**2 == 2.00
  ???
  ```

  ```python
  >>> # Cas 2
  >>> 9007199254740992.0 + 1
  ???
  ```

  ```python
  >>> # Cas 3
  >>> 1.2 - 1.0
  ???
  ```

  ```python
  >>> # Cas 4
  >>> 0.5 - 0.2 - 0.2 - 0.1
  ???
  ```


  ```python
  >>> # Cas 5
  >>> 9007199254740992.0 + 1.0 + 1.0
  ???
  ```

  ```python
  >>> # Cas 6
  >>> 1.0 + 1.0 + 9007199254740992.0 
  ???
  ```
2. Copier et exécuter les instructions précédentes et comparer avec les résultats attendus.

### 5.3. Exercice

On considère le programme suivant:

```python
a = 0.0
for loop in range(0,10):
    a = a + 0.1
    print(a)
```

1. Si l'on calculait sur des nombres rationnels exacts, que se passerait-il lors de l'exécution de ce programme ?
2. Écrire ce programme et l'exécuter. Que constate-t-on ?
3. Vérifier avec le convertisseur en ligne que la représentation binaire de 0,1 est `0 01111111011 1001100110011001100110011001100110011001100110011010`.
4. Quel nombre décimal cette représentation désigne-t-elle en réalité Quel nombre décimal cette représentation désigne-t-elle en réalité ? Expliquer le résultat obtenu.

