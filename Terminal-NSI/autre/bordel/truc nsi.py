def test(liste1, liste2):
    resultat = []
    while liste1 != [] and liste2 != []:
        if liste1[0] >= liste2[0]:
            element_supprimé = liste2.pop(-1)
            resultat.append(element_supprimé)
            print(resultat)
        else:
            element_supprimé = liste1.pop(-1)
            resultat.append(element_supprimé)
    print(resultat)


test([1,6,8], [2,4,7])