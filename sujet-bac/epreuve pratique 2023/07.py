#Exercice 1
def fusion(tab1, tab2):
    tab3 = []
    while tab1 != []:
        while tab2 != []:
            if tab1 == []:
                tab3 = tab3 + tab2
                tab2 = []
            elif tab1[0] <= tab2[0]:
                tab3.append(tab1.pop(0))
            else:
                tab3.append(tab2.pop(0))
        if tab2 == [] and tab1 != []:
            tab3 = tab3 + tab1
    return tab3

print("Exemple exercice 1 :")
print(fusion([3, 5], [2,5]))
print(fusion([-2, 4], [-3, 5, 10]))
print(fusion([4], [2, 6]))
print()



#Exercice 2
romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def traduire_romain(nombre) :
    """ Renvoie l'ecriture decimale du nombre donné en chiffres romains """

    if len(nombre) == 1:
        return romains[nombre]

    elif romains[nombre[0]] >= romains[nombre[1]]:
        return romains[nombre[0]] + traduire_romain(nombre[1:])
    else:
        return -romains[nombre[0]] + traduire_romain(nombre[1:])

print("Exemple exercice 2 :")
print(traduire_romain("XIV"))
print(traduire_romain("CXLII"))
print(traduire_romain("MMXXIII"))