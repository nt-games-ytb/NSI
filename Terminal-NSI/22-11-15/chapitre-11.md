# Chapitre 11



## Exercice 9

### Question 1
Le trajet parcouru est :    
routeur A puis routeur C, puis routeur F, puis routeur G    
avec une distance minimal de 3 sauts.    

### Question 2
Table de routage du routeur F :    
| Destination | Routeur suivant | Distance |
|:---:|:---:|:---:|
| A | F | 3 |
| B | E | 3 |
| C | F | 2 |
| D | E | 2 |
| E | E | 1 |
| F | F | 1 |

### Question 3
Table de routage du routeur F :    
| Destination | Routeur suivant | Distance |
|:---:|:---:|:---:|
| B | B | 1 |
--| C | C | 1 |--
| D | D | 1 |
| E | D | 2 |
| F | D | 4 |
| G | D | 3 |



## Exercice 11

### Question 1
10**8 / 10 000 000 000 = 0,01    
Le coût entre les routeur A et B est bien de 0,01.     

### Question 2
10**8 / 5 = 20 000 000 bits/s = 20 Mb/s    
Le débit de la liaison entre le routeur B et D.    

### Question 3
On retrouve 4 chemins possible :    
- A B D E G     
- A D E G    
- A C E G    
- A C F G    
On sait que plus le débit est grand et plus le coût est petit.    
Nous pouvons retirer A C E G car la liaison C et E à un débit plus petit que la liaison C et F.    
Nous pouvons retirer A B D E G car comparer à A D E G il fera un saut en plus.    
Pour finir de choisir entre A B D E G et A C F G nous allons calculer le coût des liaisons :    
A D E G = coût de AD + coût de DE + coût de EG = 0,01 + 5 + 0,001 + 1 = 1,011    
A C F G = coût de AC + coût de CF + coût de FG = 10 + 1 + 1 = 12    
Le chemin dont la somme des coût sera le plus petit possible est A B D E G.     
