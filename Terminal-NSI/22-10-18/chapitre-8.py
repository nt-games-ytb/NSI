#Exercice 2

#Question 1
def factRECURN(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factRECURN(n - 1)
    
#Question 2
def factITERA(n):
    for i in range(1, n):
        n = n * i
    return n
    


#Exerice 3

#Question 1
def fiboRECURN(n):
    if n == 0 or n == 1 or n == 2:
        return 1
    else:
        return fiboRECURN(n - 1) + fiboRECURN(n - 2)
       
#Question 2
def fiboITERA(n):
    if n == 0 or n == 1 or n == 2:
        return 1
    else:
        terme_avant_avant = 1
        terme_avant = 1
        terme = 2
        for i in range(n - 3):
            terme_avant_avant = terme_avant
            terme_avant = terme
            terme = terme_avant_avant + terme_avant
    return terme