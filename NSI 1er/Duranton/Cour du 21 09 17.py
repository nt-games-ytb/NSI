print("############################################")
print("# Chapitre 1 : Nombres, binaires et octets #")
print("#              Duranton.net                #")
print("############################################")

# Exercice 5

def uncaractereto10(binaire):
    if binaire=="0":
        return 0
    elif binaire=="1":
        return 1

# Exercice 6

def deuxcaractereto10(binaire):
    if binaire=="00":
        return 0
    elif binaire=="01":
        return 1
    elif binaire=="10":
        return 2
    elif binaire=="11":
        return 3

def troiscaractereto10(binaire):
    if binaire=="000":
        return 0
    elif binaire=="001":
        return 1
    elif binaire=="010":
        return 2
    elif binaire=="011":
        return 3
    elif binaire=="100":
        return 4
    elif binaire=="101":
        return 5
    elif binaire=="110":
        return 6
    elif binaire=="111":
        return 7

def quatrecaractereto10(binaire):
    if binaire=="0000":
        return 0
    elif binaire=="0001":
        return 1
    elif binaire=="0010":
        return 2
    elif binaire=="0011":
        return 3
    elif binaire=="0100":
        return 4
    elif binaire=="0101":
        return 5
    elif binaire=="0110":
        return 6
    elif binaire=="0111":
        return 7
    elif binaire=="1000":
        return 8
    elif binaire=="1001":
        return 9
    elif binaire=="1010":
        return 10
    elif binaire=="1011":
        return 11
    elif binaire=="1100":
        return 12
    elif binaire=="1101":
        return 13
    elif binaire=="1110":
        return 14
    elif binaire=="1111":
        return 15

def cinqcaractereto10(binaire):
    if binaire=="00000":
        return 0
    elif binaire=="00001":
        return 1
    elif binaire=="00010":
        return 2
    elif binaire=="00011":
        return 3
    elif binaire=="00100":
        return 4
    elif binaire=="00101":
        return 5
    elif binaire=="00110":
        return 6
    elif binaire=="00111":
        return 7
    elif binaire=="01000":
        return 8
    elif binaire=="01001":
        return 9
    elif binaire=="01010":
        return 10
    elif binaire=="01011":
        return 11
    elif binaire=="01100":
        return 12
    elif binaire=="01101":
        return 13
    elif binaire=="01110":
        return 14
    elif binaire=="01111":
        return 15
    elif binaire=="10000":
        return 16
    elif binaire=="10001":
        return 17
    elif binaire=="10010":
        return 18
    elif binaire=="10011":
        return 19
    elif binaire=="10100":
        return 20
    elif binaire=="10101":
        return 21
    elif binaire=="10110":
        return 22
    elif binaire=="10111":
        return 23
    elif binaire=="11000":
        return 24
    elif binaire=="11001":
        return 25
    elif binaire=="11010":
        return 26
    elif binaire=="11011":
        return 27
    elif binaire=="11100":
        return 28
    elif binaire=="11101":
        return 29
    elif binaire=="11110":
        return 30
    elif binaire=="11111":
        return 31

# Exercice 7

def sixcaractereto10(binaire):
    if binaire[0]=="0":
        return cinqcaractereto10(binaire[1:])
    elif binaire[0]=="1":
        return 32+cinqcaractereto10(binaire[1:])

def septcaractereto10(binaire):
    if binaire[0]=="0":
        return sixcaractereto10(binaire[1:])
    elif binaire[0]=="1":
        return 64+sixcaractereto10(binaire[1:])

def huitcaractereto10(binaire):
    if binaire[0]=="0":
        return septcaractereto10(binaire[1:])
    elif binaire[0]=="1":
        return 128+septcaractereto10(binaire[1:])

# Exercice 8

def max9caractereto9V2(binaire):
    binaire = binaire[0:9]
    if binaire[0]=="0":
        return huitcaractereto10(binaire[1:])
    elif binaire[0]=="1":
        return 256+huitcaractereto10(binaire[1:])

def max9caractereto9(binaire):
    if len(binaire)==1:
        return uncaractereto10(binaire)
    elif len(binaire)==2:
        return deuxcaractereto10(binaire)
    elif len(binaire)==3:
        return troiscaractereto10(binaire)
    elif len(binaire)==4:
        return quatrecaractereto10(binaire)
    elif len(binaire)==5:
        return cinqcaractereto10(binaire)
    elif len(binaire)==6:
        return sixcaractereto10(binaire)
    elif len(binaire)==7:
        return septcaractereto10(binaire)
    elif len(binaire)==8:
        return huitcaractereto10(binaire)
    elif len(binaire)==9:
        if binaire[0]=="0":
            return huitcaractereto10(binaire[1:])
        elif binaire[0]=="1":
            return 256+huitcaractereto10(binaire[1:])
    else:
        print("Chiffre trop grand !")

