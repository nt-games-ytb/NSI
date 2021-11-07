# Mystère

## Description

L'idée de ce TP est de manipuler les expressions booléennes.

Pour cela, vous allez devoir programmer des fonctions booléennes.

A chaque fonction `mystere` suivante, sont données des doctests.
Ces doctests correspondent aux valeurs des tables de vérités.

## Consignes

Recopier le bloc de code suivant dans un fichier `mystere.py`

Vous devez écrire le corps de la fonction sous la forme d'une expression booléenne, dont les variables correspondent aux paramètres d'entrée fournis.

```python
def mystere1(a):
    '''
        >>> mystere1(True)
        False
        >>> mystere1(False)
        True
    '''
    pass

def mystere2(a, b):
    '''
        >>> mystere2(True, True)
        True
        >>> mystere2(True, False)
        True
        >>> mystere2(False, True)
        True
        >>> mystere2(False, False)
        False
    '''
    pass

def mystere3(a, b):
    '''
        >>> mystere3(True, True)
        False
        >>> mystere3(True, False)
        True
        >>> mystere3(False, True)
        True
        >>> mystere3(False, False)
        False
    '''
    pass

def mystere4(a, b):
    '''
        >>> mystere4(True, True)
        False
        >>> mystere4(True, False)
        False
        >>> mystere4(False, True)
        False
        >>> mystere4(False, False)
        True
    '''
    pass

def mystere5(a, b):
    '''
        >>> mystere5(True, True)
        True
        >>> mystere5(True, False)
        False
        >>> mystere5(False, True)
        False
        >>> mystere5(False, False)
        True
    '''
    pass

def mystere6(a, b):
    '''
        >>> mystere6(True, True)
        False
        >>> mystere6(True, False)
        True
        >>> mystere6(False, True)
        False
        >>> mystere6(False, False)
        False
    '''
    pass

def mystere7(a, b):
    '''
        >>> mystere7(True, True)
        False
        >>> mystere7(True, False)
        True
        >>> mystere7(False, True)
        False
        >>> mystere7(False, False)
        True
    '''
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)
```