## Exercice 1

Écrire, en Python, une fonction `approximation` , prenant en entrée :
- deux paramètre `a` et `b`, les flottants à comparer),
- un paramètre `precision`, un entier donnant le nombre de chiffres après la virgule souhaitée entre 0 et 16

* Cette fonction reverra `True` si $`|a - b|< 10^{-precision}`$​ et `False` sinon.
* Documenter la fonction
* Créer plusieurs DocTests renvoyant soit True soit False.

_Remarque : On utilisera la fonction valeur absolue : [`abs` ](https://www.w3schools.com/python/ref_func_abs.asp)_

Si nous avons besoin de comparer des flottants, on utilisera donc cette fonction.

## Exercice : 2

Ecrire, en Python, une fonction `pythagore` prenant en entrée 3 flottants `a`, `b`, `c` et renvoie `True` si le triangle de dimension `a`, `b`et `c`est rectangle et `False` sinon.

_Attention : On ne sait pas lequel de `a`, `b` ou `c` est le plus grand côté ! Il faudra donc étudier tous les cas possibles !`

- Documenter la fonction
- Créer plusieurs DocTests renvoyant soit True soit False. 

## Exercice : 3

Écrire, en Python, une fonction `f` prenant en entrée un paramètre `x`, un flottant. Cette fonction renverra $x^3 + 3 * x^2 +3 * x +1$ 

Écrire, en Python, une fonction `g` prenant en entrée un paramètre `x`, un flottant. Cette fonction renverra $(x + 1)^3$

Écrire en Python une fonction `egalite` prenant en entrée 2 paramètres `f` et `g`, deux fonctions Python renvoyant des valeurs flottantes. Elle devra :

- Comparer approximativement, avec une précision de 10 chiffres après la virgule, les fonctions `f` et `g` en prenant aléatoirement 1000 valeurs de `x` dans l'intervalle [-10, 10].
- Si une des comparaisons est fausse, alors la fonction renverra `False`
- Si toutes les comparaisons sont vraie, alors la fonction renverra `True`



_Remarque : Évidemment, il s'agit de comparaison **approximative**. Si les deux fonctions sont égales 1000 fois à $`10^{-10}`$ près, il y a de fortes chances qu'elles sont égales... mais ce n'est pas une certitude !_

Modifier et `f` pour qu'elle renvoie $`x²`$ et `g` pour qu'elle renvoie $`x² + 10^{⁻11}`$.

- les deux fonctions sont-elles égales ?
- qu'en dit la fonction `egalite` ?