# Fin du cour du 21 09 10

# Exercice 9

def binaireto10V2(binaire):
    return int(binaire) # soit disant de la triche

def binaireto10V3(binaire):
    nombreDeCaracteres = len(binaire)
    resultat = 0
    for loop in range(nombreDeCaracteres):
        caractere = binaire[nombreDeCaracteres - 1]
        resultat = resultat * 2(2*caractere)
    return resultat

def binaireto10(binaire):
    longueur = len(binaire)
    somme = 0
    for i in range(longueur):
        bit = binaire[i]
        bit = int(bit)
        nombre = bit*2**(longueur-i-1)
        somme = somme + nombre
    return somme

# Exercice 10

def maxuntobinaire(base10):
    if base10 == 0:
        return "0"
    elif base10 == 1:
        return "1"

def maxtroistobinaireV2(base10):
    if base10[0]==0:
        return 0#huitcaractereto10(binaire[1:])
    elif base10[0]==1:
        return 1#256+huitcaractereto10(binaire[1:])

def maxtroistobinaire(base10):
    if base10 == 0:
        return "00"
    elif base10 == 1:
        return "01"
    elif base10 == 2:
        return "10"
    elif base10 == 3:
        return "11"

def maxsepttobinaire(base10):
    if base10 == 0:
        return "000"
    elif base10 == 1:
        return "001"
    elif base10 == 2:
        return "010"
    elif base10 == 3:
        return "011"
    elif base10 == 4:
        return "100"
    elif base10 == 5:
        return "101"
    elif base10 == 6:
        return "110"
    elif base10 == 7:
        return "111"

def maxquinzetobinaire(base10):
    if base10 == 0:
        return "00000"
    elif base10 == 1:
        return "00001"
    elif base10 == 2:
        return "00010"
    elif base10 == 3:
        return "00011"
    elif base10 == 4:
        return "00100"
    elif base10 == 5:
        return "00101"
    elif base10 == 6:
        return "00110"
    elif base10 == 7:
        return "00111"
    elif base10 == 8:
        return "01000"
    elif base10 == 9:
        return "01001"
    elif base10 == 10:
        return "01010"
    elif base10 == 11:
        return "01011"
    elif base10 == 12:
        return "01100"
    elif base10 == 13:
        return "01101"
    elif base10 == 14:
        return "01110"
    elif base10 == 15:
        return "01111"

# Fin du cour du 21 09 16

# Exercice 11 :

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

def base10ToBinaireV2(base10):
    return int(base10, 2) # soit disant de la triche

def base10ToBinaireV3(base10):
    longueur = len(str(base10))
    resultat = ""
    for i in range(longueur):
        chiffre = str(base10)[i]
        #chiffre = str(bit)
        nombre = chiffre*2**(longueur - i - 1)
        resultat = resultat + nombre
    return resultat

# Exercice 14

def caractereHexaToBase10(decimal):
    if decimal == "0":
        return 0
    if decimal == "1":
        return 1
    if decimal == "2":
        return 2
    if decimal == "3":
        return 3
    if decimal == "4":
        return 4
    if decimal == "5":
        return 5
    if decimal == "6":
        return 6
    if decimal == "7":
        return 7
    if decimal == "8":
        return 8
    if decimal == "9":
        return 9
    if decimal == "A":
        return 10
    if decimal == "B":
        return 11
    if decimal == "C":
        return 12
    if decimal == "D":
        return 13
    if decimal == "E":
        return 14
    if decimal == "F":
        return 15

# Exercice 15

def base16ToBase10V2(decimal):
    print(int(decimal, 16))

def base16ToBase10V3(decimal):
    longueur = len(decimal)
    somme = 0
    for i in range(longueur):
        bit = decimal[i]
        bit = int(bit)
        nombre = bit*16**(longueur-i-1)
        somme = somme + nombre
    return somme

# Exercice 16

def base10ToBase16V2(hexadecimal):
    print(hex(hexadecimal)[2:])

def base10ToBase16V3(base10):
    i=0
    while 16**i <= base10:
        i = i + 1
    i = i - 1
    sortie = ""
    while i >= 0:
        if 16**i <= base10:
            sortie= sortie + "1"
            base10 = base10 - 16**i
        else:
            sortie = sortie + "0"
        i = i - 1
    return sortie

# Fin du cour du 21 09 17
