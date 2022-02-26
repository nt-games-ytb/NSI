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

