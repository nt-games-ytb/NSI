'''import csv

def import_csv(fichier):
    lecteur = csv.DictReader(open(fichier + '.csv', 'r'))
    print([dict(ligne) for ligne in lecteur])
    #return [dict(ligne) for ligne in lecteur ]

def import_csv2(fichier):
    resultat = []
    with open(fichier + '.csv',newline = '') as csvfile:
        s = csv.reader(csvfile,delimiter = ';')
        for i in s:
            resultat.append(i)
    print(resultat)
    #return resultat 
  
def vers_csv(nom, ordre):
    with open(nom + '.csv', 'w') as fic:
        dic = csv.DictWriter(fic, fieldnames = ordre)
        table = eval(nom)
        dic.writeheader() # première ligne, celle des attributs
    for ligne in table:
        dic.writelow(ligne) # ajoute les lignes de la table)
    return None

folder = "D:/NSI_1er/Mathieu/Personnel/donnees_en_table/"
#import_csv("tortues")
#import_csv("D:/NSI_1er/Mathieu/Personnel/donnees_en_table/tortues")
#import_csv("NSI_1er/Mathieu/Personnel/donnees_en_table/tortues")
import_csv(folder + "tortues")
import_csv2(folder + "tortues")
'''
def f(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print(f(4))