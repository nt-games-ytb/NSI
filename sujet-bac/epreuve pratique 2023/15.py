#Exercice 1
t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018,
2019]

def mini(releve, date):
    plus_petite_valeur = releve[0]
    date_de_releve = date[0]
    for i in range(len(releve)):
        if plus_petite_valeur > releve[i]:
            plus_petite_valeur = releve[i]
            date_de_releve = date[i]
    return (plus_petite_valeur, date_de_releve)

print("Exemple exercice 1 :")
print(mini(t_moy, annees))
print()



#Exercice 2

def inverse_chaine(chaine):
    result = ""
    for caractere in chaine:
       result = caractere + result
    return result

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return chaine == inverse
    
def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)
    
print("Exemple exercice 2 :")
print(inverse_chaine('bac'))
print(est_palindrome('NSI'))
print(est_palindrome('ISN-NSI'))
print(est_nbre_palindrome(214312))
print(est_nbre_palindrome(213312))