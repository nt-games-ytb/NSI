#Exercice 1
def fibonacci(n):
    if n ==1 or n ==2:
        return 1
    else:
        premier_terme = 1
        second_terme = 1
        somme = 2
        
        for i in range(n - 3):
            premier_terme = second_terme
            second_terme = somme
            somme = premier_terme + second_terme
    return somme
    
def fibonacci_prof(n):
    if n ==1 or n ==2:
        return 1
    premier_nb = 1
    deuxieme_nb = 1
    for i in range(n - 3):
        tempo = deuxieme_nb
        deuxieme_nb = deuxieme_nb + premier_nb
        premier_nb = tempo
    return deuxieme_nb
    
def fibonacci_recursive(n): #Ne donne pas tout les points
    if n ==1 or n ==2:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
        
print("Exemple exercice 1 :")
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(25))
print(fibonacci(45))
print()



#Exerice 2
def pantheon(eleves, notes):
    note_maxi = 0
    meilleurs_eleves =  []

    for i in range(len(eleves)) :
        if notes[i] == note_maxi :
            meilleurs_eleves.append(eleves[i])
        elif notes[i] > note_maxi:
            note_maxi = notes[i]
            meilleurs_eleves = [eleves[i]]

    return (note_maxi,meilleurs_eleves)

eleves_nsi = ['a','b','c','d','e','f','g','h','i','j']
notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]

print("Exemple exercice 2 :")
print(pantheon(eleves_nsi,notes_nsi))
print(pantheon([],[]))