#Exercice 1
def taille(arbre, lettre):
    if lettre == "":
        return 0
    return 1 + taille(arbre, arbre[lettre][0]) + taille(arbre, arbre[lettre][1])

print("Exemple exercice 1 :")
a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], 
     'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'],
     'H':['','']}
print(taille(a, 'F'))
print()



#Exerice 2
def tri_selection(tab):
    N = len(tab)
    for k in range(N - 1):
        imin = k
        for i in range(k + 1, N):
            if tab[i] < tab[imin] :
                imin = i
        tab[k] , tab[imin] = tab[imin] , tab[k]

print("Exemple exercice 2 :")
liste = [41, 55, 21, 18, 12, 6, 25]
tri_selection(liste)
print(liste)