# Devoir maison 1ère NSI



> Dans cette évaluation, vous allez être confrontés à des exercices de conversions, de représentations, ainsi que de manipulations python basiques.
> Prenez le temps de lire les consignes des exercices, et n'oubliez pas que sur papier, vous n'avez pas la possibilité de tester votre code. Soyez donc vigilant-e-s aux détails. 
>
> Ce devoir est à rendre pour le vendredi 12 Novembre

------------



## Première Partie : Numération



### Exercice n°1

- Prendre sa date de naissance : additionner le jour, le mois, ainsi que l'année. On obtient alors un grand nombre en base 10.
- Représenter ce nombre en base 16 en expliquant la démarche.
- Représenter le jour de sa date de naissance en base 2. Détailler la méthode.



### Exercice n°2

- Donner l'écriture en base 10 des nombres suivants en détaillant la démarche :
  - 10011100<sub>2</sub>
  - 01010011<sub>2</sub>
  - 10100100<sub>2</sub>
  - BEEF <sub>16</sub>
  - 70E <sub>16</sub>





### Exercice n°3

- Écrire les nombres suivants en base 16. Détaillez votre raisonnement :
  - 1111010100001010<sub>2</sub>
  - 1011(10)
  - 6887<sub>10</sub>

-------------



## Deuxième Partie : Représentation des entiers relatifs & des nombres décimaux



### Exercice n°1

Soit l'écriture de l'entier relatif  **-3** sur 8 bits : 1000 0011<sub>2</sub>

- S'agit-il de binaire signé ou non signé ?
- Représenter -5,  -31, -64 et  -125 avec cette méthode

On peut également représenter -3(10) sous cette forme 1111 1101(2)

- Comment s'appelle la méthode de représentation utilisée ici ?
- En appliquant la même méthode, représenter -5, -31, -64 et -125 en expliquant une fois votre méthode.





### Exercice n°2



 **Pour convertir un réel décimal vers la base 2, on applique la méthode suivante, par exemple le nombre 12,6875** :

- On commence par convertir la partie entière : 12 <sub>10</sub> = 1100 (10)
- Puis, avec la partie décimale, on procède à des multiplications par 2 successives.
- Après chaque multiplication, on reprte le résultat sans la partie entière.
- Le calcul se poursuit jusqu'à ce que le résultat soit 1 :
  - 0,6875 * 2 = 1,375
  - 0, 375 * 2 = 0,75 
  - 0,75 * 2 = 1,5
  - 0,5 * 2 = 1
- Il ne nous reste plus qu'à noter la partie entière obtenue à chaque opération, de haut en bas : 0,675(10) = 1011(2) 
- Alors on peut écrire 12, 6875 <sub>10</sub> = 1100, 1011<sub>2</sub>



**Appliquer cette méthode pour représenter les nombres suivants:**

- 0,1 
- 0,3
- 12,4
-  32,06



--------------



## Troisième Partie : Codage des booléens



### Exercice n°1

Simplifier ces équations logiques:

1. $`S = (\overline{a} \lor b) \land (a \lor b)`$
2. $`S = \overline{a} \land b \land \overline{c} \lor \overline{a} \land b \land c \lor a \land b \land \overline{c} \lor a \land b \land c`$
3. $`S = a \land b \land c \lor b \land c \lor b \land \overline{b}`$
4. $`S = (a \lor \overline{a} \land b) \land \overline{( a \lor b )} \lor b \land \overline{c} \lor b \land c`$



### Exercice n°2



Ecrire les tables de vérités des équations ci dessus.





