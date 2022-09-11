'''
import random
choix = ["toto", "andouille", "NSI", "patate"]
solution = random.choice(choix)
essais = 8
affichage = ""
for L in solution:
    affichage += "_"
l_trouvées = ""
while essais > 0:
    print("Mot : ", affichage)
'''
    
import random
choix = ["toto", "nsi", "patate", "jeanclaude", "évaporée", "colloïde", "coassiez", "testable", "maîtrise", "octroyai", "assainie", "pacifier", "détergés", "marnière", "saducéen", "plainera", "margotin", "damnâtes", "crussiez", "rigaudon", "reniâtes", "regarder", "attardes", "virolier", "tracanés", "regroupe", "aheurtée", "critique", "huméraux", "éditable", "plombées", "abdiqués", "maoïsmes", "syncopes", "payasses", "stylisés", "frottage", "plombure", "reboutes", "plommées", "maniques", "pagnotez", "mélanome", "materons", "allument", "récoltez", "gagerait", "extasiée", "vouaient", "subroger", "concerts", "enlevons", "meulages", "enlisons", "étageons", "cônirais", "paresses", "ischions", "secouiez", "toastons", "tripodie", "dérodera", "taraudée", "abstient", "replongé", "sciaient", "contesta", "hâtaient", "distrais", "solderez", "peintura", "vachards", "survécut", "végètent", "veillent", "cardigan", "vulvaire", "orseille", "bloquons", "pavanant", "tankiste", "pompeurs", "décochas", "airelles", "zoolithe", "prévîtes", "calibrez", "imagines", "essarter", "raflâtes", "afflouât", "lazulite", "loupasse", "abjurant", "filmages", "givreuse", "taveller", "parferez", "tunisien", "empiriez", "calcinée", "appelées", "présidée", "morcelés", "lyriques", "labiales", "tripotée", "chlamyde", "mouvance", "walkyrie", "ravisiez", "madéfies", "oubliais", "olibrius", "enrochât", "insérées", "gueulent", "excluons", "gênasses", "colombes", "baleiner", "plongeai", "dérivera", "déjugiez", "grenelés", "sévirent", "embouant", "poudreux", "fixistes", "roquâmes", "démêlées", "vêtirait", "réélûmes", "empirais", "crissais", "fortifia", "obturons", "jalouser", "cinérama", "acculiez", "ricochés", "coxalgie", "palmeras", "anhéliez", "ingérais", "chicotez", "débinons", "revivres", "verdirai", "cessants", "attestas", "libretto", "exhibiez", "puddlage"]
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
        print(" ||       /|\ ")
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
