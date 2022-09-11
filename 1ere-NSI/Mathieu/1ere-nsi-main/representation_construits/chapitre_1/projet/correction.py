#! /usr/bin/env python3
# -*- coding : utf-8 -*-
# Author : Philippe BODDAERT
# Date : 01/08/2021
# License : CC-BY-NC-SA

import random, sys
from paint import dessiner, ROUGE, JAUNE, BLANC, BLEU, VERT

def creer_fils(couleur, longueur = 10):
    '''
    Créé un fils d'une longueur donnée
    :param couleur: (int) la couleur du fils
    :param longueur: (int) la longueur du fils
    :return: (list) Un fils sous la forme d'un tableau
    '''
    return [couleur] * longueur

def creer_bombe(couleurs):
    '''
    Créé une bombe de fils
    :param couleurs: (list) les couleurs des fils
    :return: (list) Un tableau de fils
    '''
    bombe = []
    for c in couleurs:
        bombe.append(creer_fils(c, 20))
    return bombe

def creer_combinaison(longueur):
    '''
    Créé une combinaison de couleurs de fils
    :param longueur: (int) le nombre de fils
    :return: (list) Un tableau de couleurs
    '''
    return [ random.choice([ROUGE, VERT, JAUNE, BLEU, BLANC]) for _ in range(longueur)]

def creer_numero_serie(longueur = 8):
    '''
    Créé un numéro de série d'une longueur donnée
    :param longueur: (int) longueur du numéro
    :return: (str) un numéro de longueurdonnée
    '''
    return str(random.randrange(0, 10**longueur)).zfill(8)

def afficher_bombe(bombe):
    '''
    Affiche une bombe de fils
    :param bombe: (list) une bombe de fils
    '''
    dessiner(bombe)

def couleur_fils(fils):
    '''
    Obtient la couleur d'un fils
    :param fils: (list) Un fil
    :return: (int) la couleur du fil
    '''
    return fils[0]

def compter_fils(bombe, couleur):
    '''
    Compte le nombre de fils de la couleur donnée
    :param bombe: (list) un tableau de fils
    :pram couleur: (int) une couleur
    :return: (int) Le nombre de fils de la couleur donnée
    '''
    nb = 0
    for fils in bombe:
        if couleur_fils(fils) == couleur:
            nb += 1
    return nb

def indice_dernier_fils(bombe, couleur):
    '''
    Détermine le dernier indice du fils de la couleur donnée
    :param bombe: (list) une bombe de fils
    :param couleur: (int) une couleur
    :return: (int) l'indice du fils, -1 sinon
    '''
    i = len(bombe) - 1
    while i >= 0 and couleur_fils(bombe[i]) != couleur:
        i -= 1
    return i

def est_dernier_chiffre_impair(numero):
    '''
    Détermine si le dernier chiffre du numéro de série est impair
    :param numero: (str) un numéro de série
    :return: (bool) True si le dernier chiffre est impair, False sinon
    '''
    return int(numero) % 2 == 1

def est_bon_fil_a_couper(bombe, indice, numero_serie=None):
    '''
    Détermine si le fil  à l'indice donné est celui à couper
    :param bombe: (list) une bombe de fils
    :param indice: (int) l'indice du fils à couper
    :return: (bool) True si le fils est le bon, False sinon
    '''
    n = len(bombe)
    if n == 3:
        if compter_fils(bombe, ROUGE) == 0:
            return indice == 1
        elif couleur_fils(bombe[n - 1]) == BLANC:
            return indice == n - 1
        elif compter_fils(bombe, BLEU) > 1:
            return indice == indice_dernier_fils(bombe, BLEU)
        else:
            return indice == n - 1
    elif n == 4:
        if compter_fils(bombe, ROUGE) > 1 and est_dernier_chiffre_impair(numero_serie):
            return indice == indice_dernier_fils(bombe, ROUGE)
        elif couleur_fils(bombe[n - 1]) == JAUNE and compter_fils(bombe, ROUGE) == 0:
            return indice == 0
        elif compter_fils(bombe, BLEU) == 1:
            return indice == 0
        elif compter_fils(bombe, JAUNE) > 1:
            return indice == n - 1
        else:
            return indice == 1
    elif n == 5:
        if couleur_fils(bombe[n - 1]) == VERT and est_dernier_chiffre_impair(numero_serie):
            return indice == 3
        elif compter_fils(bombe, ROUGE) == 1 and compter_fils(bombe, JAUNE) > 1:
            return indice == 0
        elif compter_fils(bombe, VERT) == 0:
            return indice == 1
        else:
            return indice == 0
    else:
        if compter_fils(bombe, JAUNE) == 0 and est_dernier_chiffre_impair(numero_serie):
            return indice == 2
        elif compter_fils(bombe, JAUNE) == 1 and compter_fils(bombe, BLANC) > 1:
            return indice == 3
        elif compter_fils(bombe, ROUGE) == 0:
            return indice == n - 1
        else:
            return indice == 3

if __name__ == '__main__':
    combinaison = 3
    numero_serie = None
    if len(sys.argv) > 1:
        combinaison = int(sys.argv[1])
        if combinaison > 3:
            numero_serie = creer_numero_serie()

    bombe = creer_bombe(creer_combinaison(combinaison))

    if numero_serie is not None:
        print(f"n°{numero_serie}")

    afficher_bombe(bombe)

    indice = input('Indice du fils à couper : ')

    if est_bon_fil_a_couper(bombe, int(indice), numero_serie):
        print('Sauvé !!!')
    else:
        print('Perdu, la bombe a explosé')