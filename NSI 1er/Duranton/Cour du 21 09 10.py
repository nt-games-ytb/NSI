def uncaractereto10(binaire):
    if binaire=="0":
        return 0
    elif binaire=="1":
        return 1

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