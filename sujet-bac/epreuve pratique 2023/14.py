#Exercice 1
def recherche(elt, tab):
  indice = -1
  for i in range(len(tab)):
    if tab[i] == elt:
      indice = i
      return indice
  return indice
  
def recherche_mieux(elt, tab):
  for i in range(len(tab)):
    if tab[i] == elt:
      indice = i
      return i
  return -1
  
print("Exemple exercice 1 :")
print(recherche_mieux(1, [2, 3, 4]))
print(recherche_mieux(1, [10, 12, 1, 56]))
print(recherche_mieux(50, [1, 50, 1]))
print(recherche_mieux(15, [8, 9, 10, 15]))
print(recherche_mieux(50, []))
print(recherche_mieux(4, [2, 4, 4, 3, 4]))
print()



#Exercice 2
def insere(a, tab):
    """ Insère l'élément a (int) dans le tableau tab (list)
        trié par ordre croissant à sa place et renvoie le
        nouveau tableau. """
    l = list(tab) #l contient les memes elements que tab
    l.append(a)
    i = len(l) - 2
    while a < l[i] and i >= 0: 
      l[i+1] = l[i]
      l[i] = a
      i = i - 1
    return l
    
print("Exemple exercice 2 :")
print(insere(3, [1, 2, 4, 5]))
print(insere(30, [1, 2, 7, 12, 14, 25]))
print(insere(1, [2, 3, 4]))
print(insere(1, []))