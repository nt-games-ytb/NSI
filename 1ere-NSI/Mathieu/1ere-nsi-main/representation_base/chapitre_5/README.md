# Représentation d'un texte en machine

## Attendus

| Contenus | Capacités attendues |
| :--: | :-- |
| Représentation d’un texte en machine.<br />Exemples des encodages ASCII, ISO-8859-1, Unicode | Identifier l’intérêt des différents systèmes d’encodage.<br />Convertir un fichier texte dans différents formats d’encodage. |

## Contexte

![Martine écrit en UTF-8](https://www.apprendre-en-ligne.net/bloginfo/images/humour/geek_martine-ecrit-en-utf-8.jpg)

Source : http://www.retourdemartine.free.fr/


Prenons l'alphabet courant `A`, `B`, `C`, ... `Z` et plaçons le dans un tableau.

<table>
<tr>
<td>A</td>
<td>B</td>
<td>C</td>
<td>D</td>
<td>E</td>
<td>F</td>
<td>G</td>
<td>H</td>
<td>I</td>
<td>J</td>
<td>K</td>
<td>L</td>
<td>M</td>
<td>N</td>
<td>O</td>
<td>P</td>
<td>Q</td>
<td>R</td>
<td>S</td>
<td>T</td>
<td>U</td>
<td>V</td>
<td>W</td>
<td>X</td>
<td>Y</td>
<td>Z</td>
</tr>
</table>

Regardons les indices associés à chaque lettre.

<table>
<tr>
<th>0</th>
<th>1</th>
<th>2</th>
<th>3</th>
<th>4</th>
<th>5</th>
<th>6</th>
<th>7</th>
<th>8</th>
<th>9</th>
<th>10</th>
<th>11</th>
<th>12</th>
<th>13</th>
<th>14</th>
<th>15</th>
<th>16</th>
<th>17</th>
<th>18</th>
<th>19</th>
<th>20</th>
<th>21</th>
<th>22</th>
<th>23</th>
<th>24</th>
<th>25</th>
</tr>
<tr>
<td>A</td>
<td>B</td>
<td>C</td>
<td>D</td>
<td>E</td>
<td>F</td>
<td>G</td>
<td>H</td>
<td>I</td>
<td>J</td>
<td>K</td>
<td>L</td>
<td>M</td>
<td>N</td>
<td>O</td>
<td>P</td>
<td>Q</td>
<td>R</td>
<td>S</td>
<td>T</td>
<td>U</td>
<td>V</td>
<td>W</td>
<td>X</td>
<td>Y</td>
<td>Z</td>
</tr>
</table>

À un indice correspond une lettre et à une lettre est associée un et un seul indice.

## Définition

En généralisant à l'ensemble des caractères (`,`, `é`, `%`, ...), un caractère peut être représenté par un entier, donc avoir une représentation binaire en machine.

___Définition___

> L'entier associé à un caractère est appelé ___point de code___ de ce caractère (0 est le point de code de `A`. 25 le point de code de `Z`.)

___Définition___

> On parle ainsi d'___encodage de caractères___ : mécanisme qui gère les points de code en octets dans la mémoire de l’ordinateur, puis lit les octets à nouveau en points de code.

Il a existé et existe plusieurs encodages.

## Encodage ASCII

En 1960, l'organisation internationale de normalisation (ISO) décide de créer la norme ASCII (American Standard Code for Information Interchange).

À chaque caractère est associé un nombre binaire sur 7 bits.

![Table ASCII](https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/ASCII-Table.svg/738px-ASCII-Table.svg.png)

Source : Wikipédia

Comme vous pouvez le constater dans le tableau ci-dessus, au "A" majuscule correspond le code binaire $`(1000001)_2`$ $`(65)_{10}`$ ou $`(41)_{16}`$

___Question___

> Combien de points de code (et donc de caractères) peuvent être représentés grâce à l'encodage ASCII ?"

___Solution___

> Avec 7 bits, on peut coder $`2^7`$ points de code, donc 128 caractères.

___Travail à effectuer___

> 1. Quel est le point de code et la représentation en binaire, du caractère `a` ?
> 2. Comment grâce à la représentation, en binaire, peut-on savoir si une lettre est en majuscule ou minuscule ?

___Solution___

> 1. Le caractère `a` a pour point de code 97, soit $`(1100001)_2`$.
> 2. Le bit de rang 5 est égal à :
> 	- 1 si la lettre est en minuscule,
> 	- 0 si la lettre est en majuscule.

La norme ASCII convient bien à la langue anglaise, mais pose des problèmes dans d'autres langues, par exemple le français.

En effet, l'ASCII ne prévoit pas d'encoder les lettres accentuées.

## Encodage ISO-8859-1

Cette norme reprend les mêmes principes que l'ASCII, mais les points de code associés à chaque caractère sont codés sur 8 bits.

___Question___

> Combien de points de code (et donc de caractères) peuvent être représentés grâce à l'encodage ISO-8859-1 ?

___Soution____

> Sur 8 bits, on peut représenter $`2^8`$ points de code, soit 256 caractères... 2 fois plus que l'encodage ASCII.

Cette norme va être principalement utilisée dans les pays européens puisqu'elle permet d'encoder les caractères utilisés dans les principales langues européennes (la norme ISO-8859-1 est aussi appelée "latin1" car elle permet d'encoder les caractères de l'alphabet dit "latin").

Problème, il existe beaucoup d'autres langues dans le monde qui n'utilisent pas l'alphabet dit "latin", par exemple le chinois ou le japonais ! D'autres normes ont donc dû voir le jour.

Des changements de configuration sont nécessaires pour afficher un texte dans l'encodage adéquat.

## Encodage Unicode

Pour éviter ces problèmes, en 1991, une nouvelle norme a vu le jour : Unicode.

Unicode a pour ambition de rassembler tous les caractères existant afin qu'une personne utilisant Unicode puisse, sans changer la configuration de son traitement de texte, à la fois lire des textes en français ou en japonais.

Unicode est une table qui regroupe tous les caractères existant au monde. Unicode accepte plusieurs systèmes de codage : UTF-8, UTF-16, UTF-32.

Le plus utilisé, notamment sur le Web, est UTF-8.

### Nombre s'octets en UTF-8

Pour encoder les caractères Unicode, UTF-8 utilise un nombre variable d'octets (jusque 4) :

- Les caractères de numéro 0 à 127 sont codés sur un octet dont le bit de poids fort est toujours nul,
- Les caractères de numéro supérieur à 127 sont codés sur plusieurs octets.
- Dans ce cas, les bits de poids fort du premier octet forment une suite de 1 de longueur égale au nombre d'octets utilisés pour coder le caractère, les octets suivants ayant 10 comme bits de poids fort.

<table>
<caption><b>Définition du nombre d'octets utilisés</b></caption>
<thead>
<tr><th>Représentation binaire en UTF-8</th><th>Signification</th></tr>
</thead>
<tbody>
<tr><td>0xxxxxxx</td><td>1 octet codant 1 à 7 bits</td></tr>
<tr><td>110xxxxx 10xxxxxx</td><td>2 octets codant 8 à 11 bits</td></tr>
<tr><td>1110xxxx 10xxxxxx 10xxxxxx</td><td>3 octets codant 12 à 16 bits</td></tr>
<tr><td>11110xxx 10xxxxxx 10xxxxxx 10xxxxxx</td><td>4 octets codant 17 à 21 bits</td></tr>
</tbody>
</table>

### Méthode pour obtenir la représentation binaire en UTF-8 d'un caractère

1. Représenter le point de code associé au caractère en binaire
2. En fonction du nombre de bits, définir le nombre d'octets nécessaires pour une représentation en UTF-8
3. Découper les blocs de bits en autant d'octets nécessaires.

Exemple : le caractère `A` a pour point de code 65 dans la table Unicode.

1. Représentation binaire de 65 : <tt>100 0001</tt>
2. 7 bits sont nécessaires $`\rightarrow`$​ 1 octet nécessaire pour le représenter en UTF-8</li>
3. Représentation en UTF-8 : <tt><b>0</b>1000001</tt> ou $`(41)_{16}`$

Exemple : le caractère &#339; a pour point de code 339 dans la table Unicode.

1. Représentation binaire de 339 : <tt>1 0101 0011</tt>
2. 9 bits sont nécessaires $`\rightarrow`$ 2 octets nécessaires pour le représenter en UTF-8
3. l'octet de poids faible codant les 6 bits de poids faible, l'octet poids fort codant les 3 bits de poids forts
4. Représentation en UTF-8 : <tt><b>110</b>0101 <b>10</b>010011</tt> ou $`(\text{C}5\,93)_{16}`$

___Travail à effectuer___

> 1. Quelle est la représentation binaire du caractère `b` (point de code : 98) en UTF-8 ?
> 2. Quel est le point de code représenté par $`(\text{C}2\,80)_{16}`$ en UTF-8 ?

___Solution___

> 1. Le point de code 98 a comme représentatio binaire : $`(1100010)_`$
>		- 7 bits sont nécessaires &rArr; 1 octet nécessaire pour le réprésenter en UTF-8
>		- Représentation en UTF-8 : <tt><b>0</b>1100010</tt> ou $`(62)_{16}`$
> 2. $`(\text{C}2\,80)_{16} = (11000010\,10000000)_{16}`$

Le point de code est représenté par les bits <tt>110<b>00010</b> 10<b>000000</b></tt>. Soit $`(10000000)_2 = (128)_{10}`$

<table>
	<caption><b>Exemples de codage UTF-8</b></caption>
	<thead>
    <tr>
      <th>Point de code</th>
      <th>Caractère</th>
      <th>Représentation binaire UTF-8</th>
    </tr>
	</thead>
	<tbody>
		<tr>
			<td>66</td>
			<td>B</td>
      <td><tt><b>0</b>1000010</tt></td>
    </tr>
    <tr>
      <td>233</td>
      <td>é</td>
      <td><tt><b>110</b>00011 <b>10</b>101001</tt></td>
    </tr>
    <tr>
      <td>8364</td>
      <td>€</td>
      <td><tt><b>1110</b>0010 <b>10</b>000010 <b>10</b>101100</tt></td>
    </tr>
    <tr>
      <td>119070</td>
      <td>𝄞</td>
      <td><tt><b>11110</b>000 <b>10</b>011101 <b>10</b>000100 <b>10</b>011110</tt></td>
    </tr>
	</tbody>
</table>

___Observation___

Dans toute chaîne de caractères UTF-8, on remarque que :

- tout octet de bit de poids fort nul code un caractère ASCII sur un octet,
- tout octet de bits de poids fort valant <tt><b>11</b></tt> est le premier octet d'un caractère codé sur plusieurs octets,
- tout octet de bits de poids fort valant <tt><b>10</b></tt> est à l'intérieur d'un caractère codé sur plusieurs octets.
