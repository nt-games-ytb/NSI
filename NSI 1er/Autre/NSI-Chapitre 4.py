def afficheliste(liste):
    for i in liste:
        print(i)


def moyenneliste(liste):
    somme=0
    for i in liste:
        somme=somme+i
    moy=somme/len(liste)
    return moy

def plusgrandliste(liste):
    plusgrand=liste[0]
    for i in liste:
        if i>plusgrand:
            plusgrand=i
    return plusgrand

def pluspetitliste(liste):
    pluspetit=liste[0]
    for i in liste:
        if i<pluspetit:
            pluspetit=i
    return pluspetit

def caractères(texte):
    liste=[]
    for i in texte:
        liste.append(i)
    return liste

def caractèresuniques(texte):
    liste=[]
    for i in texte:
        if i not in liste:
            liste.append(i)
    return liste

def sansespaces(texte):
    liste=[]
    for i in texte:
        if i !=" ":
            liste.append(i)
    return liste

def caractèresspéciauxV1(texte):
    liste=[]
    for i in texte:
        nombre=ord(i)
        if (nombre<=64) or (nombre>=91 and nombre(i)<=96) or (nombre>=123):
            liste.append(i)
        return liste

def caractèresspéciauxV2(texte):
    listefinale=[]
    listenormaux=[]
    for i in range(65,91):
        listenormaux.append(chr(i))
    for i in range(97,123):
        listenormaux.append(chr(i))
    for y in texte:
        if y not in listenormaux:
            listefinale.append(y)
    return listefinale

def trouvelesmots(texte):
    liste=[]
    mot=""
    for i in texte:
        if i==" ":
            liste.append(mot)
            mot=""
        else:
            mot=mot+i
    liste.append(mot)
    return liste

def trouvelesmotsV2(texte):
    liste=[]
    mot=""
    for i in texte:
        if i in [" ",",",";",":","!","?","(",")"]:
            liste.append(mot)
            mot=""
        else:
            mot=mot+i
    liste.append(mot)
    return liste

def estpaire(liste):
    return [x%2==0 for x in liste]


