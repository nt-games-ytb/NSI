# Codage des booléens

## Attendus

| Contenus | Capacités attendues |
| :--: | :-- |
| Valeurs booléennes : 0,1. Opérateurs booléens : and, or, not.<br />Expressions booléennes | Dresser la table d’une expression booléenne | 

## Définition

De nombreux dispositifs électroniques, électromécanique, (mécanique, électrique, pneumatique, etc....) fonctionnement en TOUT ou RIEN.

Ceci sous-entend qu'ils peuvent prendre 2 états. 

Exemples : 

- Arrêt / Marche
- Enclenché / Déclenché
- Vrai / Faux
- Ouvert / Fermé
- Avant / Arrière
- Conduction / Blocage

Un système présentera un fonctionnement __logique combinatoire__ si l'état à un instant $`t`$ des variables de sortie ne dépend que de l'état des variables d'entrée au même instant $`t`$.

## Variable logique

Une variable logique ne peut prendre que 2 états:

| État Vrai | État Faux |
| :--: | :--: |
| Oui | Non |
| True | False |
| 1 | 0 |
| Haut | Bas |
| High | Low |

Pour ces raisons, il est beaucoup plus avantageux d'employer un système mathématique n'utilisant que 2 valeurs numériques.

Par convention, on utilise les valeurs 0 / 1 pour représenter les états d'une variable logique.

La variable binaire est aussi appelée variable __booléenne__. (De George Boole, mathématicien anglais 1815 - 1864)

## Fonction logique

Une fonction $`S`$ (exemple: allumer une lampe) peut comporter $`n`$ variables logiques.
Pour chacune de ces combinaisons, la fonction peut prendre une valeur 0 ou 1.
Nous obtenons $`2^n`$ combinaisons pour ces $`n`$ variables.

### Table de vérité

On représente l'ensemble valeurs d'entrées et sorties par une table de vérité :

- À chaque variable d'entrée correspond une colonne, 
- À chaque ligne, une valeur d'état possible,
- Une colonne de sortie contient la valeur de l'état de l'opération.

Exemple : 

```math
\begin{aligned}
S = 1 \text{ si} \left\{
\begin{array}{l}
 a = 0 \text{ et } b = 1 \\
 a = 0 \text{ et } b = 0 \\
 a = 1 \text{ et } b = 0
 \end{array}
\right.
\end{aligned}
```

| $`a`$ | $`b`$ | $`S`$ |
| :--: | :--: | :--: |
| 0 | 1 | 1 |
| 0 | 0 | 1 |
| 1 | 1 | 0 |
| 1 | 1 | 0 |
| 1 | 0 | 1 |

### Opérateurs logiques

#### Opérateur NON

On associe à une variable binaire quelconque $`a`$ son complément, noté $`\overline{a}`$

```math
\begin{aligned}
S = 1 \text{ ssi } a = 0
\end{aligned}
```

La table de vérité de l'opérateur NON :

| $`a`$ | $`S = \overline{a}`$ |
| :--: | :--: |
| 0 | 1 |
| 1 | 0 |

#### Opérateur ET

L'état 1 est obtenu lors de l’action simultanée sur les 2 variables $`a`$ et $`b`$. L'opérateur est noté $`\land`$

```math
\begin{aligned}
S & = 1 \text{ ssi } a = 1 \text{ et } b = 1 \\
 & = a \land b
\end{aligned}
```

La table de vérité de l'opérateur ET :

| $`a`$ | $`b`$ | $`S = a \land b`$ |
| :--: | :--: | :--: |
| 0 | 0 | 0 | 
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

##### Propriétés

```math
\begin{aligned}
 a \land a & = a \\
 a \land 1 & = a \\
 a \land \overline{a} & = 0 \\
 a \land 0 & = 0
\end{aligned}
```

#### Opérateur OU

L'état 1 est obtenu lors de l’action simultanée sur l'une des 2 variables ou les 2. L'opérateur est noté $`\lor`$

