## Propriétés et caractéristiques d'un algorithme

Il est essentiel, pour un bon algorithme, de posséder certaines propriétés :

- La **terminaison** : Votre algo doit donner un résultat en un **nombre fini d'étapes** et donc ne surtout pas rester coincé dans une boucle.

- La **validation** : Votre algorithme doit amener au résultat attendu, peu importe la situation.

En plus de ces deux propriétés, on peut également citer ***le coût*** ou ***complexité*** :

- en **temps** : le nombre d'opérations nécessaires à son exécution 
- en **espace** : la quantité d'espace mémoire nécessaire à son exécution

Ici, nous ne nous intéresserons uniquement qu'au **coût en temps, la complexité temporelle.**

### Complexité d'un algorithme

On ne va pas vous demander de chronométrer l'exécution, mais plutôt de trouver **l'ordre de grandeur**.

Il s'agit de différencier les algorithmes selon un type de complexité : on va les grouper par *familles*.

Soit *n* la taille des données d'entrée, on notera la complexité d'un algorithme en fonction de *n* : 
$$
O(f(n))
$$

> On note O pour ***Ordre de grandeur***

| Complexité    | Notation         | Temps pour n = 10 | Temps pour n = 1000 | Temps pour n = 10<sup>6</sup> |
| ------------- | ---------------- | ----------------- | ------------------- | ----------------------------- |
| Constante     | O(1)             | 10 ns             | 10 ns               | 10 ns                         |
| Logarithmique | O(log(n))        | 10 ns             | 30 ns               | 60 ns                         |
| Linéaire      | O(n)             | 100 ns            | 10 μs               | 10 ms                         |
| Quadratique   | O(n<sup>2</sup>) | 1 μs              | 10 ms               | 2,8 heures                    |



*Pour comprendre la notion de complexité, utilisons l'exemple de tri de tableau : il s'agit d'un des cas les plus récurrents d'utilisation d'un algorithme. On a un tableau, contenant des élèments que l'on devra trier dans un ordre précis.*

*Si un algorithme met un temps donné pour trier un tableau de taille n, combien de temps lui faudra t-il pour trier un tableau 10 ou 100 fois plus grand ?*

- La **complexité d'un algorithme** est une mesure du temps requis par l'algorithme pour accomplir sa tâche, en fonction de la taille des données à traiter.
- On dira d'un problème qu'il est aussi complexe que le meilleur algorithme connu pour le résoudre.
- Si la **complexité** est **constante**, alors le temps d'execution sera sensiblement toujours le même, peu importe la taille du tableau traité.
- Si elle est **logarithmique**, alors le temps d'execution augmente très faiblement quand le paramètre croit.
- **Complexité** **linéaire** : le nombre d'étapes à effectuer va varier en proportion directe de la taille de l'échantillon à traiter : si l'échantillon croît par un facteur de 10000, la complexité sera accrue elle aussi par un facteur de 10000.
- **Complexité Quadratique** : Dans le cadre du tri par insertion, par exemple, quand on double la taille du tableau, le nombre de comparaisons sera lui multiplié par...4.

------

Auteur : Florian Mathieu

Licence CC BY NC

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Licence Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a> <br />Ce cours est mis à disposition selon les termes de la <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Licence Creative Commons Attribution - Pas d’Utilisation Commerciale - Partage dans les Mêmes Conditions 4.0 International</a>.
