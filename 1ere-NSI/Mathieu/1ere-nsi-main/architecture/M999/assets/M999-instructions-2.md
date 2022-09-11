---
title: M999 - jeu d'instructions 2
author: Philippe BODDAERT
---

# 1. Contexte

Le processeur M999 est doté d'un jeu d'instructions.

Une instruction est un mot de 3 chiffres, appelé _opcode_, correspondant à une opération à effectuer par le processeur.

Le premier chiffre de l'opcode détermine le type de l'opération (copie, opération arithmétique, saut d'instruction ...). 

Les deux derniers chiffres indiquent, selon le type de l'opération, une adresse mémoire, un registre, un sous-type d'opération...

# 2. Jeu d'instructions

| op0   | op1 op2   | instruction à réaliser                                       |
| ----- | --------- | ------------------------------------------------------------ |
| 0     | _addr_    | copie le mot mémoire d’adresse _addr_ dans le registre A     |
| 1     | _addr_    | copie le mot mémoire d’adresse _addr_ dans le registre B     |
| 2     | _addr_    | copie le contenu du registre R dans le mot mémoire d'adresse _addr_ |
| 3     | 0 0       | ajoute les valeurs des registres A et B, produit le résultat dans R |
| 3     | 0 1       | soustrait la valeur du registre B à celle du registre A, produit le résultat dans R |
| 3    | 0 2     | divise la valeur du registre A par 2, le quotient est placé dans R, le reste dans B |
| 3    | 0 3     | multiplie la valeur du registre A par 2, le résultat est placé dans R |
| 3     | 9 9       | ne fait rien                                                 |
| 4     | _rs_ _rd_ | copie la valeur du registre source _rs_ dans le registre destination _rd_ |
| 5     | _addr_    | branche en _addr_ (PC reçoit la valeur _addr_)               |
| 6     | _addr_    | branche en _addr_ si la valeur du registre R est strictement positive |

Les registres (_rs_, _rd_) sont désignés par les valeurs suivantes :

valeur | registre
:------: | :--------:
0 | A
1 | B
2 | R

