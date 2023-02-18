#Exercice 1

print("Exemple exercice 1 :")
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(25))
print(lfibonacci(45))
print()



#Exerice 2
def pantheon(eleves, notes):
    note_maxi = 0
    meilleurs_eleves =  ...

    for i in range(...) :
        if notes[i] == ... :
            meilleurs_eleves.append(...)
        elif notes[i] > note_maxi:
            note_maxi = ...
            meilleurs_eleves = [...]

    return (note_maxi,meilleurs_eleves)



eleves_nsi = ['a','b','c','d','e','f','g','h','i','j']
notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]

print("Exemple exercice 2 :")
print(pantheon(eleves_nsi,notes_nsi))
print(pantheon([],[]))