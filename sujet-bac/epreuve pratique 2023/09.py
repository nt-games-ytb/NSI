#Exercice 1
def multiplication(n1, n2):
    n3 = 0
    negatif = False
    if n1 < 0:
        negatif = True
        n1 = -n1
    for i in range(n1):
        n3 = n3 + n2
    if negatif == True:
        n3 = -n3
    return n3

print("Exemple exercice 1 :")
print(multiplication(3,5))
print(multiplication(-4,-8))
print(multiplication(-2,6))
print(multiplication(-2,0))
print()



#Exercice 2
def chercher(tab, n, i, j):
    if i < 0 or j > len(tab):
        return None
    elif i > j:
        return None
    m = (i + j) // 2
    if tab[m] < n:
        return chercher(tab, n, m + 1, j)
    elif tab[m] > n:
        return chercher(tab, n, i, m - 1)
    else:
        return m

print("Exemple exercice 2 :")
print(chercher([1,5,6,6,9,12],7,0,10))
print(chercher([1,5,6,6,9,12],7,0,5))
print(chercher([1,5,6,6,9,12],9,0,5))
print(chercher([1,5,6,6,9,12],6,0,5))