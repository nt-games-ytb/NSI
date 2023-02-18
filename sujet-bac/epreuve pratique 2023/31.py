#Exercice 1

print("Exemple exercice 1 :")
print(nb_repetitions(5,[2,5,3,5,6,9,5]))
print(nb_repetitions('A',['B','A','B','A','R']))
print(nb_repetitions(12,[1,'!',7,21,36,44]))
print()



#Exerice 2
def binaire(a):
    bin_a = str(...)
    a = a // 2
    while a ... :
        bin_a = ...(a%2) + ...
        a = ...
    return bin_a

print("Exemple exercice 2 :")
print(binaire(0))
print(binaire(77))