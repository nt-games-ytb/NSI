#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# Author : Philippe BODDAERT
# Date : 28/12/2020
# License : CC-BY-NC-SA
''' Module de génération de Drapeaux '''

import sys, copy
from paint import NOIR, ROUGE, VERT, JAUNE, BLEU, CYAN, BLANC, dessiner

def miroir_vertical(matrice):
    '''
    Inverse une matrice verticalment
    '''
    for ligne in matrice:
        ligne.reverse()

def miroir_horizontal(matrice):
    '''
    Inverse une matrice horizontalment
    '''
    matrice.reverse()

def creer_drapeau_france():
    '''
    Génère la matrice relative au drapeau de la France
    :return: (list) la matrice de codes couleurs
    '''
    return [ [BLEU] * 5 + [BLANC] * 5 + [ROUGE] * 5 for _ in range(7)]

def creer_drapeau_irlande():
    '''
    Génère la matrice relative au drapeau de l'Irlande
    :return: (list) la matrice de codes couleurs
    '''
    return [ [VERT] * 5 + [BLANC] * 5 + [ROUGE] * 5 for _ in range(7)]

def creer_drapeau_cote_ivoire():
    '''
    Génère la matrice relative au drapeau de la Côte d'Ivoire
    :return: (list) la matrice de codes couleurs
    '''
    drapeau = creer_drapeau_irlande()
    miroir_vertical(drapeau)
    return drapeau

def creer_drapeau_belgique():
    '''
    Génère la matrice relative au drapeau de la Belgique
    :return: (list) la matrice de codes couleurs
    '''
    return [ [NOIR] * 5 + [JAUNE] * 5 + [ROUGE] * 5 for _ in range(7)]

def creer_drapeau_pays_bas():
    '''
    Génère la matrice relative au drapeau des Pays-Bas
    :return: (list) la matrice de codes couleurs
    '''
    return [[BLEU] * 15] * 2  + [[BLANC] * 15] * 2 + [[ROUGE] * 15] * 2

def creer_drapeau_suede():
    '''
    Génère la matrice relative au drapeau de la Suède
    :return: (list) la matrice de codes couleurs
    '''
    bloc = [[BLEU] * 4 + [JAUNE] * 2 + [BLEU] * 9] * 3

    return bloc + [[JAUNE] * 15] + bloc

def creer_drapeau_finlande():
    '''
    Génère la matrice relative au drapeau de la Finlande
    :return: (list) la matrice de codes couleurs
    '''
    bloc = [[BLANC] * 4 + [BLEU] * 2 + [BLANC] * 9] * 3
    return bloc + [[BLEU] * 15] + bloc

def creer_drapeau_guinee():
    '''
    Génère la matrice relative au drapeau de la Guinée
    :return: (list) la matrice de codes couleurs
    '''
    return [ [ROUGE] * 5 + [JAUNE] * 5 + [VERT] * 5 for _ in range(7)]

def creer_drapeau_mali():
    '''
    Génère la matrice relative au drapeau du Mali
    :return: (list) la matrice de codes couleurs
    '''
    drapeau = creer_drapeau_guinee()
    miroir_vertical(drapeau)
    return drapeau

def creer_drapeau_monaco():
    '''
    Génère la matrice relative au drapeau de Monaco
    :return: (list) la matrice de codes couleurs
    '''
    return [[ROUGE] * 15] * 3 + [[BLANC] * 15] * 3

def creer_drapeau_pologne():
    '''
    Génère la matrice relative au drapeau de la Pologne
    :return: (list) la matrice de codes couleurs
    '''
    drapeau = creer_drapeau_monaco()
    miroir_horizontal(drapeau)
    return drapeau

def creer_drapeau_hongrie():
    '''
    Génère la matrice relative au drapeau de la Hongrie
    :return: (list) la matrice de codes couleurs
    '''
    return [[ROUGE] * 15] * 2 + [[BLANC] * 15] * 2 + [[VERT] * 15] * 2

def creer_drapeau_iran():
    '''
    Génère la matrice relative au drapeau d'Iran
    :return: (list) la matrice de codes couleurs
    '''
    drapeau = creer_drapeau_hongrie()
    miroir_horizontal(drapeau)
    return drapeau

def creer_drapeau_rc():
    '''
    Génère la matrice relative au drapeau de la République du Congo
    :return: (list) la matrice de codes couleurs
    '''
    drapeau = []
    for i in range(7):
        drapeau.append([VERT] * (12 - (i * 2)) + [JAUNE] * 3 + [ROUGE] * (i * 2))
    return drapeau

def creer_drapeau_trinidad():
    '''
    Génère la matrice relative au drapeau de Trinidad et Tobago
    :return: (list) la matrice de codes couleurs
    '''
    drapeau = []
    for i in range(7):
        drapeau.append([ROUGE] * (7 - i) + [BLANC] + [NOIR] * 4 + [BLANC] + [ROUGE] * (i + 2))
    miroir_vertical(drapeau)
    return drapeau

def creer_drapeau_etats_unis():
    '''
    Génère la matrice relative au drapeau des Etats-Unis
    :return: (list) la matrice de codes couleurs
    '''
    return  ([[BLEU, BLANC] * 3 + [BLEU] + [ROUGE] * 8] +
             [[BLEU, BLEU, BLANC, BLEU, BLANC, BLEU, BLEU] + [BLANC] * 8] +
             [[BLEU, BLANC] * 3 + [BLEU] + [ROUGE] * 8] +
             [[BLANC] * 15] + [[ROUGE] * 15] + [[BLANC] * 15])

