zoo_Beauval = {
'elephant' : ('Asie', 5),
'ecureuil' : ('Asie', 17),
'panda' : ('Asie', 2),
'hippopotame' : ('Afrique', 7),
'girafe' : ('Afrique', 4)
}

zoo_LaFleche = {
  'ours' : ('Europe', 4),
  'tigre' : ('Asie', 7),
  'girafe' : ('Afrique', 11),
  'hippopotame' : ('Afrique', 3)
  }

def plus_grand_nombre(zoo):
  #"""
  #:param: zoo est un dictionnaire dont les clés sont des str (noms des animaux) 
  #:param: les valeurs de ces clés sont des tuples (origine, nombre) avec origine : str et nombre : int
  #:return: le nom de l'animal le plus représenté dans le zoo, sous la forme d'une chaîne de caractères
  #"""
    resultat = ""
    nombre = 0
    
    nom_max = 0
    nombre_max = 0
#   for cle in zoo.keys():
#      if zoo.keys(1)[1] > nombre:
#          résultat = zoo.keys(1)
#    for (cle, valeur) in zoo.items()
#        if zoo[cle][1] > nombre:
#            résultat = zoo[cle]
#    for (resultat(x,nombre), nombre) in zoo.items():
#        if resultat(nombre) > nombre:
#            resultat = resultat
    for (nom, (x,nombre)) in zoo.items():
        if nombre_max > nombre:
            nombre_max = nombre
            nom_max = nom
    return nom_max
    return resultat
