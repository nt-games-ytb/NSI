#Exercice 1
def moyenne_old(liste_notes):
    moyenne = 0
    total_points = 0
    total_coefficients = 0
    for element in liste_notes:
        total_points = total_points + element[0] * element[1]
        total_coefficients = total_coefficients + element[1]
    return total_points / total_coefficients

def moyenne(liste_notes):
    somme = 0
    coefficient = 0
    for element in liste_notes:
        somme = somme + element[0] * element[1]
        coefficient = coefficient + element[1]
    if coefficient == 0:
        return None
    return somme / coefficient

print("Exemple exercice 1 :")
print(moyenne([(15, 2), (9, 1), (12, 3)]))
print()



#Exercice 2 
def pascal(n):
    triangle = [[1]]
    for k in range(1, n + 1):
        ligne_k = [1]
        for i in range(1,k):
            ligne_k.append(triangle[-1][i-1]+triangle[-1][i])
        ligne_k.append(1)
        triangle.append(ligne_k)
    return triangle

print("Exemple exercice 2 :")
print(pascal(4))
print(pascal(5))