```math
\begin{aligned}
S = 1 \text{ si} \left\{
\begin{array}{l}
 a = 0 \text{ ou } b = 1 \\
 a = 1 \text{ ou } b = 0 \\
 a = 1 \text{ ou } b = 1
 \end{array}
\right.
\end{aligned}
```

La table de vérité de l'opérateur OU :

| $`a`$ | $`b`$ | $`S = a \lor b`$ |
| :--: | :--: | :--: |
| 0 | 0 | 0 | 
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

##### Propriétés

```math
\begin{aligned}
 a \lor a & = a \\
 a \lor 1 & = 1 \\
 a \lor \overline{a} & = 1 \\
 a \lor 0 & = a
\end{aligned}
```

### Algèbre de Boole 

#### Définition

Système algébrique constitué de l'ensemble $`\{0, 1\}`$, muni des 3 opérateurs de base NON, ET, OU.

#### Propriétés

- __Associativité__ : Comme avec les opérations habituelles, certaines parenthèses sont inutiles. Exemple : $`( a \land b ) \land c = a \land (b \land c) = a \land b \land c`$
- __Commutativité__ : L'ordre est sans importance. Exemple : $`a \land b = b \land a`$
- __Distributivité__ : Exemple : $`a \lor ( b \land c ) = ( a \lor b ) \land ( a \lor c )`$
- __Idempotence__ : Exemple : $`a \land a \land a \land \dots \land a = a`$

### Forme canonique

Combinaison des variables de la fonction via les opérateurs de base de l’__algèbre de Boole__.

La fonction $`S`$ définie par :

```math
\begin{aligned}
S = 1 \text{ si} \left\{
\begin{array}{l}
 a = 0 \text{ et } b = 1 \\
 a = 0 \text{ et } b = 0 \\
 a = 1 \text{ et } b = 0
 \end{array}
\right.
\end{aligned}
```

$`S`$ s'écrit sous sa forme canonique : $`S= (\overline{a} \land b) \lor (\overline{a} \land \overline{b}) \lor (a \land \overline{b})`$

### 

## Exercices

### Établir des tables de vérité

**Travail à effectuer** : Écrire les tables de vérité des expressions booléennes suivantes :

1. $`S(a, b) = \overline{a} \land b`$
2. $`S(a, b) = b \lor (a \land b)`$
3. $`S(a, b) = a \land (a \lor b)`$
4. $`S(a, b, c) = (\overline{a} \land b) \lor (a \land c)`$
5. Communication = Émetteur ET Récepteur
6. Décrocher = (Sonnerie ET Décision de répondre) OU décision d'appeler
7. Bac = Avoir la moyenne OU (NON Avoir la moyenne ET rattrapage)

### Équivalence d'expressions booléennes

1. Montrer que $`(a \land b) = \overline{\overline{a} \lor \overline{b}}`$
2. Montrer que $`(a \lor b) = \overline{\overline{a} \land \overline{b}}`$

N.B : Deux expressions booléennes sont équivalentes si leurs tables de vérité le sont. 

Autrement dit, si pour toutes les entrées des tables de vérité, l'ensemble des valeurs de sorties de ces mêmes tables sont équivalentes alors les expressions booléennes sont équivalentes.

### Déterminer une expression booléenne

| a | b | ssi(a, b) |
| :--: | :--: | :--: |
| 0 | 0 | __1__ |
| 0 | 1 | __0__ |
| 1 | 0 | __0__ |
| 1 | 1 | __1__ |

**Travail à effectuer** : Trouver l'expression booléenne, notée ssi(a, b) à partir de la table de vérité ci-dessus.

### Loi de De Morgan

Les __lois de De Morgan__ sont des identités entre propositions logiques. Elles ont été formulées par le mathématicien britannique Augustus De Morgan (1806-1871).

1. $`\overline{(a \lor b)} = \overline{a} \land \overline{b}`$
2. $`\overline{(a \land b)} = \overline{a} \lor \overline{b}`$

**Travail à effectuer** : Démontrer ces 2 lois.

