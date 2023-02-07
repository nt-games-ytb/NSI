# Chapitre 10



## Exercice 7
Il y a 10 places, dont :    
- 3 P1    
- 3 P2    
- 4 P3     

On sait que P3 arrive à 0, P2 arrive à 2 et P1 arrive à 3.    
Alors :       
```
|P3 |P3 |P2 |P1 |P1 |P1 |P2 |P2 |P3 |P3 |    
0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10    
```    



## Exercice 9
Selon moi, le scénario 1 et 2 ne provoque pas d'interblocage.    
C'est le scénario 3 qui provoque un interblocage.    
En effet, à un moment, P3 et P1 attendent R2.    
C'est P3 qui acquérire R2 en premier or dans l'ordre des prioritées, P1 est logiquement censé passer avant.    
Il y a donc un problème et un interblocage.    

D'après le prof, c'est le scénario 2, voici les lignes importantes :    
P1 acquiert R1    
P3 acquiert R2    
P1 attend R2    
P3 attend R1    