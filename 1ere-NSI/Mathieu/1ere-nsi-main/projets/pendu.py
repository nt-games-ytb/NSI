import random
choix = ["toto", "nsi", "patate", "jeanclaude"]
solution = random.choice(choix)

essais = 7
affichage = ""
lettres_trouvees = ""

for l in solution:
  affichage = affichage + "_ "

print(">> Bienvenue dans le pendu <<")

while essais > 0:
  print("\nMot à deviner : ", affichage)
  proposition = input("proposez une lettre : ")[0:1].lower()

  if proposition in solution:
      lettres_trouvees = lettres_trouvees + proposition
      print("-> Bien vu!")
  else:
    essais = essais - 1
    print("-> Nope\n")
    if essais==0:
        print(" ==========Y= ")
    if essais<=1:
        print(" ||/       |  ")
    if essais<=2:
        print(" ||        0  ")
    if essais<=3:
        print(" ||       /|\ ")
    if essais<=4:
        print(" ||       /|  ")
    if essais<=5:                    
        print("/||           ")
    if essais<=6:
        print("==============\n")

  affichage = ""
  for x in solution:
      if x in lettres_trouvees:
          affichage += x + " "
      else:
          affichage += "_ "

  if "_" not in affichage:
      print(">>> Gagné! <<<")
      break
     
print("\n    * Fin de la partie *    ")