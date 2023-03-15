#Exercice 1
def ecriture_binaire_entier_positif(n):
    """
    une fonction ecriture_binaire_entier_positif qui prend en paramètre un entier positif n
    et renvoie une liste d'entiers correspondant à l'écriture binaire de n.
    """
    assert type(n) == int, "Ce n'est pas un entier !"
    assert n >= 0, "L'entier ne pas positif !"
    if n == 0:
        return [0]
    resultat = []
    while n > 0:
        b = n % 2
        n = n // 2
        resultat.append(b)
    resultat.reverse()
    return resultat

def prof():
    liste=[]
    while n != 0:
        liste.append(n%2)
        n=n//2
        liste.reverse()
    return liste

print("Exemple exercice 1 :")
print(ecriture_binaire_entier_positif(0))
print(ecriture_binaire_entier_positif(2))
print(ecriture_binaire_entier_positif(105))
print()



#Exerice 2
def tri_bulles(T):
    '''
	Renvoie le tableau T trié par ordre croissant
	'''
    n = len(T)
    for i in range(n-1,-1, -1): #ou n-1, 0, -1
        for j in range(i):
            if T[j] > T[j + 1]:
                temp = T[j]
                T[j] = T[j + 1]
                T[j+1] = temp
    return T

print("Exemple exercice 2 :")
print(tri_bulles([]))
print(tri_bulles([7]))
print(tri_bulles([9, 3, 7, 2, 3, 1, 6]))
print(tri_bulles([9, 7, 4, 3]))