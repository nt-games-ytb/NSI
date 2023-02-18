#Exercice 1
def nbr_occurences(chaine):
    resultat = {}
    for element in chaine:
        if element in resultat:
            resultat[element] = resultat[element] + 1
        else:
            resultat[element] = 1
    return resultat

print("Exemple exercice 1 :")
print(nbr_occurences("Hello world !"))
print()



#Exerice 2
def fusion(lst1, lst2):
    n1 = len(lst1)
    n2 = len(lst2)
    lst12 = [0] * (n1 + n2)
    i1 = 0
    i2 = 0
    i=0
    while i1 < n1 and i2 < n2 :
        if lst1[i1] < lst2[i2]:
            lst12[i] = lst1[i1] 
            i1 = i1 + 1
        else:
            lst12[i] = lst2[i2]
            i2 = i2 + 1
        i += 1
    while i1 < n1:
        lst12[i] = lst1[i1] 
        i1 = i1 + 1
        i = i + 1
    while i2 < n2:
        lst12[i] = lst1[i2] 
        i2 = i2 + 1
        i = i + 1
    return lst12

print("Exemple exercice 2 :")
print(fusion([1, 6, 10], [0, 7, 8, 9]))