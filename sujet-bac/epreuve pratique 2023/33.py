#Exercice 1

print("Exemple exercice 1 :")
a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], 
     'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'],
     'H':['','']}
print(taille(a, 'F'))
print()



#Exerice 2
def tri_selection(tab):
    N = len(tab)
    for k in range(...):
        imin = ...
        for i in range(... , N):
            if tab[i] < ... :
                imin = i
        ... , tab[imin] = tab[imin] , ...

print("Exemple exercice 2 :")
liste = [41, 55, 21, 18, 12, 6, 25]
tri_selection(liste)
print(liste)