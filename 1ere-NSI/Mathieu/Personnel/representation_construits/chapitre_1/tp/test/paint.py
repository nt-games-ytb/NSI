#! /usr/bin/env python3
# -*- coding : utf-8 -*-
# Author : Philippe BODDAERT
# Date : 28/12/2020
# License : CC-BY-NC-SA
''' Affichage en couleur '''

NOIR = 0
ROUGE = 1
VERT = 2
JAUNE = 3
BLEU = 4
MAGENTA = 5
CYAN = 6
BLANC = 7

def case_couleur(back = 9):
    '''
    Renvoi le texte d'un espace dont la couleur de fond est celle donnée
    :param back: (int) le code couleur du fond du texte
    '''
    return couleur(' ', back)

def couleur(texte, back = 9, fore = 9):
    '''
    Renvoi le texte dans la couleur donnée
    :param fore: (int) le code couleur du texte
    :param back: (int) le code couleur de fond du texte
    :param texte: (str) texte à mettre en couleur
    :return: (str) le texte mis en couleur pour affichage
    '''
    return f"\033[3{fore}m\033[4{back}m{texte}\033[39m\033[49m"

def dessiner(matrice):
    '''
    Affiche le contenu de la matrice sous la forme de cases colorées
    :param matrice: (list) un tableau de tableaux
    :return: None
    :CU: les valeurs de la matrice doivent être comprises entre 0 et 7 inclus
    '''
    for ligne in matrice:
        for colonne in ligne:
            print(case_couleur(colonne), sep = '', end = '')
        print('')