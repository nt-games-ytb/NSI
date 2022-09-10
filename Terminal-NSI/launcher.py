import os

dossier = os.path.dirname(os.path.realpath(__file__))

print("Bienvenue sur le launcher de Terminal NSI !")

print("\r\nVoulez-vous lancer le dernier fichier modifier ? (Oui ou Non) ")
dernier = str(input())
if dernier == "Oui" or dernier == "oui" or dernier == "OUI" or dernier == "O" or dernier == "o":
    print("OK")

print("\r\nVoici les dossier disponible :")
listeDesDossiers = [x[0] for x in os.walk(dossier)]
listeDesDossiers.pop(0)
nombre = 1
for element in listeDesDossiers:
    print(nombre + " - " + element.replace(dossier, ""))
    nombre = nombre + 1

