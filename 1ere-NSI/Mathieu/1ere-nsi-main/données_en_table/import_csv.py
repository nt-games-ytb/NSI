import csv

def import_csv(fichier):
  lecteur = csv.DictReader(open(fichier + '.csv', 'r'))
  return [dict(ligne) for ligne in lecteur ]


def select(table, critere):
  def test(ligne):
    return eval(critere)
  return [ligne for ligne in table if test(ligne)] 