def creer_drapeau_benin():
    '''
    Génère la matrice relative au drapeau du Bénin
    :return: (list) la matrice de codes couleurs
    '''
    return [[VERT] * 6 + [JAUNE] * 9 ] * 3 + [[VERT] * 6 + [ROUGE] * 9 ] * 3

def creer_drapeau_botswana():
    '''
    Génère la matrice relative au drapeau du Botswana
    :return: (list) la matrice de codes couleurs
    '''
    haut = [[CYAN] * 15] * 2 + [[BLANC] * 15]
    bas = haut.copy()
    miroir_horizontal(bas)
    return  haut + [[NOIR] * 15] + bas

def creer_drapeau_grece():
    '''
    Génère la matrice relative au drapeau de la Grèce
    :return: (list) la matrice de codes couleurs
    '''
    return  ([[BLEU] * 2 + [BLANC] + [BLEU] * 2 + [BLANC] * 10] +
             [[BLANC] * 5 + [BLEU] * 10] +
             [[BLEU] * 2 + [BLANC] + [BLEU] * 2 + [BLANC] * 10] +
             [[BLEU] * 15] + [[BLANC] * 15] + [[BLEU] * 15])

def creer_drapeau_suisse():
    '''
    Génère la matrice relative au drapeau de la Suisse
    :return: (list) la matrice de codes couleurs
    '''
    haut = [[ROUGE] * 15] + [[ROUGE] * 6 + [BLANC] * 3 + [ROUGE] * 6] * 2
    bas = haut.copy()
    miroir_horizontal(bas)
    return haut + [[ROUGE] * 3 + [BLANC] * 9 + [ROUGE] * 3] + bas

def creer_drapeau_japon():
    '''
    Génère la matrice relative au drapeau du Japon
    :return: (list) la matrice de codes couleurs
    '''
    haut = ([[BLANC] * 15] +
            [[BLANC] * 6 + [ROUGE] * 3 + [BLANC] * 6 ] +
            [[BLANC] * 4 + [ROUGE] * 7 + [BLANC] * 4 ])
    bas = haut.copy()
    miroir_horizontal(bas)
    return haut + [[BLANC] * 3 + [ROUGE] * 9 + [BLANC] * 3 ] + bas

def creer_drapeau_jamaique():
    '''
    Génère la matrice relative au drapeau de la Jamaique
    :return: (list) la matrice de codes couleurs
    '''
    haut = [[JAUNE] * 2 + [VERT] * 11 + [JAUNE] * 2,
        [NOIR] * 2 + [JAUNE] * 2 + [VERT] * 7 + [JAUNE] * 2 + [NOIR] * 2,
        [NOIR] * 4 + [JAUNE] * 2 + [VERT] * 3 + [JAUNE] * 2 + [NOIR] * 4]
    bas = haut.copy()
    miroir_horizontal(bas)
    return  haut + [[NOIR] * 6 + [JAUNE] * 3 + [NOIR] * 6] + bas

def creer_drapeau_palaos():
    '''
    Génère la matrice relative au drapeau du Palaos
    :return: (list) la matrice de codes couleurs
    '''
    haut = [[CYAN] * 15] + [[CYAN] * 5 + [JAUNE] * 3 + [CYAN] * 7 ] + [[CYAN] * 3 + [JAUNE] * 7 + [CYAN] * 5 ]
    bas = haut.copy()
    miroir_horizontal(bas)
    return haut + [[CYAN] * 2 + [JAUNE] * 9 + [CYAN] * 4 ] + bas

def creer_drapeau_republique_dominicaine():
    '''
    Génère la matrice relative au drapeau de la République Dominicaine
    :return: (list) la matrice de codes couleurs
    '''
    haut = [[BLEU] * 6 + [BLANC] * 3 + [ROUGE] * 6] * 3
    bas = copy.deepcopy(haut)
    miroir_horizontal(bas)
    miroir_vertical(bas)
    return haut + [[BLANC] * 7 + [BLEU] + [BLANC] * 7] + bas

DRAPEAUX = {
    'france' : creer_drapeau_france,
    'belgique' : creer_drapeau_belgique,
    'pays_bas' : creer_drapeau_pays_bas,
    'irlande' : creer_drapeau_irlande,
    'cote_ivoire' : creer_drapeau_cote_ivoire,
    'suede' : creer_drapeau_suede,
    'finlande' : creer_drapeau_finlande,
    'guinee' : creer_drapeau_guinee,
    'mali' : creer_drapeau_mali,
    'monaco' : creer_drapeau_monaco,
    'pologne' : creer_drapeau_pologne,
    'hongrie' : creer_drapeau_hongrie,
    'trinidad' : creer_drapeau_trinidad,
    'iran' : creer_drapeau_iran,
    'etats_unis' : creer_drapeau_etats_unis,
    'republique_congo' : creer_drapeau_rc,
    'benin' : creer_drapeau_benin,
    'botswana' : creer_drapeau_botswana,
    'grece' : creer_drapeau_grece,
    'suisse' : creer_drapeau_suisse,
    'japon' : creer_drapeau_japon,
    'jamaique' : creer_drapeau_jamaique,
    'palaos' : creer_drapeau_palaos,
    'dominique' : creer_drapeau_republique_dominicaine
    }

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        if sys.argv[1] == 'all':
            for nom, fonction in DRAPEAUX.items():
                print(nom)
                dessiner(fonction())
                print('')
        elif sys.argv[1] in DRAPEAUX:
            dessiner(DRAPEAUX[sys.argv[1]]())
        else:
            print(f'Le pays doit être dans la liste {list(DRAPEAUX.keys())}')
