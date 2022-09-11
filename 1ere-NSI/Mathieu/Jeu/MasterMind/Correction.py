# Vendredi 25/02
'''
import random

couleurs = []
code = []
code_essaye = []
présent = 0
bonne_place = 0
essais = 12
essai = 1

while len(code) < 4:
    code.append(random.choice(["Rouge", "Jaune", "Orange", "Vert", "Bleu", "Noir"]))

gameover = False
while gameover == False:
    print("Essaie numéro " + str(essai) + " sur 12")  

    clavier = str(input("Entrez le code (un espace entre chaque caractère) \n"))
    code_essaye = clavier.split(' ')

    i = 0
    while i < len(code):
        if code_essaye[i] == code[i]:
            bonne_place =+ 1
            i =+ 1

    i = 0
    while i < len(code_essaye):
        présent += code.count(code_essaye[i])
        i =+ 1
'''

# Jeudi 03/03
#-*-coding: utf8 -*-
import random

code = [] # code établi par l'ordinateur
pCode =  [] # code rentré par l'utilisateur
pCode_s = ""  #texte rentré par le joueur
cInCode = 0 # couleur présente dans le code
cInPlace = 0 # bonne couleur à la bonne place
essais = 12 #nombre d'essais disponibles
essai = 1 #essai actuel

while len(code) <4:
    code.append(random.choice(['J','B','R','V','O','N']))
    
gameOver = False
while gameOver == False:
    print("essai", essai, "sur 12")
    pCode_s = str(input("Entrez une combinaison de couleurs(un espace entre chaque) \n"))
    pCode = pCode_s.split(' ')

    i = 0
    while i < len(code):
        if pCode[i] == code[i]:
            cInPlace +=1
        i+=1
    i = 0
    while i < len(pCode):
        cInCode += code.count(pCode[i])
        i+=1
    
    essai +=1
    print(cInPlace, " pions de bonne couleur à la bonne place")
    print(cInCode, " pions de bonne couleur")
    if cInPlace == 4 or essai == essais:
        gameOver = True
        print("Vous avez gagné !")
        print("code :", ('').join(code))
    cInCode = 0
    cInPlace = 0
quit()
