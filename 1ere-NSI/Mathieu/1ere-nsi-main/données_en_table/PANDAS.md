## La bibliothèque Pandas



La bibliothèque pandas est l'une des plus utilisées pour la gestion de données - appelée également *Data Science*.

Comme pour toutes les bibliothèques python, on doit l'importer en début de fichier :

```python
import pandas
```

Elle nous permet de lire un fichier CSV de manière beaucoup plus rapide :

```python
pandas.read_csv('nom_du_fichier.csv' delimiter = ';')
```

Mais également un fichier Excel :

```python
pandas.read_excek('nom_de_fichier.xlsx' delimiter = ';')
```

On obtient alors un objet caractéristique de cette bibliothèque qu'on appellera *dataframe* et qu'on peut représenter par un tableau de p-uplets nommés (on utilise alors des noms au lieu d'indices).

De plus, Pandas permet d'effectuer les manipulations de base que l'on a vu précédemment et même plus :

Exemple, une table nommée 'table' pourra être utilisée :

- pour afficher les 10 premières lignes : table.head(10)
- pour afficher les en-têtes des colonnes (aussi appelés champs) : table.columns( )

Enfin, on peut également fusionner deux tables ensemble via cette instruction:

```python
pandas.merge(table_1,table_2)
```

