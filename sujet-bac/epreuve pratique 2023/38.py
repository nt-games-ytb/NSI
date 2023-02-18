#Exercice 1

print("Exemple exercice 1 :")
print(correspond('INFORMATIQUE', 'INFO*MA*IQUE'))
print(correspond('AUTOMATIQUE', 'INFO*MA*IQUE'))
print(correspond('STOP', 'S*'))
print(correspond('AUTO', '*UT*'))
print()



#Exerice 2
def est_cyclique(plan):
    '''
    Prend en paramÃ¨tre un dictionnaire `plan` correspondant Ã  un plan d'envoi de messages (ici entre les personnes A, B, C, D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et False sinon.
    '''
    expediteur = 'A'
    destinataire = plan[ ... ]
    nb_destinaires = 1
    
    while destinataire != ...:
        destinataire = plan[ ... ]
        nb_destinaires += ...

    return nb_destinaires == ...

print("Exemple exercice 2 :")
print(est_cyclique({'A':'E',  'F':'A',  'C':'D',  'E':'B',  'B':'F', 'D':'C'}))
print(est_cyclique({'A':'E',  'F':'C',  'C':'D',  'E':'B',  'B':'F','D':'A'}))
print(est_cyclique({'A':'B',  'F':'C',  'C':'D',  'E':'A',  'B':'F', 'D':'E'}))
print(est_cyclique({'A':'B',  'F':'A',  'C':'D',  'E':'C',  'B':'F', 'D':'E'}))