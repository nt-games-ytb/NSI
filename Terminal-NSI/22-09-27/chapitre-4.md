# Chapitre 4



## Exercice 5

### Question 1
Sa racine est "Toto".

### Question 2
Sa hauteur est de 6 si on compte les noeuds et 5 si on compte les arrêtes.

### Question 3
Sa taille est de 19 noeuds.

### Question 4
Son arité est de 4 noeuds.

### Question 5
Il y a 9 feuilles

### Question 6
Le grand-parent de "Tojtoj" est "Tintin".

### Question 7
"Tôtô" n'a pas de frères et soeurs.



## Exercice 6

### Question 1
```
Fonction recherche prennant comme paramètre élément et arbre:    
    définir l'arbre provisoire qui vaut l'abre    
    tant que tout les noeuds non pas était vu:    
	pour noeuds dans l'arbre provisoire:	#au début sa sera la racine    
	    si le noeuds est égale à l'élément alors:    
	        renvoie "Oui"    
        prendre le noeuds suivant    
    renvoie "Non"    
```

#### Correction :
```
fonction recherche(arbre, objet à demander)    
    si objet à chercher est dans racine:    
        retourner vrai    
    si arbre est une feuille:    
        passe    
    sinon:    
	on lance la fonction recherche pour tout les enfants     
```

### Question 2
#### Correction :
```
Fonction taille(arbre):    
    si arbre est une famille:    
        renvoie    
    sinon    
	je renvoie 1 + la somme des tailles des ...    
```