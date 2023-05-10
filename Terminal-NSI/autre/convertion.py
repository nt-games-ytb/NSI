def base10ToBinaire(base10):
    i=0
    while 2**i <= base10:
        i = i + 1
    i = i - 1
    sortie = ""
    while i >= 0:
        if 2**i <= base10:
            sortie= sortie + "1"
            base10 = base10 - 2**i
        else:
            sortie = sortie + "0"
        i = i - 1
    return sortie

def binaireToBase10(binaire):
    longueur = len(binaire)
    resultat = 0
    for i in range(longueur):
        bit = int(binaire[i])
        nombre = bit * 2**(longueur-i-1)
        resultat = resultat + nombre
    return resultat

def base10ToBase16(nombre):
    i = 0
    while 16**i <= nombre:
        i = i + 1
    i = i - 1
    sortie = ""
    while i >= 0 :
        quotient = nombre // (16**i)
        nombre = nombre - (quotient * 16**i)
        if quotient < 10:
            sortie = sortie + str(quotient)
        elif quotient == 10:
            sortie = sortie + "A"
        elif quotient == 11:
            sortie = sortie + "B"
        elif quotient == 12:
            sortie = sortie + "C"
        elif quotient == 13:
            sortie = sortie + "D"
        elif quotient == 14:
            sortie = sortie + "E"
        elif quotient == 15:
            sortie = sortie + "F"
        i = i - 1
    return sortie

def base16ToBase10(base16):
    longueur = len(base16)
    resultat = 0
    for i in range(longueur):
        if base16[i] == "0":
            decimal = 0
        elif base16[i] == "1":
            decimal = 1
        elif base16[i] == "2":
            decimal = 2
        elif base16[i] == "3":
            decimal = 3
        elif base16[i] == "4":
            decimal = 4
        elif base16[i] == "5":
            decimal = 5
        elif base16[i] == "6":
            decimal = 6
        elif base16[i] == "7":
            decimal = 7
        elif base16[i] == "8":
            decimal = 8
        elif base16[i] == "9":
            decimal = 9
        elif base16[i] == "a" or base16[i] == "A":
            decimal = 10
        elif base16[i] == "b" or base16[i] == "B":
            decimal = 11
        elif base16[i] == "c" or base16[i] == "C":
            decimal = 12
        elif base16[i] == "d" or base16[i] == "D":
            decimal = 13
        elif base16[i] == "e" or base16[i] == "E":
            decimal = 14
        elif base16[i] == "f" or base16[i] == "F":
            decimal = 15
        nombre = decimal * 16**(longueur - i - 1)
        resultat = resultat + nombre
    return resultat