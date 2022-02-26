## Fusion et jointures de tables



>  Lorsque l'on a de grandes quantités de données à traiter, il arrive que celles-ci soient réparties entre plusieurs tables. Il est donc parfois utile voir necessaire de regrouper toutes ces données dans une seule table. On appelle cela "fusion de tables" ou "jointure de tables"

### Le programme

![bo_3](assets/bo_3.png)

-----

- On veut fusionner deux tables selon un attribut commun. 
- On va donc selectionner dans chaque table la ligne ayant la même valeur pour l'attribut choisi.

Reprenons une table *Notes* vu précédemment :

| Prénom       | DS1  | DS2  | Projet |
| ------------ | ---- | ---- | ------ |
| Michelangelo | 12   | 14   | B      |
| Leonardo     | 15   | 16   | A      |
| Raphael      | 10   | 12   | C      |
| Donatello    | 13   | 15   | B      |

Admettons une seconde table et appellons la *Infos* :

| Prénom       | Âge  | Mail                |
| ------------ | ---- | ------------------- |
| Michelangelo | 16   | pizza@turtle.com    |
| Leonardo     | 15   | devinci@turtle.com  |
| Raphael      | 14   | chocolat@turtle.com |
| Donatello    | 17   | donut@turtle.com    |

- On souhaite regrouper les données des deux tables : on peut utiliser l'attribut "Prénom" pour cela.
- Il nous faut donc une fonction qui permettent de fusionner les tables:

```python
from copy import deepcopy
def fusion(table_1, table_2, cle_1, cle_2=None):
  if cle_2 is None:
    cle_2 = cle_1
  table_finale = []
  for ligne_1 in table_1:
    for ligne_2 in table_2:
      if ligne_1[cle_1] == ligne_2[cle_2]:
        ligne_finale = deepcopy(ligne_1)
        for cle in ligne_2:
          if cle != cle_2:
            ligne_finale[cle] = ligne_2[cle]
        table_finale.append(ligne_finale)
  return table_finale      
```

