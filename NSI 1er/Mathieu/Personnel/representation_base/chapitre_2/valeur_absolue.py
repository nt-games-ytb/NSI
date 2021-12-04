def valeur_absolue(nombre):
    if str(nombre)[0] == "-":
        return int(str(nombre)[1:])
    else:
        return int(str(nombre))

def valeur_absolue_prof(nombre):
    if nombre > 0:
        return nombre
    elif nombre < 0:
        return -nombre
    else:
        return 0

def inverse(binaire):
    #binaire = str(binaire) #Au cas où c'est un int
    caractere = len(binaire)
    resultat = ""
    for i in range(caractere):
        if binaire[i:] == "0":
            resultat = resultat + "1"
        elif binaire [i:] == "1":
            resultat = resultat + "0"
    return int(resultat)

def addition_binaire(binaire1,binaire2):
    caractere = len(str(binaire2))
    resultat = ""
    for i in range(caractere):
        if binaire2[i:] == "0":
            resultat = resultat + binaire1[i:]
        elif binaire2[i:] == "1":
            if binaire1[i:] == "0":
                resultat = resultat + "1"
            else:
                resultat = resultat + "11"
    return resultat
