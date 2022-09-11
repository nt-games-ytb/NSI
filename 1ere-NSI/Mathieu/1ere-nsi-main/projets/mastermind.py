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