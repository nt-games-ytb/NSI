#Exercice 1
def moyenne(tab):
    total_des_notes = 0.0
    for element in tab:
        total_des_notes = total_des_notes + element
    return total_des_notes / len(tab)

def moyenne_rapide(tab):
    #assert len(tab) > 0, "Le tableau ne doit pas être vide !"
    return sum(tab) / len(tab)

print("Exemple exercice 1 :")
print(moyenne([1.0]))
print(moyenne([1.0, 2.0, 4.0]))
print()



#Exerice 2
def binaire(a):
    bin_a = str(a % 2)
    a = a // 2
    while a != 0 :
        bin_a = str(a % 2) + bin_a
        a = a // 2
    return bin_a

print("Exemple exercice 2 :")
print(binaire(83))
print(binaire(127))
print(binaire(0))