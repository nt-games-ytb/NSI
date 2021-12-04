# Tableaux Python



En python, une matrice est un *tableau de tableaux*.

```python
matrice= [[2,4,3,7],[1,3,6,7],[5,7,0,2],[1,8,9,3]]
```

On peut représenter l'instruction ci dessus de cette manière :

| 2    | 4    | 3    | 7    |
| ---- | ---- | ---- | ---- |
| 1    | 3    | 6    | 7    |
| 5    | 7    | 0    | 2    |
| 1    | 8    | 9    | 3    |

Pour accéder à un élèment d'une matrice, s'agissant d'un tableau de tableaux, on utilisera deux *indices* :

- L'indice du tableau contenant l'élèment
- L'indice de l'élèment dans le tableau selectionné précédemment

On accède donc à l'élèment situé en ligne **i** et colonne **j** par 

```pyth
 matrice[i][j]
```

Par exemple si l'on reprend le tableau ci dessus :

```python
matrice[2][3]
2
```

Soit la matrice m = [["a","b"],["c","d"],["e","f"],["g","h"]]

Comment accéder à l'élément "e" ?

