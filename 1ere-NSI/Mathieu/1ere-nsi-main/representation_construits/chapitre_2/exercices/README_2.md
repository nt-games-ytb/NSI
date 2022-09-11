## Exercice n°2



Pour remplir le pokedex de Sacha, on modélise les informations sur les Pokemons de la façon suivante :

```python
liste_pokemons = {
  'Bulbizarre' : (70, 7),
  'Herbizarre' : (100,13),
  'Abo' : (200, 7),
  'Pikachu' : (40, 6)
}
```

Les tuples représentent la taille en centimètres, ainsi que le poids en kilogramme du Pokemon.

#### Questions :

- Quel est le type de *liste_pokemons* ?

- Quelle instruction permet d'ajouter à cette structure de données le Pokemon Goupil qui mesure 60 cm et pèse 10 kg ?

On donne le code suivant :

```python
def le_plus_grand(pokemons):
  grand = None
  taille_max = None
  for (nom,(taille, poids)) in pokemons.items():
    taille_max = taille
    grand = nom
  return(grand,taille_max)
```

- Quelle est la valeur de *le_plus_grand(liste_pokemons)* ?

- Écrire le code d'une fonction *le_plus_leger(liste_pokemons)* qui prend des Pokémons en paramètre et renvoie un tuple correspondant au nom ainsi qu'au poids de Pokémon le plus léger.

```python
>> le_plus_leger(liste_pokemons)
>> ('Pikachu', 6)
```



- Écrire une fonction *taille* qui prend en paramère un dictionnaire de Pokémons ainsi que le nom d'un Pokémon, et qui renvoie la taille de ce Pokémon.

```python
>> taille(liste_pokemons, 'Abo')
>> 200
```

```python
>> taille(liste_pokemons, 'Dracaufeu')
>> None
```

