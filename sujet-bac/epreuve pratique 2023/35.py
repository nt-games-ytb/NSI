#Exercice 1
def ou_exclusif(tableau1, tableau2):
    resultat = []
    for i in range(len(tableau1)):
        if tableau1[i] == tableau2[i]:
            resultat.append(0)
        else:
            resultat.append(1)
    return resultat

print("Exemple exercice 1 :")
a = [1, 0, 1, 0, 1, 1, 0, 1]
b = [0, 1, 1, 1, 0, 1, 0, 0]
c = [1, 1, 0, 1]
d = [0, 0, 1, 1]
print(ou_exclusif(a, b))
print(ou_exclusif(c, d))
print()



#Exerice 2
c2 = [[1, 7], [7, 1]]
c3 = [[3, 4, 5], [4, 4, 4], [5, 4, 3]]
c3bis = [[2, 9, 4], [7, 0, 3], [6, 1, 8]]


class Carre:
    def __init__(self, liste, n):
        self.ordre = n
        self.tableau = [[liste[i + j * n] for i in range(n)] for j in range(n)]

    def affiche(self):
        '''Affiche un carré'''
        for i in range(self.ordre):
            print(self.tableau[i])

    def somme_ligne(self, i):
        '''Calcule la somme des valeurs de la ligne i'''
        somme = 0
        for j in range(self.ordre):
            somme = somme + self.tableau[i][j]
        return somme

    def somme_col(self, j):
        '''Calcule la somme des valeurs de la colonne j'''
        somme = 0
        for i in range(self.ordre):
            somme = somme + self.tableau[i][j]
        return somme

    def est_semimagique(self):
        s = self.somme_ligne(0)

        #test de la somme de chaque ligne
        for i in range(self.ordre):
            if self.somme_ligne(i) != s:
                return False

        #test de la somme de chaque colonne
        for j in range(self.ordre):
            if self.somme_col(j) != s:
                return False

        return True

print("Exemple exercice 2 :")
liste_c2 = (3, 4, 5, 4, 4, 4, 5, 4, 3)
c2 = Carre(liste_c2, 3)
liste_c3 = (3, 4, 5, 4, 4, 4, 5, 4, 3)
c3 = Carre(liste_c3, 3)
liste_c3bis = (3, 4, 5, 4, 4, 4, 5, 4, 3)
c3_bis = Carre(liste_c3bis, 3)
print(c2.affiche())
print(c2.est_semimagique())
print(c3.affiche())
print(c3.est_semimagique())
print(c3_bis.affiche())
print(c3_bis.est_semimagique())