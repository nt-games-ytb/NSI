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
    """
    :param: zoo est un dictionnaire dont les clés sont des str (noms des animaux) 
    :param: les valeurs de ces clés sont des tuples (origine, nombre) avec origine : str et nombre : int
    :return: le nom de l'animal le plus représenté dans le zoo, sous la forme d'une chaîne de caractères
    """
    
# Mes tests :
    '''
    resultat = ""
    nombre = 0
    
    # Test 1 :
    for cle in zoo.keys():
      if zoo.keys(1)[1] > nombre:
          résultat = zoo.keys(1)
          
    # Test 2 :
    for (cle, valeur) in zoo.items()
        if zoo[cle][1] > nombre:
            résultat = zoo[cle]
            
    # Test 3 :
    for (resultat(x,nombre), nombre) in zoo.items():
        if resultat(nombre) > nombre:
            resultat = resultat
    return resultat
    '''

# Correction : 
    nom_max = 0
    nombre_max = 0
    for (nom, (x,nombre)) in zoo.items():
        if nombre_max < nombre:
            nombre_max = nombre
            nom_max = nom
    return "L'animal le plus présent dans le zoo est " + nom_max + " avec " + str(nombre_max) + " animaux de ce type !"
    
    
def nombre_total(zoo, continent):
    """
    :param: zoo est un dictionnaire dont les clés sont des chaines, correspondantes aux noms des animaux
    :param: et dont les valeurs sont des tuples (origine, nombre), origine étant une chaine, nombre un int
    :param: continent est une chaine comprenant le nom d'un continent d'où sont originaires les animaux
    :return: la fonction renvoie le nombre d'animaux originaires de 'continent' dans ce zoo
    """
# Mes tests :
    '''
    nombre = 0
    # Test 1 (Plus lent et plus de ram) :
    
    for (i, (y,x)) in zoo.items():
        if y == continent :
            nombre = nombre + x
    return "Dans l'" + continent + ", il y a " + str(nombre) + " animaux !"
    
    # Test 2 (Mieux) :
    for valeur in zoo.values():
        if valeur[0] == continent :
            nombre = nombre + valeur[1]
    return nombre
    '''
    
# Correction :
    animals = 0
    for (origine, nombre) in zoo.values():
        if origine == continent :
            animals = animals + nombre
    return animals
    
    
def nombre(zoo, animal):
    """
    :param: zoo est un dictionnaire dont les clés sont des chaines, correspondantes aux noms des animaux
    :param: et dont les valeurs sont des tuples (origine, nombre), origine étant une chaine, nombre un int
    :param: animal est une chaine comprenant le nom d'un animal
    :return: la fonction renvoie le nombre de représentants du paramètre 'animal' dans ce zoo
    """
# Mes tests :
    """
    nombre = 0
    # Test 1 (Plus lent et plus de ram) :
    for (i, (y,x)) in zoo.items():
        if i == animal :
            nombre = nombre + x
    return "Il y a " + str(nombre) + " " + animal + " dans le zoo !"
    # Test 2 (Mieux) :
    for cle in zoo.keys():
        if cle == animal :
            nombre = cle[1]
    return nombre
    """
    
# Correction :
    if animal not in zoo.keys():
        return 0
    else:
        return zoo[animal][1]
    


