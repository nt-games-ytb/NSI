#Exercice 1
def nb_repetitions(elt, tab):
    repetition = 0
    for element in tab:
        if element == elt:
            repetition = repetition + 1
    return repetition

print("Exemple exercice 1 :")
print(nb_repetitions(5,[2,5,3,5,6,9,5]))
print(nb_repetitions('A',['B','A','B','A','R']))
print(nb_repetitions(12,[1,'!',7,21,36,44]))
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
print(binaire(0))
print(binaire(77))