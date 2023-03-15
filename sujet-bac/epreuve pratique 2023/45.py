#Exercice 1
notes_eval = [2, 0, 5, 9, 6, 9, 10, 5, 7, 9, 9, 5, 0, 9, 6, 5, 4]

def rangement_valeurs(notes):
    resultat = [0] * 11
    for i in range(len(resultat)):
        for j in range(len(notes)):
            if notes[j] == i:
                resultat[i] = resultat[i] + 1
    return resultat
    
def rangement_valeurs_prof(notes_eval):
    resultat = [0] * 11
    for notes in notes_eval
        resultat[note] += 1
    return resultat

def notes_triees(liste):
    resultat = []
    for i in range(len(liste)):
        for j in range(liste[i]):
            resultat.append(i)
    return resultat

print("Exemple exercice 1 :")
print([2, 0, 5, 9, 6, 9, 10, 5, 7, 9, 9, 5, 0, 9, 6, 5, 4])
effectifs_notes = rangement_valeurs(notes_eval)
print(effectifs_notes)
print(notes_triees(effectifs_notes))
print()



#Exerice 2
def dec_to_bin (nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == 0:
        return str(r)
    else:
        return dec_to_bin(q) + str(r)

def bin_to_dec(nb_bin):
    if nb_bin == '0':
        return 0
    elif nb_bin == '1':
        return 1
    else:
        if nb_bin[-1] == '0':
            bit_droit = 0
        else:
            bit_droit = 1
        return 2 * bin_to_dec(nb_bin[:-1]) + bit_droit

print("Exemple exercice 2 :")
print(dec_to_bin(25))
print(bin_to_dec('101010'))